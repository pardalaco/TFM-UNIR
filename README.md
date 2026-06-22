# EVMAudit — TFM UNIR

> **Trabajo Fin de Máster** · Daniel Rovira Martínez, Paula Suárez Prieto, Adrián Moreno Martín  
> Máster en Ciberseguridad · UNIR

Pipeline multiherramienta para el análisis automatizado de vulnerabilidades en contratos inteligentes compatibles con la Ethereum Virtual Machine (EVM).

---

## ¿Qué es este proyecto?

Los contratos inteligentes operan en entornos públicos y adversariales, y sus errores son irreversibles una vez desplegados. Existen herramientas especializadas para detectar vulnerabilidades (Slither, Mythril, Echidna), pero cada una genera resultados con formatos, severidades y nomenclaturas distintas, obligando al auditor a revisar múltiples salidas heterogéneas de forma manual.

**EVMAudit** integra estas tres herramientas en un pipeline automatizado de siete pasos que:

1. Ejecuta **Slither** (análisis estático)
2. Ejecuta **Mythril** (ejecución simbólica)
3. **Normaliza** las salidas a una estructura común
4. **Correlaciona** hallazgos equivalentes entre herramientas, eliminando redundancias
5. Genera automáticamente **propiedades para Echidna** a partir del catálogo SWC
6. Ejecuta **Echidna** (fuzzing basado en propiedades)
7. Produce un **informe consolidado** en JSON y Markdown con puntuación de riesgo (`risk_score`)

El mecanismo de correlación es la contribución principal: dos vulnerabilidades detectadas independientemente por Slither y Mythril sobre la misma función y con el mismo SWC se unifican en un único hallazgo con `confidence_score: 3` (confirmado), reduciendo el ruido entre un 60 y un 75 % en los casos evaluados.

La lógica de análisis está publicada como librería independiente en PyPI: [`evmaudit`](https://pypi.org/project/evmaudit/).

---

## Estructura del repositorio

```
TFM-UNIR/
├── evmaudit/              # Submódulo Git — librería Python publicada en PyPI
│   ├── src/evmaudit/
│   │   ├── runner.py          # Ejecución de Slither, Mythril y Echidna
│   │   ├── normalizer.py      # Normalización de salidas heterogéneas
│   │   ├── correlator.py      # Correlación de hallazgos por (contrato, función, SWC)
│   │   ├── swc_catalog.py     # Catálogo SWC con plantillas para Echidna
│   │   ├── echidna_adapter.py # Generación automática de wrappers Solidity
│   │   ├── reporter.py        # Informes JSON y Markdown con risk_score
│   │   ├── exceptions.py      # Jerarquía de excepciones propia
│   │   └── main.py            # Punto de entrada CLI (evmaudit <contrato.sol>)
│   └── pyproject.toml
├── webapp/                # Aplicación web (FastAPI + HTML/CSS/JS vanilla)
│   ├── app.py             # API REST con endpoints /analyze, /status, /result
│   └── static/            # Frontend SPA en modo oscuro
├── contracts/             # Contratos Solidity de prueba
│   ├── VulnerableBank.sol     # Reentrancy (SWC-107)
│   └── MultiVuln.sol          # Reentrancy + Selfdestruct + tx.origin
├── tests/                 # Tests de integración del pipeline
├── Dockerfile             # Imagen Ubuntu 22.04 con Slither, Mythril y Echidna
├── docker-compose.yml     # Build local, puerto 8080
├── docker-compose.gh-img.yml  # Imagen pre-construida desde GHCR, puerto 8081
├── pyproject.toml         # Workspace uv (gestión de dependencias)
└── uv.lock                # Lockfile reproducible
```

> `evmaudit` es un submódulo Git que apunta al repositorio [pardalaco/evmaudit](https://github.com/pardalaco/evmaudit). Al clonar este repo hay que inicializar los submódulos (ver instrucciones abajo).

---

## Tecnología

| Capa                    | Tecnología                                                                     |
| ----------------------- | ------------------------------------------------------------------------------ |
| Lenguaje principal      | Python 3.12                                                                    |
| Gestión de dependencias | [uv](https://docs.astral.sh/uv/) (Astral)                                      |
| Análisis estático       | [Slither](https://github.com/crytic/slither) ≥ 0.9.2                           |
| Ejecución simbólica     | [Mythril](https://github.com/ConsenSysDiligence/mythril) ≥ 0.24.8              |
| Fuzzing                 | [Echidna](https://github.com/crytic/echidna) 2.3.2                             |
| Gestión de compiladores | [solc-select](https://github.com/crytic/solc-select)                           |
| Backend web             | [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/) |
| Frontend                | HTML5 / CSS3 / JavaScript (sin frameworks)                                     |
| Contenerización         | Docker + Docker Compose                                                        |
| CI/CD                   | GitHub Actions → GHCR                                                          |
| Despliegue cloud        | [Railway](https://railway.app/) (EU — Ámsterdam)                               |
| Distribución librería   | [PyPI](https://pypi.org/project/evmaudit/)                                     |

---

## Despliegue con Docker

Es la forma más sencilla de arrancar la aplicación web completa con todas las dependencias ya instaladas.

### Opción A — Build local (desde el código fuente)

```bash
# 1. Clonar el repositorio con sus submódulos
git clone --recurse-submodules https://github.com/pardalaco/TFM-UNIR.git
cd TFM-UNIR

# 2. Construir la imagen y arrancar el contenedor
docker compose up -d

# 3. Ver los logs en tiempo real
docker compose logs -f evmaudit-web
```

La webapp queda disponible en **http://localhost:8080**.

### Opción B — Imagen pre-construida desde GitHub Container Registry

Si no quieres compilar la imagen localmente, puedes usar la imagen publicada automáticamente por el pipeline de CI:

```bash
docker compose -f docker-compose.gh-img.yml up -d
```

La webapp queda disponible en **http://localhost:8081**.

### Parar el servicio

```bash
docker compose down
```

Los resultados de los análisis se persisten en `./jsons/_uploads/` gracias al volumen montado, y no se pierden al apagar el contenedor.

---

## Ejecución local sin Docker

Para ejecutar el pipeline directamente desde la línea de comandos o levantar la webapp en local sin Docker.

### Requisitos previos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado
- Slither, Mythril y Echidna instalados en el sistema (ver abajo)

### 1. Clonar con submódulos

```bash
git clone --recurse-submodules https://github.com/pardalaco/TFM-UNIR.git
cd TFM-UNIR
```

### 2. Instalar las herramientas de análisis externas

**Echidna** (binario nativo):

```bash
# macOS
brew install echidna

# Linux — descargar el binario estático
curl -L https://github.com/crytic/echidna/releases/download/v2.3.2/echidna-2.3.2-x86_64-linux.tar.gz \
  | tar -xz -C /usr/local/bin/
```

**Compilador Solidity:**

```bash
solc-select install 0.8.20
solc-select use 0.8.20
```

### 3. Instalar dependencias Python con uv

```bash
uv sync
source .venv/bin/activate
```

### 4a. Usar la CLI de EVMAudit

```bash
# Analizar un contrato (genera informe en jsons/<contrato>/)
evmaudit contracts/VulnerableBank.sol
evmaudit contracts/MultiVuln.sol
```

### 4b. Levantar la webapp en local

```bash
python3 -m uvicorn webapp.app:app --host 0.0.0.0 --port 8000
```

Interfaz disponible en **http://localhost:8000**.

---

## Contratos de prueba incluidos

| Archivo              | Vulnerabilidades                                        | SWC                       |
| -------------------- | ------------------------------------------------------- | ------------------------- |
| `VulnerableBank.sol` | Reentrancy en `withdraw()`                              | SWC-107                   |
| `MultiVuln.sol`      | Reentrancy + Selfdestruct sin restricción + `tx.origin` | SWC-107, SWC-106, SWC-115 |

## Pipeline en detalle

```
contrato.sol
     │
     ▼
 [Runner]──────────────────────────────────────────────────────────┐
     │  run_slither()          run_mythril()                       │
     ▼                              ▼                              │
 slither_raw.json          mythril_raw.json                        │
     │                              │                              │
     ▼──────────[Normalizer]────────▼                              │
                    │                                              │
          hallazgos normalizados (Finding)                         │
                    │                                              │
                    ▼                                              │
              [Correlator]                                         │
          clave: (contrato, función, SWC)                          │
          confidence_score: 3 (confirmado) / 2 (detectado)        │
                    │                                              │
                    ▼                                              │
            [SWC Catalog]                                          │
          plantillas Echidna por detector                          │
                    │                                              │
                    ▼                                              │
          [Echidna Adapter]                                        │
          genera wrapper .sol con propiedades echidna_*            │
                    │                                              │
                    ▼                                              │
          run_echidna() ◄─────────────────────────────────────────┘
                    │
                    ▼
              [Reporter]
    _report.json + _report.md + risk_score (0–10)
```

---

## CI/CD

El repositorio incluye un workflow de GitHub Actions (`.github/workflows/`) que:

1. Se activa en cada push a `main` o pull request
2. Construye la imagen Docker con la arquitectura `linux/amd64`
3. Publica la imagen en **GitHub Container Registry** con doble etiqueta: `:<sha>` y `:latest`

La imagen publicada es la que usa `docker-compose.gh-img.yml`.

---

## Instalación de la librería desde PyPI

Si solo quieres usar el motor de análisis sin la webapp:

```bash
pip install evmaudit
# o
uv add evmaudit
```

Ejemplo de uso en Python:

```python
from evmaudit.runner import run_slither, run_mythril
from evmaudit.normalizer import normalize_slither_output, normalize_mythril_output
from evmaudit.correlator import correlate
from evmaudit.reporter import generate_report

slither_raw = run_slither("mi_contrato.sol")
mythril_raw = run_mythril("mi_contrato.sol")
slither_norm = normalize_slither_output(slither_raw)
mythril_norm = normalize_mythril_output(mythril_raw)
corr = correlate(slither_norm, mythril_norm, "mi_contrato.sol")
report = generate_report("mi_contrato.sol", corr)
```

---

## Autores

- **Daniel Rovira Martínez**
- **Paula Suárez Prieto**
- **Adrián Moreno Martín**
