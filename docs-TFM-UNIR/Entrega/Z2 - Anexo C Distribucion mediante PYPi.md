# ANEXO C.	DISTRIBUCIÓN Y PUBLICACIÓN EN EL REGISTRO DE PAQUETES PYPI
El ciclo de desarrollo de la librería propuesta culmina con su fase de distribución, permitiendo que las herramientas de análisis de seguridad implementadas sean accesibles e integrables por la comunidad de desarrollo y auditoría de smart contracts. Para asegurar una distribución estandarizada y eficiente dentro del ecosistema Python, se ha seleccionado el índice oficial de paquetes PyPI (Python Package Index). La gestión de este proceso se unifica bajo la herramienta uv, garantizando la consistencia desde la compilación de los artefactos hasta su publicación definitiva.
5.2.4. Configuración de Metadatos del Proyecto (pyproject.toml)
El paso previo indispensable para la distribución consiste en la definición inequívoca de los metadatos y la especificación del sistema de construcción (build system) en el archivo de configuración pyproject.toml, ubicado en la raíz del paquete. Este procedimiento se rige bajo los estándares modernos de empaquetado de Python (PEP 517 y PEP 621).
Para este proyecto, se ha adoptado hatchling como build backend, debido a su ligereza, velocidad y compatibilidad nativa con las especificaciones del ecosistema actual. A continuación, se presenta la estructura de configuración requerida para delimitar las propiedades de la librería evmaudit:
[project]
name = "evmaudit"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Daniel Rovira Martínez", email = "pardalaco@gmail.com" },
    { name = "Paula Suárez Prieto", email = "Paula Suárez Prieto" },
    { name = "Adrián Moreno Martín", email = "adrimore2@gmail.com" }
]
requires-python = ">=3.12"
dependencies = [
    "eth>=0.0.1",
    "mythril>=0.24.8",
    "setuptools<70.0.0",
    "slither-analyzer>=0.9.2",
    "solc-select>=1.2.0",]

[project.scripts]
evmaudit = "evmaudit.main:main"

[build-system]
requires = ["uv_build>=0.11.15,<0.12.0"]
build-backend = "uv_build"
Los clasificadores (classifiers) incluidos permiten categorizar la librería dentro del índice público, facilitando su indexación en función de la licencia de código abierto seleccionada, la compatibilidad del sistema operativo y las versiones soportadas del intérprete Python.
5.2.5. Proceso de Compilación del Paquete
Una vez validados los metadatos, se procede a la generación de los archivos de distribución. Este proceso transforma el código fuente estructurado en el directorio src/ en artefactos instalables e independientes del entorno de desarrollo.
La ejecución del comando unificado de compilación abstrae la complejidad de las herramientas tradicionales:
uv build
Este comando genera de forma nativa dos tipos de distribuciones estándar dentro del directorio dist/:
•	Distribución de código fuente (sdist o .tar.gz): Un archivo comprimido que contiene el código fuente original y los archivos de configuración, actuando como respaldo para plataformas o configuraciones no previstas.
•	Distribución binaria compilada (wheel o .whl): El formato de empaquetado moderno que permite una instalación directa y optimizada en el sistema destino, evitando la necesidad de compilar el código en la máquina del usuario final.
En contextos de desarrollo complejos donde el paquete forma parte de un repositorio principal o arquitectura de workspace (como el entorno de trabajo TFM-UNIR), uv permite gestionar la compilación de manera localizada. Para forzar la construcción exclusiva del subproyecto desde su propio directorio y evitar colisiones en la raíz global, se aplica la opción de empaquetado específico:
uv build --package evmaudit
5.2.6. Seguridad y Autenticación en la Publicación
La publicación de código en repositorios públicos exige mecanismos estrictos de control de acceso para prevenir vectores de ataque basados en la cadena de suministro (supply chain attacks). Por razones de seguridad, se desestima el uso de contraseñas de usuario tradicionales en favor de la autenticación basada en Tokens de API.
El proceso de despliegue requiere la obtención de un token con prefijo pypi- generado desde el panel de control de PyPI. En la primera interacción, el alcance del token se configura de manera global; no obstante, una vez realizada la primera subida con éxito, la buena práctica metodológica dicta restringir los permisos del token de manera exclusiva al ámbito del paquete evmaudit, minimizando así la superficie de exposición en caso de compromiso de la credencial. 
5.2.7. Ejecución del Despliegue
Con los artefactos ubicados en el directorio dist/ y las credenciales expedidas, se procede a la transferencia segura hacia los servidores de PyPI. El comando uv publish automatiza la verificación de integridad mediante hashes criptográficos y realiza la subida en un único paso:
uv publish
Durante el flujo interactivo en la línea de comandos, el sistema requiere la introducción del identificador genérico __token__ en el campo de usuario, seguido de la clave alfanumérica del token de API en el campo de contraseña. Con el objetivo de optimizar este flujo en entornos de Integración Continua (CI/CD) o evitar la inserción manual recurrente, es posible exportar temporalmente la credencial en el entorno de la terminal actual:
export UV_PUBLISH_TOKEN="pypi-tu-token-aqui"
uv publish
Tras la finalización exitosa del proceso, el paquete queda registrado globalmente, permitiendo su incorporación inmediata en otros proyectos mediante los gestores tradicionales del ecosistema:
pip install evmaudit
O bien, aprovechando los beneficios de rendimiento de la herramienta unificada del proyecto:
uv add evmaudit
5.2.8. Ciclo de Mantenimiento y Actualización de Versiones
La evolución de la librería para la corrección de vulnerabilidades o la integración de nuevas capacidades de análisis requiere una política estricta de control de versiones. El flujo metodológico establecido para la liberación de actualizaciones iterativas consta de tres fases secuenciales:
•	Incremento del número de versión: Modificación manual del campo version en el archivo pyproject.toml siguiendo el estándar de Versionado Semántico (ej. de 0.1.0 a 0.1.1).
•	Saneamiento del directorio de distribución: Eliminación de los artefactos obsoletos del directorio dist/ para mitigar el riesgo de duplicidad o subidas erróneas de versiones previas.
•	Reconstrucción y despliegue: Ejecución consecutiva de los procesos de empaquetado y transferencia:
uv build
uv publish
Esta sistemática asegura que cada iteración de la herramienta de auditoría de la EVM mantenga la trazabilidad, la coherencia histórica y la disponibilidad pública necesarias para un entorno de producción académica y profesional.

 
