## 📋 Requisitos Previos

1. **Tener `uv` instalado**: Si no lo tienes, puedes instalarlo en macOS/Linux con:

```

```text
File GUIA_PUBLICACION_UV.md created successfully.

```bash
   curl -sSf [https://url.e.uv.io/install.sh](https://url.e.uv.io/install.sh) | sh

```

2. **Cuenta en PyPI**: Regístrate en [PyPI.org](https://pypi.org/).
3. **Token de API de PyPI**:
* Ve a **Account settings** > **API tokens**.
* Genera un nuevo token (si es el primer paquete, dale alcance global a la cuenta; tras la primera subida, podrás limitarlo solo a este paquete).
* Guarda el token de forma segura (`pypi-...`).



---

## 1. Configuración del Proyecto (`pyproject.toml`)

El archivo `pyproject.toml` en la raíz de tu paquete debe definir correctamente los metadatos. Un ejemplo limpio utilizando `hatchling` como sistema de construcción:

```toml
[project]
name = "evmaudit"
version = "0.1.0"
description = "Herramienta de auditoría para la EVM (Ethereum Virtual Machine)"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    { name = "Daniel", email = "tu-email@ejemplo.com" }
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

```

---

## 2. Compilación del Paquete

El comando `uv build` se encarga de empaquetar tu código fuente en los formatos de distribución estándar (`.tar.gz` y `.whl`).

### Caso A: Estructura de Proyecto Estándar

Si tu terminal está situada en la raíz del proyecto donde reside el `pyproject.toml` que quieres publicar, simplemente ejecuta:

```bash
uv build

```

Esto creará una carpeta llamada `dist/` en ese mismo directorio con los archivos compilados.

### Caso B: Estructura de Subproyecto o *Workspace* (Tu Caso)

Si tienes un repositorio principal de pruebas (ej. `TFM-UNIR`) y dentro tienes la carpeta de tu paquete (ej. `evmaudit`), `uv` por defecto compilará los archivos en la raíz del repositorio principal (`TFM-UNIR/dist/`).

Para gestionar esto, tienes dos opciones válidas:

1. **Compilar desde la raíz del subproyecto especificando el paquete:**
```bash
cd evmaudit/
uv build --package evmaudit

```


2. **Compilar de forma global (Estrategia directa):**
Ejecutar `uv build` desde la raíz del repositorio principal. Generará el `dist/` global con el contenido de tu paquete interno según las referencias de tu entorno de trabajo.

---

## 3. Publicación en PyPI

Una vez que los archivos están dentro de la carpeta `dist/`, es hora de subirlos.

### Paso Directo (Desde el directorio donde está la carpeta `dist/`)

1. Sitúate en el directorio que contiene la carpeta `dist/` generada:
```bash
cd /ruta/hacia/el/directorio-con-dist/

```


2. Ejecuta el comando de publicación:
```bash
uv publish

```


3. Introduce las credenciales cuando te lo solicite:
* **Username:** `__token__` (Escribe literalmente esta palabra, con los dos guiones bajos antes y después).
* **Password:** Pega tu token de PyPI (`pypi-...`).



### Flujo de Trabajo Alternativo (Automatizando las credenciales)

Para evitar escribir el token manualmente en cada publicación, puedes exportarlo temporalmente en las variables de entorno de tu terminal:

```bash
export UV_PUBLISH_TOKEN="pypi-tu-token-aqui"
uv publish

```

---

## 4. Verificación e Instalación

Si el proceso ha finalizado con éxito, verás una confirmación en la terminal indicando el hashing y la subida de los archivos. Tu paquete ya está disponible públicamente en el ecosistema de Python.

Cualquier usuario puede instalarlo ejecutando:

```bash
pip install evmaudit

```

O si utilizan el ecosistema de `uv`:

```bash
uv pip install evmaudit

```

---

## 🔄 Ciclo de Actualización del Paquete

Cuando modifiques el código y quieras liberar una nueva versión (ej. solucionar un bug o añadir una funcionalidad):

1. Abre el `pyproject.toml` de tu paquete e incrementa el campo `version` (ej. de `"0.1.0"` a `"0.1.1"`).
2. Borra los archivos viejos de la carpeta `dist/` para evitar subir duplicados.
3. Vuelve a ejecutar el ciclo:

```bash
uv build
uv publish
```
