import sys
import uuid
import threading
import tempfile
import os
from pathlib import Path
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

sys.path.insert(0, str(Path(__file__).parent.parent / "evmaudit" / "src"))

from evmaudit.runner import run_slither, run_mythril, run_echidna, detect_contract_name
from evmaudit.normalizer import normalize_slither_output, normalize_mythril_output
from evmaudit.correlator import correlate
from evmaudit.echidna_adapter import generate as generate_echidna_wrapper
from evmaudit.reporter import generate_report

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
    jobs[job_id] = {"status": "running", "step": 0, "msg": "Iniciando...", "result": None, "error": None}

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
    jobs[job_id] = {"status": "running", "step": 0, "msg": "Iniciando...", "result": None, "error": None}

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
