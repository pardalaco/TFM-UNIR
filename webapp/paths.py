import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
EVMAUDIT_SRC = ROOT_DIR / "evmaudit" / "src"
JSONS_DIR = ROOT_DIR / "jsons"
UPLOADS_DIR = JSONS_DIR / "_uploads"

if str(EVMAUDIT_SRC) not in sys.path:
    sys.path.insert(0, str(EVMAUDIT_SRC))
