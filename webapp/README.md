# EVMAudit — Interfaz Web

Interfaz web local para analizar contratos inteligentes de Ethereum.  
Replica el estilo de VirusTotal con dos modos de entrada: subir archivo `.sol` o pegar código directamente.

---

## Requisitos previos

Antes de arrancar la webapp necesitas tener instalado:

| Herramienta   | Instalación                  |
| ------------- | ---------------------------- |
| Python 3.12+  | https://python.org           |
| uv            | `pip install uv`             |
| Echidna 2.3.2 | `brew install echidna` (Mac) |

Slither y Mythril se instalan automáticamente con `uv sync`.

---

## Instalación

### Si ya tienes el repo clonado

```bash
cd ~/Documents/TFM-Workspace/TFM-UNIR

git pull origin main

source .venv/bin/activate

uv sync
```

### Si partes de cero

```bash
git clone https://github.com/pardalaco/TFM-UNIR.git
cd TFM-UNIR

uv sync
uv pip install -e evmaudit/

source .venv/bin/activate

uv sync
```

---

## Arrancar el servidor

```bash
source .venv/bin/activate
python3 -m uvicorn webapp.app:app --host 0.0.0.0 --port 8000
```

Abre el navegador en: **http://localhost:8000**

Para parar el servidor: `CTRL + C`

---

## Modos de análisis

### FILE — Subir archivo

Arrastra un archivo `.sol` o usa el botón de selección.  
El nombre del contrato se detecta automáticamente desde el código fuente, independientemente del nombre del archivo.

### CODE — Pegar código

Escribe el nombre del contrato, pega el código Solidity en el editor y pulsa **Analizar código**.

---

## Pipeline de análisis

La webapp ejecuta el pipeline completo de EVMAudit en 7 pasos:

```
1. Slither      → análisis estático (~1 seg)
2. Mythril      → ejecución simbólica (~1-2 min)
3. Normalización → formato común para ambas herramientas
4. Correlación  → agrupa hallazgos por (contrato, función, SWC)
5. Adapter      → genera wrapper Solidity con propiedades Echidna
6. Echidna      → fuzzing basado en propiedades (~30 seg)
7. Informe      → JSON + Markdown + risk score 0-10
```

Los resultados se guardan en `jsons/_uploads/{contrato}/`.

---

## Estructura de archivos

```
webapp/
├── app.py              # Backend FastAPI
├── static/
│   └── index.html      # Frontend (HTML + CSS + JS, sin dependencias externas)
└── README.md           # Este archivo
```

---

## Solución de problemas

**Error en el paso 6 (Echidna):**  
Echidna no está instalado. Ejecutar: `brew install echidna`

**Error: "No existe el contrato":**  
El servidor debe arrancarse desde la raíz del workspace (`TFM-UNIR/`), no desde dentro de `webapp/`.

**Mythril tarda mucho:**  
Normal. Mythril hace ejecución simbólica y puede tardar hasta 2 minutos por contrato. La barra de progreso lo refleja.

**Puerto 8000 ocupado:**  
Cambiar el puerto: `python3 -m uvicorn webapp.app:app --port 8001`
