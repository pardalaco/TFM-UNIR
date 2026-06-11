# Rutas compartidas por toda la webapp. Centralizarlas aquí evita que cada
# módulo tenga que recalcular su posición relativa al repo.

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
EVMAUDIT_SRC = ROOT_DIR / "evmaudit" / "src"
JSONS_DIR = ROOT_DIR / "jsons"
UPLOADS_DIR = JSONS_DIR / "_uploads"

# evmaudit no está instalado como paquete (vive en evmaudit/src dentro del
# repo), así que lo añadimos al path para poder importarlo como librería.
if str(EVMAUDIT_SRC) not in sys.path:
    sys.path.insert(0, str(EVMAUDIT_SRC))
