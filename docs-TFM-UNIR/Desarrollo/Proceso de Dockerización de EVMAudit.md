# Proceso de Dockerización de EVMAudit

Este documento describe detalladamente la estrategia y los pasos seguidos para contenedorizar la aplicación web de **EVMAudit**, permitiendo empaquetar el backend de FastAPI junto con todo el conjunto de herramientas de seguridad de Smart Contracts (`solc`, `Slither`, `Mythril` y `Echidna`) en un entorno reproducible y aislado.

## 1. Diseño del Dockerfile (Estrategia de Construcción)

Para dar soporte a todas las herramientas que utiliza el pipeline, se ha configurado un único `Dockerfile` estructurado en las siguientes fases:

* **Imagen Base:** Se utiliza `ubuntu:22.04` para garantizar la máxima compatibilidad con las dependencias binarias y los repositorios nativos de Ethereum.
* **Instalación de Dependencias del Sistema y Solc:**
* Se instalan paquetes esenciales como `curl`, `git`, `build-essential`, `python3-pip` y `python3-dev`.
* Se añade el PPA oficial de Ethereum (`ppa:ethereum/ethereum`) para instalar el compilador nativo de Solidity (`solc`).


* **Gestión de Versiones de Solidity con solc-select:** Se instala `solc-select` mediante `pip` para configurar y fijar de forma global la versión `0.8.20`, requerida por el pipeline de Slither.
* **Instalación Manual de Echidna:** Se descarga de forma directa el binario estático de Echidna (versión `v2.3.2`) desde su repositorio oficial, se descomprime y se mueve a `/usr/local/bin/` para que esté disponible en el `PATH` global del contenedor.
* **Optimización con 'uv' (Multi-stage Build):** Se aprovecha la imagen oficial de `astral-sh/uv` copiando sus binarios de manera directa (`COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`). Esto acelera drásticamente la sincronización e instalación de las dependencias de Python de forma aislada.
* **Despliegue del Código:** Se establece el directorio de trabajo en `/app`, se copia el código fuente del proyecto y se ejecuta `uv sync --frozen --no-cache` para congelar e instalar el paquete local `evmaudit` y el resto de librerías en un entorno virtual optimizado.

---

## 2. Orquestación con Docker Compose

Para simplificar el despliegue local y evitar comandos extensos de Docker, se ha creado el archivo `docker-compose.yml`. Su configuración asegura:

* **Persistencia de Datos (Volúmenes):** * `./jsons/_uploads:/app/jsons/_uploads`: Monta localmente el directorio donde se almacenan el código subido por los usuarios y los informes JSON finales generados por el pipeline, evitando la pérdida de información al reiniciar el contenedor.
* `./contracts:/app/contracts`: Permite mapear de forma opcional un directorio de contratos locales para realizar pruebas.


* **Mapeo de Puertos:** Redirecciona el puerto `8080:8080` de la máquina anfitriona hacia la API de FastAPI dentro del contenedor.
* **Políticas de Reintento:** Configurado con `restart: unless-stopped` para que el servicio web se levante de forma automática en entornos de producción o servidores locales salvo que sea detenido explícitamente.

---

## 3. Guía de Uso y Comandos de Despliegue

Sigue estos pasos en la terminal desde la raíz de tu proyecto para construir y arrancar la aplicación doquerizada:

### Paso 1: Construir la imagen de Docker

Este comando leerá las instrucciones del `Dockerfile`, descargará las dependencias de Ubuntu, compilará los binarios y preparará el entorno de Python mediante `uv`.

```bash
docker compose build

```

### Paso 2: Levantar el contenedor en segundo plano (Detached mode)

Arranca el servicio web y expone el frontend en el puerto configurado.

```bash
docker compose up -d

```

### Paso 3: Verificar el estado del servicio

Puedes comprobar que el contenedor `evmaudit_webapp` se encuentra corriendo de forma correcta con el siguiente comando:

```bash
docker compose ps

```

### Paso 4: Consultar los logs en tiempo real (Opcional)

Muy útil para auditar el progreso real de las herramientas (como los 1-2 minutos que toma la ejecución simbólica de Mythril):

```bash
docker compose logs -f evmaudit-web

```

### Paso 5: Detener la aplicación

Para apagar los servicios manteniendo intactos tus archivos guardados en los volúmenes locales (`jsons/_uploads`):

```bash
docker compose down

```

---

## 4. Acceso a la Aplicación

Una vez que el contenedor esté en ejecución gracias a Docker Compose, la interfaz VirusTotal-like de EVMAudit estará totalmente disponible en el navegador web local a través de la dirección:

👉 **http://localhost:8080**



---

## X. Contenedorización e Infraestructura de Despliegue

Para garantizar la portabilidad, el aislamiento y la perfecta reproducibilidad del entorno de ejecución de EVMAudit, se ha optado por una estrategia de contenedorización basada en **Docker** y **Docker Compose**. La arquitectura de la aplicación web presenta una alta complejidad debido a la necesidad de orquestar herramientas de análisis que dependen de distintos entornos de ejecución, binarios estáticos y gestores de paquetes. A continuación, se detalla el diseño técnico de la infraestructura de despliegue.

### X.1. Estrategia de Construcción de la Imagen (Dockerfile)

La construcción de la imagen se define en un único `Dockerfile` optimizado. Debido a que el *pipeline* de análisis requiere interactuar con el sistema operativo para invocar compiladores y binarios de seguridad, se ha seleccionado **Ubuntu 22.04** como imagen base, proporcionando un entorno estable y con soporte extendido para dependencias nativas de Linux en arquitectura `amd64`.

El proceso de aprovisionamiento de la imagen se divide en las siguientes fases críticas:

1. 
**Entorno y Variables de Sistema:** Se configuran las variables de entorno `PYTHONDONTWRITEBYTECODE=1` y `PYTHONUNBUFFERED=1` para optimizar la ejecución de Python dentro del contenedor, evitando la escritura de residuos binarios y forzando el volcado de *logs* en tiempo real. Asimismo, se establece `DEBIAN_FRONTEND=noninteractive` para suprimir diálogos interactivos durante la instalación de paquetes.


2. 
**Aprovisionamiento de Compiladores (Solidity):** Se añade el repositorio PPA oficial de Ethereum (`ppa:ethereum/ethereum`) para incorporar el compilador nativo de Solidity (`solc`). Posteriormente, se instala la utilidad `solc-select` mediante el gestor de paquetes de Python para automatizar la descarga y conmutación de versiones, fijando globalmente la versión `0.8.20`, que es el estándar requerido para la correcta ejecución del analizador estático Slither.


3. 
**Integración del Fuzzer Echidna:** Dado que Echidna se distribuye de manera óptima como un binario estático para Linux, el contenedor automatiza su descarga directa (versión `v2.3.2`) desde los repositorios oficiales de *Crytic*, procediendo a su extracción e instalación en `/usr/local/bin/` para garantizar su disponibilidad inmediata en el `PATH` del sistema.


4. 
**Optimización de Dependencias con 'uv' (Multi-stage Build):** Con el objetivo de minimizar los tiempos de construcción y asegurar una gestión eficiente de los paquetes de Python, se emplea un mecanismo de construcción en etapas múltiples (*Multi-stage build*), importando los binarios optimizados del gestor `uv` directamente desde su imagen oficial en el registro de GitHub (`ghcr.io/astral-sh/uv:latest`).


5. 
**Instalación del Paquete Local:** Tras establecer el directorio de trabajo en `/app` y copiar el código fuente , se ejecuta el comando `uv sync --frozen --no-cache`. Esto resuelve de forma determinista el grafo de dependencias del archivo `uv.lock`, registrando el paquete local editable `evmaudit` e instalando el servidor ASGI `Uvicorn` sin almacenar datos residuales en la caché de la imagen.



### X.2. Orquestación de Servicios (Docker Compose)

La coordinación del contenedor web y sus dependencias con el sistema anfitrión se gestiona de forma declarativa mediante un archivo `docker-compose.yml`. La especificación del servicio, denominado `evmaudit-web`, se fundamenta en tres pilares de ingeniería:

* **Persistencia de Datos mediante Volúmenes:** Con el fin de dotar al sistema de un estado persistente (pese a la naturaleza efímera de los contenedores), se realiza un mapeo directo de directorios del *host* hacia el contenedor:
* 
`./jsons/_uploads:/app/jsons/_uploads`: Almacena de forma persistente los contratos Solidity cargados por los usuarios, los *wrappers* intermedios generados para Echidna y los informes de auditoría finales en formato JSON y Markdown.


* 
`./contracts:/app/contracts`: Habilita un volumen opcional para la auditoría directa de Smart Contracts locales sin necesidad de interactuar con la interfaz web.




* 
**Aislamiento de Red y Mapeo de Puertos:** Se expone el puerto `8080` del contenedor hacia el puerto `8080` del sistema anfitrión. Esto permite redirigir el tráfico HTTP de la interfaz construida en HTML5/Vanilla JS hacia el *backend* desarrollado en FastAPI de forma transparente.


* 
**Tolerancia a Fallos:** Se implementa la política de reinicio `restart: unless-stopped`. Esta directiva asegura la alta disponibilidad del servicio ante excepciones imprevistas en el motor de ejecución simbólica (Mythril) o caídas del propio demonio de Docker, garantizando que el servicio web vuelva a levantarse de manera automática salvo interrupción explícita del administrador.



---

### X.3. Flujo de Despliegue y Ciclo de Vida del Contenedor

Para la puesta en marcha de la infraestructura local en entornos de desarrollo o evaluación, el ciclo de vida del contenedor se administra mediante el estándar de comandos de Docker Compose:

1. **Fase de Construcción (Build):** Compilación de la imagen e instalación del entorno virtual determinista:
```bash
docker compose build

```


2. **Fase de Inicialización (Up):** Despliegue e instanciación del servicio en segundo plano (*detached mode*):
```bash
docker compose up -d

```


3. **Fase de Auditoría de Ejecución (Logs):** Inspección de la salida estándar del contenedor para la monitorización de los análisis en curso:
```bash
docker compose logs -f evmaudit-web

```


4. **Fase de Parada (Down):** Interrupción y eliminación de los contenedores activos salvaguardando la integridad de los datos de las auditorías gracias a los volúmenes enlazados:
```bash
docker compose down

```