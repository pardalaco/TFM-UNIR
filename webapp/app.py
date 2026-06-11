import sys
import uuid
import re
import threading
import tempfile
import os
from io import BytesIO
from pathlib import Path
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
import markdown2
from xhtml2pdf import pisa

sys.path.insert(0, str(Path(__file__).parent.parent / "evmaudit" / "src"))

from evmaudit.runner import run_slither, run_mythril, run_echidna, detect_contract_name
from evmaudit.normalizer import normalize_slither_output, normalize_mythril_output
from evmaudit.correlator import correlate
from evmaudit.echidna_adapter import generate as generate_echidna_wrapper
from evmaudit.reporter import generate_report

# xhtml2pdf no soporta emojis a color: se renderizan como cuadros que
# se solapan con el texto siguiente. Se eliminan antes de generar el PDF.
PDF_EMOJI_STRIP = str.maketrans("", "", "🔴🟠🟡🟢⚪✅❌⚠️⚠")

# xhtml2pdf no calcula bien el ancho automático de columnas: una celda larga
# sin espacios (ej. "unprotected_selfdestruct") se solapa con la columna
# siguiente. Se fijan anchos proporcionales para la tabla de hallazgos.
PDF_FINDINGS_TABLE_RE = re.compile(
    r"(<thead>(?:(?!</thead>).)*Tipo(?:(?!</thead>).)*Severidad(?:(?!</thead>).)*</thead>)",
    re.S,
)
PDF_FINDINGS_COL_WIDTHS = ["4%", "11%", "9%", "24%", "10%", "13%", "29%"]


def _set_findings_table_widths(html: str) -> str:
    def add_widths(match: re.Match) -> str:
        widths = iter(PDF_FINDINGS_COL_WIDTHS)
        return re.sub(r"<th>", lambda _: f'<th style="width:{next(widths)}">', match.group(1))

    return PDF_FINDINGS_TABLE_RE.sub(add_widths, html, count=1)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

# Jobs en memoria: {job_id: {status, step, total_steps, result, error}}
jobs: dict = {}


def run_pipeline(job_id: str, contract_path: str, contract_name: str):
    job = jobs[job_id]

    def update(step: int, msg: str):
        job["step"] = step
        job["msg"] = msg

    try:
        update(1, "Ejecutando Slither...")
        slither_raw = run_slither(contract_path)

        update(2, "Ejecutando Mythril (puede tardar 1-2 min)...")
        mythril_raw = run_mythril(contract_path, timeout=120, depth=22)

        update(3, "Normalizando resultados...")
        slither_norm = normalize_slither_output(slither_raw)
        mythril_norm  = normalize_mythril_output(mythril_raw)

        update(4, "Correlacionando hallazgos...")
        corr = correlate(slither_norm, mythril_norm, contract_path)

        update(5, "Generando wrapper Echidna...")
        meta = generate_echidna_wrapper(corr, contract_path, contract_name)

        echidna_raw = {}
        if meta.get("wrapper_path"):
            update(6, "Ejecutando Echidna (fuzzing)...")
            echidna_raw = run_echidna(
                meta["wrapper_path"],
                meta["contract_name_echidna"],
                output_contract_path=contract_path,
            )

        update(7, "Generando informe...")
        report = generate_report(contract_path, corr, echidna_raw, meta)

        contract_stem = Path(contract_path).stem
        md_path = Path(__file__).parent.parent / "jsons" / contract_stem / f"{contract_stem}_report.md"
        job["report_md"] = md_path.read_text() if md_path.exists() else None

        job["status"] = "done"
        job["result"] = report

    except Exception as e:
        job["status"] = "error"
        job["error"] = str(e)


@app.get("/", response_class=HTMLResponse)
def index():
    return (Path(__file__).parent / "static" / "index.html").read_text()


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()

    tmp_dir = Path(__file__).parent.parent / "jsons" / "_uploads"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    contract_path = str(tmp_dir / file.filename)
    Path(contract_path).write_bytes(content)

    # Detectar el nombre real del contrato desde el código fuente
    # evita el bug cuando el archivo se llama diferente al contrato
    contract_name = detect_contract_name(contract_path) or Path(file.filename).stem

    job_id = str(uuid.uuid4())[:8]
    jobs[job_id] = {"status": "running", "step": 0, "msg": "Iniciando...", "result": None, "error": None, "report_md": None}

    thread = threading.Thread(target=run_pipeline, args=(job_id, contract_path, contract_name), daemon=True)
    thread.start()

    return {"job_id": job_id}


class CodePayload(BaseModel):
    code: str
    contract_name: str = "MiContrato"

@app.post("/analyze-code")
async def analyze_code(payload: CodePayload):
    tmp_dir = Path(__file__).parent.parent / "jsons" / "_uploads"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    contract_path = str(tmp_dir / f"{payload.contract_name}.sol")
    Path(contract_path).write_text(payload.code)

    # Detectar nombre real del contrato desde el código pegado
    contract_name = detect_contract_name(contract_path) or payload.contract_name

    job_id = str(uuid.uuid4())[:8]
    jobs[job_id] = {"status": "running", "step": 0, "msg": "Iniciando...", "result": None, "error": None, "report_md": None}

    thread = threading.Thread(target=run_pipeline, args=(job_id, contract_path, contract_name), daemon=True)
    thread.start()
    return {"job_id": job_id}


@app.get("/status/{job_id}")
def status(job_id: str):
    job = jobs.get(job_id)
    if not job:
        return JSONResponse({"error": "Job no encontrado"}, status_code=404)
    return {
        "status": job["status"],
        "step":   job["step"],
        "total":  7,
        "msg":    job["msg"],
        "error":  job.get("error"),
    }


@app.get("/result/{job_id}")
def result(job_id: str):
    job = jobs.get(job_id)
    if not job:
        return JSONResponse({"error": "Job no encontrado"}, status_code=404)
    if job["status"] != "done":
        return JSONResponse({"error": "Análisis no completado"}, status_code=400)
    return job["result"]


@app.get("/result/{job_id}/pdf")
def result_pdf(job_id: str):
    job = jobs.get(job_id)
    if not job:
        return JSONResponse({"error": "Job no encontrado"}, status_code=404)
    if job["status"] != "done" or not job.get("report_md"):
        return JSONResponse({"error": "Informe no disponible"}, status_code=400)

    md_text = job["report_md"].translate(PDF_EMOJI_STRIP)
    html = markdown2.markdown(md_text, extras=["tables", "fenced-code-blocks"])
    html = _set_findings_table_widths(html)
    html = f"""<html><head><style>
        body {{ font-family: Helvetica, sans-serif; font-size: 11px; }}
        h1, h2, h3 {{ color: #1a1c2e; }}
        table {{ border-collapse: collapse; width: 100%; margin-bottom: 1em; table-layout: fixed; }}
        th, td {{
            border: 1px solid #ccc; padding: 4px 8px; text-align: left;
            word-wrap: break-word; overflow-wrap: break-word; word-break: break-all;
        }}
        th {{ background: #eef0fa; }}
        code {{ background: #f4f4f4; padding: 1px 3px; }}
    </style></head><body>{html}</body></html>"""

    pdf_buffer = BytesIO()
    pisa.CreatePDF(html, dest=pdf_buffer)

    contract_name = job["result"]["meta"]["contract"]
    return Response(
        content=pdf_buffer.getvalue(),
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{contract_name}_report.pdf"'},
    )
