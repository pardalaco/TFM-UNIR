import threading
import uuid
from pathlib import Path

from webapp.paths import JSONS_DIR

from evmaudit.runner import run_slither, run_mythril, run_echidna
from evmaudit.normalizer import normalize_slither_output, normalize_mythril_output
from evmaudit.correlator import correlate
from evmaudit.echidna_adapter import generate as generate_echidna_wrapper
from evmaudit.reporter import generate_report

TOTAL_STEPS = 7

jobs: dict = {}


def create() -> str:
    job_id = str(uuid.uuid4())[:8]
    jobs[job_id] = {
        "status": "running",
        "step": 0,
        "msg": "Iniciando...",
        "result": None,
        "error": None,
        "report_md": None,
    }
    return job_id


def launch(job_id: str, contract_path: str, contract_name: str) -> None:
    thread = threading.Thread(
        target=_run_pipeline, args=(job_id, contract_path, contract_name), daemon=True
    )
    thread.start()


def _run_pipeline(job_id: str, contract_path: str, contract_name: str) -> None:
    job = jobs[job_id]

    def set_step(step: int, msg: str) -> None:
        job["step"] = step
        job["msg"] = msg

    try:
        set_step(1, "Ejecutando Slither...")
        slither_raw = run_slither(contract_path)

        set_step(2, "Ejecutando Mythril (puede tardar 1-2 min)...")
        mythril_raw = run_mythril(contract_path, timeout=120, depth=22)

        set_step(3, "Normalizando resultados...")
        slither_norm = normalize_slither_output(slither_raw)
        mythril_norm = normalize_mythril_output(mythril_raw)

        set_step(4, "Correlacionando hallazgos...")
        corr = correlate(slither_norm, mythril_norm, contract_path)

        set_step(5, "Generando wrapper Echidna...")
        meta = generate_echidna_wrapper(corr, contract_path, contract_name)

        echidna_raw = {}
        if meta.get("wrapper_path"):
            set_step(6, "Ejecutando Echidna (fuzzing)...")
            echidna_raw = run_echidna(
                meta["wrapper_path"],
                meta["contract_name_echidna"],
                output_contract_path=contract_path,
            )

        set_step(7, "Generando informe...")
        report = generate_report(contract_path, corr, echidna_raw, meta)

        contract_stem = Path(contract_path).stem
        md_path = JSONS_DIR / contract_stem / f"{contract_stem}_report.md"
        job["report_md"] = md_path.read_text() if md_path.exists() else None
        job["status"] = "done"
        job["result"] = report

    except Exception as e:
        job["status"] = "error"
        job["error"] = str(e)
