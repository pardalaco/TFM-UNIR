## Entorno virtual Python

### ¿Por qué usar entornos virtuales?

El desarrollo de una librería Python destinada a integrar múltiples herramientas de análisis de seguridad plantea, desde el inicio, un problema de gestión de dependencias que no debe subestimarse. Las herramientas que se integran en la solución propuesta, como Slither, Mythril o Echidna, tienen requisitos de versión específicos y en ocasiones incompatibles entre sí cuando se instalan en el entorno global del sistema. Esta situación, conocida en el ecosistema Python como *dependency hell*, puede provocar conflictos silenciosos difíciles de depurar y comprometer la reproducibilidad del entorno de desarrollo.

Un entorno virtual (*virtual environment*) es un directorio aislado que contiene una instalación independiente del intérprete Python junto con sus propios paquetes y dependencias, sin interferir con el sistema global ni con otros proyectos. Esta separación proporciona varias ventajas fundamentales en el contexto del presente trabajo:

En primer lugar, garantiza el **aislamiento de dependencias**, de forma que cada proyecto mantiene sus propias versiones de bibliotecas sin afectar al resto del sistema. Esto resulta especialmente relevante cuando diferentes herramientas de análisis requieren versiones distintas de una misma dependencia transitiva.

En segundo lugar, favorece la **reproducibilidad** del entorno de desarrollo. Todos los integrantes del equipo pueden trabajar exactamente con las mismas versiones de todas las dependencias, eliminando la variabilidad asociada a instalaciones manuales y garantizando que los resultados obtenidos durante el desarrollo son consistentes independientemente del sistema operativo o configuración personal de cada desarrollador.

En tercer lugar, facilita el **ciclo de vida del proyecto** al delimitar claramente qué paquetes pertenecen al proyecto y cuáles son del sistema, simplificando tanto la distribución de la librería como su posterior publicación en registros públicos como PyPI.

### Tipos de entornos virtuales

En el ecosistema Python existen varias alternativas para la gestión de entornos virtuales, con distintos niveles de abstracción y funcionalidad.

El módulo estándar `venv`, incluido en la biblioteca estándar desde Python 3.3, permite crear entornos virtuales básicos mediante el comando `python -m venv .venv`. Sin embargo, este enfoque no incluye gestión de dependencias ni ficheros de bloqueo (*lockfiles*), por lo que debe complementarse con herramientas adicionales como `pip` y `pip-tools`.

`virtualenv` es una alternativa anterior al módulo estándar, con mayor compatibilidad con versiones antiguas de Python y algunas funcionalidades adicionales, aunque en la práctica ha quedado desplazada por las herramientas modernas.

`conda` ofrece un modelo más completo que combina gestión de entornos con gestión de paquetes, incluyendo dependencias no Python. Es habitual en entornos científicos y de análisis de datos, pero introduce una complejidad y un tamaño innecesarios para un proyecto centrado en el ecosistema Python puro.

Herramientas como `poetry` o `pipenv` representan un nivel superior de abstracción, combinando la gestión de entornos virtuales con la resolución de dependencias, la generación de ficheros de bloqueo y el ciclo de publicación de paquetes. Su adopción en proyectos profesionales se ha generalizado en los últimos años.

Finalmente, `uv` constituye la herramienta de última generación en este espacio, combinando todas las funcionalidades anteriores en una solución de rendimiento muy superior, como se detalla en la sección siguiente.

### Herramienta a usar: uv

#### ¿Qué es uv?

`uv` es un gestor de paquetes y proyectos Python de alto rendimiento desarrollado por Astral, la empresa creadora del formateador Ruff. Implementado en Rust, se presenta como una herramienta unificada capaz de sustituir a `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine` y `virtualenv` mediante una interfaz de línea de comandos coherente. Su desarrollo se orienta tanto a la velocidad de ejecución como a la corrección en la resolución de dependencias y a la facilidad de adopción en proyectos de diferente escala y complejidad.

#### Ventajas de uv

La principal ventaja diferencial de `uv` respecto a las alternativas existentes es su rendimiento. Según los propios *benchmarks* publicados en su documentación oficial, `uv` es entre 10 y 100 veces más rápido que `pip` en operaciones de instalación de paquetes con caché caliente. Esta diferencia resulta perceptible en la práctica, especialmente durante las fases de incorporación de nuevos integrantes al equipo o en entornos de integración continua donde el entorno debe reconstruirse frecuentemente.

Más allá del rendimiento, `uv` ofrece un conjunto de ventajas relevantes para el desarrollo de la librería propuesta en este trabajo. Gestiona automáticamente los entornos virtuales asociados a cada proyecto, sin necesidad de crearlos ni activarlos manualmente. Genera y mantiene un fichero de bloqueo universal (`uv.lock`) que garantiza instalaciones reproducibles en cualquier plataforma. Permite gestionar múltiples versiones del intérprete Python e instalar la versión adecuada de forma automática si no está disponible en el sistema. Además, su diseño es compatible con los estándares del ecosistema Python (`pyproject.toml`, PEP 517, PEP 621), lo que facilita la integración con otras herramientas y la publicación en registros de paquetes.

#### Qué proporciona uv en el contexto de este proyecto

Para el desarrollo de la librería propuesta, `uv` proporciona un conjunto de funcionalidades que cubren todo el ciclo de vida del proyecto, desde la inicialización hasta la publicación.

**Gestión de dependencias y sincronización del entorno.** Una vez definidas las dependencias del proyecto en el fichero `pyproject.toml`, cualquier integrante del equipo puede reproducir exactamente el mismo entorno ejecutando un único comando:

```bash
uv sync
```

Este comando resuelve las dependencias declaradas, instala las versiones exactas registradas en el fichero de bloqueo `uv.lock` y configura el entorno virtual del proyecto de forma automática. La simplicidad de este flujo elimina los problemas habituales de divergencia entre entornos de desarrollo individuales, garantizando que todos los miembros del equipo trabajan con las mismas versiones de Slither, Mythril, Echidna y el resto de dependencias de la librería.

**Inicialización de proyectos.** `uv` proporciona soporte integrado para la creación de nuevos proyectos mediante el comando `uv init`. Para el caso específico de una librería Python destinada a ser importada por otros proyectos o publicada en PyPI, se utiliza la opción `--lib`:

```bash
uv init --lib evm-security-analyzer
```

Este comando genera automáticamente la estructura de directorios recomendada para una librería Python, incluyendo el fichero `pyproject.toml` con los metadatos del proyecto, el directorio `src/` con el paquete principal y los ficheros de configuración necesarios para la construcción y distribución. El uso de la disposición `src/` (*src layout*) es la práctica recomendada actualmente para proyectos publicables, ya que evita problemas habituales relacionados con la importación del paquete desde el directorio raíz durante el desarrollo.

**Construcción de distribuciones.** `uv` integra soporte nativo para la generación de distribuciones instalables mediante el comando `uv build`, que produce tanto el archivo fuente (*sdist*) como la rueda binaria (*wheel*) del paquete:

```bash
uv build
```

El resultado son los artefactos estándar de distribución Python ubicados en el directorio `dist/`, listos para ser publicados o distribuidos directamente.

**Publicación de paquetes.** El ciclo se completa con el soporte para publicación en registros de paquetes, incluyendo PyPI, mediante el comando `uv publish`:

```bash
uv publish
```

Este comando gestiona la autenticación y la subida de los artefactos generados, cubriendo el flujo completo que anteriormente requería herramientas adicionales como `twine`.

En conjunto, `uv` unifica en una sola herramienta todo el ciclo de vida del proyecto: inicialización, gestión de dependencias, sincronización del entorno, construcción de distribuciones y publicación. Esta integración reduce la fricción en el desarrollo colaborativo y facilita la adopción de prácticas profesionales de gestión de proyectos Python desde las primeras fases del trabajo.

