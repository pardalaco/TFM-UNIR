from pathlib import Path

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from webapp.paths import UPLOADS_DIR
from webapp import jobs
from webapp.pdf_export import render_pdf

from evmaudit.runner import detect_contract_name

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")


class CodePayload(BaseModel):
    code: str
    contract_name: str = "MiContrato"


def _start_analysis(contract_path: Path, fallback_name: str) -> str:
    contract_name = detect_contract_name(str(contract_path)) or fallback_name
    job_id = jobs.create()
    jobs.launch(job_id, str(contract_path), contract_name)
    return job_id


@app.get("/", response_class=HTMLResponse)
def index():
    return (Path(__file__).parent / "static" / "index.html").read_text()


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    contract_path = UPLOADS_DIR / file.filename
    contract_path.write_bytes(await file.read())

    job_id = _start_analysis(contract_path, Path(file.filename).stem)
    return {"job_id": job_id}


@app.post("/analyze-code")
async def analyze_code(payload: CodePayload):
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    contract_path = UPLOADS_DIR / f"{payload.contract_name}.sol"
    contract_path.write_text(payload.code)

    job_id = _start_analysis(contract_path, payload.contract_name)
    return {"job_id": job_id}


@app.get("/status/{job_id}")
def status(job_id: str):
    job = jobs.jobs.get(job_id)
    if not job:
        return JSONResponse({"error": "Job no encontrado"}, status_code=404)
    return {
        "status": job["status"],
        "step": job["step"],
        "total": jobs.TOTAL_STEPS,
        "msg": job["msg"],
        "error": job.get("error"),
    }


@app.get("/result/{job_id}")
def result(job_id: str):
    job = jobs.jobs.get(job_id)
    if not job:
        return JSONResponse({"error": "Job no encontrado"}, status_code=404)
    if job["status"] != "done":
        return JSONResponse({"error": "Análisis no completado"}, status_code=400)
    return job["result"]


@app.get("/result/{job_id}/pdf")
def result_pdf(job_id: str):
    job = jobs.jobs.get(job_id)
    if not job:
        return JSONResponse({"error": "Job no encontrado"}, status_code=404)
    if job["status"] != "done" or not job.get("report_md"):
        return JSONResponse({"error": "Informe no disponible"}, status_code=400)

    contract_name = job["result"]["meta"]["contract"]
    return Response(
        content=render_pdf(job["report_md"]),
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{contract_name}_report.pdf"'},
    )
