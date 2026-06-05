## 📋 Requisitos Previos

1. **Tener `uv` instalado**: Si no lo tienes, puedes instalarlo en macOS/Linux con:




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
---

## 4. Distribución y Publicación en el Registro de Paquetes PyPI

El ciclo de desarrollo de la librería propuesta culmina con su fase de distribución, permitiendo que las herramientas de análisis de seguridad implementadas sean accesibles e integrables por la comunidad de desarrollo y auditoría de *smart contracts*. Para asegurar una distribución estandarizada y eficiente dentro del ecosistema Python, se ha seleccionado el índice oficial de paquetes PyPI (*Python Package Index*). La gestión de este proceso se unifica bajo la herramienta `uv`, garantizando la consistencia desde la compilación de los artefactos hasta su publicación definitiva.

### 4.1. Configuración de Metadatos del Proyecto (`pyproject.toml`)

El paso previo indispensable para la distribución consiste en la definición inequívoca de los metadatos y la especificación del sistema de construcción (*build system*) en el archivo de configuración `pyproject.toml`, ubicado en la raíz del paquete. Este procedimiento se rige bajo los estándares modernos de empaquetado de Python (PEP 517 y PEP 621).

Para este proyecto, se ha adoptado `hatchling` como *build backend*, debido a su ligereza, velocidad y compatibilidad nativa con las especificaciones del ecosistema actual. A continuación, se presenta la estructura de configuración requerida para delimitar las propiedades de la librería `evmaudit`:

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

Los clasificadores (*classifiers*) incluidos permiten categorizar la librería dentro del índice público, facilitando su indexación en función de la licencia de código abierto seleccionada, la compatibilidad del sistema operativo y las versiones soportadas del intérprete Python.

### 4.2. Proceso de Compilación del Paquete

Una vez validados los metadatos, se procede a la generación de los archivos de distribución. Este proceso transforma el código fuente estructurado en el directorio `src/` en artefactos instalables e independientes del entorno de desarrollo.

La ejecución del comando unificado de compilación abstrae la complejidad de las herramientas tradicionales:

```bash
uv build

```

Este comando genera de forma nativa dos tipos de distribuciones estándar dentro del directorio `dist/`:

* **Distribución de código fuente (*sdist* o `.tar.gz`):** Un archivo comprimido que contiene el código fuente original y los archivos de configuración, actuando como respaldo para plataformas o configuraciones no previstas.
* **Distribución binaria compilada (*wheel* o `.whl`):** El formato de empaquetado moderno que permite una instalación directa y optimizada en el sistema destino, evitando la necesidad de compilar el código en la máquina del usuario final.

En contextos de desarrollo complejos donde el paquete forma parte de un repositorio principal o arquitectura de *workspace* (como el entorno de trabajo `TFM-UNIR`), `uv` permite gestionar la compilación de manera localizada. Para forzar la construcción exclusiva del subproyecto desde su propio directorio y evitar colisiones en la raíz global, se aplica la opción de empaquetado específico:

```bash
uv build --package evmaudit

```

### 4.3. Seguridad y Autenticación en la Publicación

La publicación de código en repositorios públicos exige mecanismos estrictos de control de acceso para prevenir vectores de ataque basados en la cadena de suministro (*supply chain attacks*). Por razones de seguridad, se desestima el uso de contraseñas de usuario tradicionales en favor de la autenticación basada en **Tokens de API**.

El proceso de despliegue requiere la obtención de un *token* con prefijo `pypi-` generado desde el panel de control de PyPI. En la primera interacción, el alcance del *token* se configura de manera global; no obstante, una vez realizada la primera subida con éxito, la buena práctica metodológica dicta restringir los permisos del token de manera exclusiva al ámbito del paquete `evmaudit`, minimizando así la superficie de exposición en caso de compromiso de la credencial.

### 4.4. Ejecución del Despliegue

Con los artefactos ubicados en el directorio `dist/` y las credenciales expedidas, se procede a la transferencia segura hacia los servidores de PyPI. El comando `uv publish` automatiza la verificación de integridad mediante *hashes* criptográficos y realiza la subida en un único paso:

```bash
uv publish

```

Durante el flujo interactivo en la línea de comandos, el sistema requiere la introducción del identificador genérico `__token__` en el campo de usuario, seguido de la clave alfanumérica del token de API en el campo de contraseña. Con el objetivo de optimizar este flujo en entornos de Integración Continua (CI/CD) o evitar la inserción manual recurrente, es posible exportar temporalmente la credencial en el entorno de la terminal actual:

```bash
export UV_PUBLISH_TOKEN="pypi-tu-token-aqui"
uv publish

```

Tras la finalización exitosa del proceso, el paquete queda registrado globalmente, permitiendo su incorporación inmediata en otros proyectos mediante los gestores tradicionales del ecosistema:

```bash
pip install evmaudit

```

O bien, aprovechando los beneficios de rendimiento de la herramienta unificada del proyecto:

```bash
uv pip install evmaudit

```

### 4.5. Ciclo de Mantenimiento y Actualización de Versiones

La evolución de la librería para la corrección de vulnerabilidades o la integración de nuevas capacidades de análisis requiere una política estricta de control de versiones. El flujo metodológico establecido para la liberación de actualizaciones iterativas consta de tres fases secuenciales:

1. **Incremento del número de versión:** Modificación manual del campo `version` en el archivo `pyproject.toml` siguiendo el estándar de Versionado Semántico (ej. de `0.1.0` a `0.1.1`).
2. **Saneamiento del directorio de distribución:** Eliminación de los artefactos obsoletos del directorio `dist/` para mitigar el riesgo de duplicidad o subidas erróneas de versiones previas.
3. **Reconstrucción y despliegue:** Ejecución consecutiva de los procesos de empaquetado y transferencia:

```bash
uv build
uv publish

```

Esta sistemática asegura que cada iteración de la herramienta de auditoría de la EVM mantenga la trazabilidad, la coherencia histórica y la disponibilidad pública necesarias para un entorno de producción académica y profesional.


