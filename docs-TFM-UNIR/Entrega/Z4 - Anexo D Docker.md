# Anexo D Docker

## ANEXO D.1.	CONTENEDORIZACIÓN E INFRAESTRUCTURA DE DESPLIEGUE (DOCKER)

En el ámbito del desarrollo de software moderno y la ciberseguridad, la reproducibilidad del entorno de ejecución constituye un pilar crítico. Tradicionalmente, el despliegue de aplicaciones que integran múltiples herramientas de análisis (como compiladores de Solidity y motores de ejecución simbólica) se enfrentaba al problema de "funciona en mi máquina", derivado de las discrepancias en las versiones de las dependencias, librerías del sistema operativo y configuraciones locales. Para mitigar este riesgo, el presente proyecto adopta una arquitectura basada en contenedores de aplicación a través del ecosistema de **Docker** y **Docker Compose**.

## ANEXO D.2.	Fundamentos de Contenedorización: Docker y Docker Compose

Docker es una plataforma de código abierto basada en la tecnología de contenedorización, la cual permite empaquetar una aplicación y todas sus dependencias (binarios, librerías, archivos de configuración) en una unidad estandarizada denominada **contenedor**. A diferencia de la virtualización tradicional, Docker opera mediante la virtualización a nivel de sistema operativo, compartiendo el núcleo (kernel) del sistema anfitrión pero ejecutando los procesos en espacios de usuario completamente aislados a través de namespaces y cgroups. Desde la perspectiva de la seguridad, este aislamiento garantiza que los procesos del pipeline de auditoría de EVMAudit se ejecuten de forma confinada, mitigando el impacto en la infraestructura anfitriona ante la eventual ejecución de código arbitrario o inesperado durante el análisis de contratos inteligentes.

Por su parte, **Docker Compose** es la herramienta diseñada para definir y orquestar aplicaciones Docker multi-contenedor. Mediante el uso de un archivo de configuración declarativo en formato YAML (docker-compose.yml), permite definir con precisión los servicios que componen el sistema, sus dependencias de arranque, la exposición de puertos hacia el exterior, la creación de redes aisladas y la asignación de volúmenes persistentes. En el contexto de EVMAudit, actúa como el motor de despliegue unificado, permitiendo al administrador inicializar toda la infraestructura del TFM (servidor FastAPI, interfaz web y almacenamiento de informes) de manera centralizada.

## ANEXO D.3.	Estrategia de Construcción de la Imagen (Dockerfile)
La construcción de la imagen se define en un único Dockerfile optimizado. Debido a que el pipeline de análisis requiere interactuar con el sistema operativo para invocar compiladores y binarios de seguridad, se ha seleccionado **Ubuntu 22.04** como imagen base, proporcionando un entorno estable y con soporte extendido para dependencias nativas de Linux en arquitectura amd64.

El proceso de aprovisionamiento de la imagen se divide en las siguientes fases críticas:
1. **Entorno y Variables de Sistema**: Se configuran las variables de entorno `PYTHONDONTWRITEBYTECODE=1` y `PYTHONUNBUFFERED=1` para optimizar la ejecución de Python dentro del contenedor, evitando la escritura de residuos binarios y forzando el volcado de logs en tiempo real. Asimismo, se establece `DEBIAN_FRONTEND=noninteractive` para suprimir diálogos interactivos durante la instalación de paquetes.
2. **Aprovisionamiento de Compiladores (Solidity):** Se añade el repositorio PPA oficial de Ethereum (ppa:ethereum/ethereum) para incorporar el compilador nativo de Solidity (solc). Posteriormente, se instala la utilidad `solc-select` mediante el gestor de paquetes de Python para automatizar la descarga y conmutación de versiones.
3. **Integración del Fuzzer Echidna:** Dado que Echidna se distribuye de manera óptima como un binario estático para Linux, el contenedor automatiza su descarga directa (versión v2.3.2) desde los repositorios oficiales de *Crytic*, procediendo a su extracción e instalación en `/usr/local/bin/` para garantizar su disponibilidad inmediata en el PATH del sistema.
4. **Optimización de Dependencias con `uv` (Multi-stage Build):** Con el objetivo de minimizar los tiempos de construcción y asegurar una gestión eficiente de los paquetes de Python, se emplea un mecanismo de construcción en etapas múltiples (Multi-stage build), importando los binarios optimizados del gestor uv directamente desde su imagen oficial en el registro de GitHub (ghcr.io/astral-sh/uv:latest).
5. **Instalación del Paquete Local:** Tras establecer el directorio de trabajo en /app y copiar el código fuente , se ejecuta el comando `uv sync --frozen --no-cache`. Esto resuelve de forma determinista el grafo de dependencias del archivo uv.lock, registrando el paquete local editable evmaudit e instalando el servidor ASGI Uvicorn sin almacenar datos residuales en la caché de la imagen.

## ANEXO D.4.	Orquestación de Servicios (Docker Compose)

La coordinación del contenedor web y sus dependencias con el sistema anfitrión se gestiona de forma declarativa mediante un archivo docker-compose.yml. La especificación del servicio, denominado evmaudit-web, se fundamenta en tres pilares de ingeniería:

- **Persistencia de Datos mediante Volúmenes**: Con el fin de dotar al sistema de un estado persistente (pese a la naturaleza efímera de los contenedores), se realiza un mapeo directo de directorios del host hacia el contenedor:
- **`./jsons/_uploads:/app/jsons/_uploads`**: Almacena de forma persistente los contratos Solidity cargados por los usuarios, los wrappers intermedios generados para Echidna y los informes de auditoría finales en formato JSON y Markdown.
- **`./contracts:/app/contracts`**: Habilita un volumen opcional para la auditoría directa de Smart Contracts locales sin necesidad de interactuar con la interfaz web.
- **Aislamiento de Red y Mapeo de Puertos**: Se expone el puerto 8080 del contenedor hacia el puerto 8080 del sistema anfitrión. Esto permite redirigir el tráfico HTTP de la interfaz construida en HTML5/Vanilla JS hacia el backend desarrollado en FastAPI de forma transparente.
- **Tolerancia a Fallos**: Se implementa la política de reinicio restart: unless-stopped. Esta directiva asegura la alta disponibilidad del servicio ante excepciones imprevistas en el motor de ejecución simbólica (Mythril) o caídas del propio demonio de Docker, garantizando que el servicio web vuelva a levantarse de manera automática salvo interrupción explícita del administrador.

## ANEXO D.5.	Flujo de Despliegue y Ciclo de Vida del Contenedor
Para la puesta en marcha de la infraestructura local en entornos de desarrollo o evaluación, el ciclo de vida del contenedor se administra mediante el estándar de comandos de Docker Compose:
1. **Fase de Construcción (Build):** Compilación de la imagen e instalación del entorno virtual determinista:
```bash
docker compose build
```

2. **Fase de Inicialización (Up):** Despliegue e instanciación del servicio en segundo plano (detached mode):
```bash
docker compose up -d
```

3.	**Fase de Auditoría de Ejecución (Logs):** Inspección de la salida estándar del contenedor para la monitorización de los análisis en curso:

```bash
docker compose logs -f evmaudit-web
```

4.	**Fase de Parada (Down):** Interrupción y eliminación de los contenedores activos salvaguardando la integridad de los datos de las auditorías gracias a los volúmenes enlazados:
docker compose down

