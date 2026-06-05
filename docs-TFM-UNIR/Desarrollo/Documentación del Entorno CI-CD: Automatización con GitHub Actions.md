
# Documentación del Entorno CI/CD: Automatización con GitHub Actions

Este documento describe la arquitectura, configuración y funcionamiento del pipeline de Integración Continua (CI) implementado para **EVMAudit** utilizando **GitHub Actions** y **GitHub Container Registry (GHCR)**.

## 1. Arquitectura del Flujo CI/CD

El objetivo principal de este entorno es automatizar el ciclo de vida del contenedor de la aplicación. Cada vez que se introduce nuevo código en el repositorio, el pipeline se activa para garantizar que la aplicación se compila correctamente y que la imagen Docker resultante queda disponible de forma pública o privada en un registro seguro.


```

                [ Código Desarrollador ]
                             │
                             ▼ (Push / Pull Request en rama main)
┌─────────────────────────────────────────────────────────┐
│                  GITHUB ACTIONS WORKFLOW                │
│                                                         │
│  1. Checkout Código (incluyendo submódulos)             │
│  2. Autenticación en GitHub Container Registry (GHCR)   │
│  3. Construcción de Imagen (Multi-tag: SHA y latest)    │
│  4. Publicación (Push) en ghcr.io                       │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
        ┌─────────────────────────────────────┐
        │   GITHUB CONTAINER REGISTRY (GHCR)  │
        │  - evmaudit:[commit_sha]            │
        │  - evmaudit:latest                  │
        └─────────────────────────────────────┘

```

---

## 2. Configuración del Trigger (Disparadores)

El archivo de configuración de la acción (`.github/workflows/docker-ci.yml`) está diseñado para reaccionar ante dos eventos críticos en la rama principal:

* **`push` en la rama `main`:** Cuando se consolida código directamente o se acepta un merge.
* **`pull_request` hacia la rama `main`:** Permite validar de forma anticipada si los cambios propuestos rompen la construcción de la imagen antes de ser fusionados.

---

## 3. Desglose del Pipeline (Jobs y Steps)

El workflow está compuesto por dos trabajos (*jobs*) principales ejecutados sobre entornos virtuales limpios de **`ubuntu-latest`**:

### Job 1: `create-docker-image`
Es el núcleo del pipeline. Se encarga de la construcción y empaquetado del software a través de los siguientes pasos:

1. **Descarga del Repositorio (`Checkout code`):**
   Utiliza la acción oficial `actions/checkout@v2`. Incluye el parámetro crítico `submodules: 'recursive'`, el cual es obligatorio en nuestra arquitectura para clonar de forma automática el subdirectorio/repositorio `evmaudit` que contiene el *core* de análisis de la aplicación.
   
2. **Autenticación en el Registro (`Login to GitHub Container Registry`):**
   Utiliza `docker/login-action@v2` para autenticarse en el servidor `ghcr.io`. Para el inicio de sesión:
   * **Usuario:** Toma dinámicamente el actor de GitHub que disparó el evento (`${{ github.actor }}`).
   * **Contraseña / Token:** Utiliza un secreto personalizado guardado en el repositorio llamado `${{ secrets.IMAGES_TFM_UNIR }}`.

3. **Construcción y Publicación de la Imagen (`Build and push Docker image`):**
   Para optimizar el almacenamiento y el rastreo de versiones, el proceso realiza las siguientes tareas mediante scripts de consola:
   * **Normalización del nombre:** Convierte el nombre del repositorio a minúsculas mediante `tr '[:upper:]' '[:lower:]'` debido a que las especificaciones de Docker y GHCR prohíben caracteres en mayúscula para los nombres de las imágenes.
   * **Estrategia de Doble Etiquetado (*Multi-tagging*):**
     * `IMAGE_SHA`: Etiqueta la imagen con el hash único del *commit* (`${{ github.sha }}`). Esto garantiza la inmutabilidad y la trazabilidad (saber exactamente qué código dio origen a qué contenedor).
     * `IMAGE_LATEST`: Etiqueta la imagen con el *tag* `latest` para apuntar siempre a la última versión estable construida.
   * **Compilación Multiplataforma:** Fuerza la construcción bajo la arquitectura `--platform linux/amd64` para asegurar la compatibilidad con el entorno de despliegue final.
   * **Push:** Sube de manera consecutiva ambas etiquetas al registro de GitHub.

### Job 2: `deploy` (Marcador de posición / Placeholder)
Este trabajo depende directamente de la finalización exitosa del primero (`needs: create-docker-image`). Actualmente, actúa como un *placeholder* (imprime un mensaje en consola) diseñado para albergar en el futuro los comandos de despliegue automatizado en el servidor de producción (como webhooks, SSH deploys, o GitOps).

---

## 4. Gestión de Secretos y Permisos

Para que el pipeline funcione de forma correcta sin comprometer la seguridad del proyecto, se deben configurar los siguientes parámetros en la interfaz de GitHub:

1. **Secretos del Repositorio:**
   Ir a `Settings -> Secrets and variables -> Actions` y añadir el token:
   * `IMAGES_TFM_UNIR`: Un *Personal Access Token (PAT)* de GitHub con permisos mínimos de `write:packages` y `read:packages` para poder inyectar la imagen en el registro de la organización o usuario.

2. **Permisos de los Paquetes (GHCR):**
   Asegurarse de que el paquete resultante (`evmaudit`) tenga los permisos de acceso correctos vinculados al repositorio para permitir la descarga (*pull*) desde entornos locales o servidores externos.
---

Aquí tienes la redacción formal y académica de este bloque, estructurada para dar continuidad al apartado anterior de tu memoria del TFM. Sigue el mismo estilo riguroso, el uso de la tercera persona (pasiva refleja) y la justificación técnica de cada decisión de diseño.

---

## X.4. Entorno de Integración Continua (CI/CD) y Publicación Automatizada

Para garantizar la integridad del software durante el ciclo de vida del desarrollo y agilizar el flujo de despliegue, se ha diseñado e implementado un pipeline de Integración Continua (CI) basado en **GitHub Actions**. Esta estrategia de ingeniería de software permite automatizar la compilación, verificación y empaquetado de la aplicación en cada iteración, mitigando los riesgos asociados a la integración manual de código y asegurando la disponibilidad inmediata de artefactos listos para producción.

### X.4.1. Arquitectura del Workflow y Disparadores (*Triggers*)

El flujo de trabajo automatizado se define de manera declarativa mediante la sintaxis YAML de GitHub Actions. Con el propósito de optimizar los recursos de cómputo y mantener un control estricto sobre la estabilidad de la rama principal, se han configurado dos disparadores específicos:

* **Eventos de Empuje (*Push*):** El pipeline se ejecuta de forma automática ante cualquier consolidación directa de código en la rama `main`, asegurando que cada incremento de software sea evaluado y empaquetado de inmediato.
* **Solicitudes de Extracción (*Pull Requests*):** La automatización actúa como una barrera de calidad (*quality gate*) ante cualquier intento de fusión hacia la rama `main`. Esto permite validar que las modificaciones propuestas por los desarrolladores no rompan el proceso de construcción del contenedor antes de que el código sea integrado definitivamente.

El entorno de ejecución seleccionado para los trabajos (*jobs*) es `ubuntu-latest`, lo que proporciona un entorno virtual limpio, aislado y actualizado de manera nativa por la infraestructura de GitHub.

### X.4.2. Desglose Técnico de las Etapas del Pipeline

El ciclo de vida del pipeline se divide en dos trabajos secuenciales y dependientes, los cuales ejecutan tareas críticas de aprovisionamiento, autenticación y despliegue:

#### A. Trabajo de Construcción y Publicación (`create-docker-image`)

Es el núcleo técnico de la automatización y consta de los siguientes pasos detallados:

1. **Clonación del Repositorio y Gestión de Submódulos:** Se utiliza la acción oficial `actions/checkout@v2`. Debido a la arquitectura desacoplada del proyecto, es indispensable configurar el parámetro `submodules: 'recursive'`. Esta directiva instruye al agente para que descargue e integre de manera automática el repositorio y código de `evmaudit` dentro de la estructura de directorios del pipeline.
2. **Autenticación en el Registro de Contenedores (GHCR):** Mediante la acción `docker/login-action@v2`, el pipeline establece una conexión segura con el registro oficial de GitHub (`ghcr.io`). El proceso se autentica de forma dinámica utilizando el actor del ciclo de vida (`${{ github.actor }}`) y un token de acceso seguro almacenado de forma cifrada en los secretos del repositorio bajo la clave `${{ secrets.IMAGES_TFM_UNIR }}`.
3. **Normalización del Espacio de Nombres y Doble Etiquetado (*Multi-tagging*):** Las especificaciones de Docker y el estándar de la Open Container Initiative (OCI) prohíben estrictamente el uso de caracteres en mayúscula para los nombres de las imágenes de contenedores. Para solucionar esto, el pipeline ejecuta un script en Bash que convierte dinámicamente el nombre del repositorio a minúsculas utilizando el comando `tr '[:upper:]' '[:lower:]'`. Posteriormente, se implementa una estrategia de doble etiquetado para optimizar la trazabilidad y la inmutabilidad:
* **Etiqueta por SHA (`IMAGE_SHA`):** Vincula de forma unívoca el contenedor con el hash del *commit* específico de Git que originó la compilación (`${{ github.sha }}`). Esto permite realizar auditorías retrospectivas y despliegues deterministas en caso de fallos.
* **Etiqueta de Última Versión (`IMAGE_LATEST`):** Sobrescribe el puntero `:latest` con la versión más reciente del software que haya superado la fase de construcción con éxito.


4. **Construcción y *Push* Multiplataforma:** Se invoca de manera directa el comando `docker build`, forzando la compilación bajo la arquitectura destino `--platform linux/amd64` utilizando el `Dockerfile` del proyecto como plano de construcción. Una vez generadas las imágenes locales con sus respectivas etiquetas, se ejecutan las instrucciones de empuje (*push*) hacia el registro seguro de GitHub, quedando el artefacto disponible para su consumo.



#### B. Trabajo de Despliegue (`deploy`)

Para garantizar una separación formal de conceptos, el pipeline implementa un segundo trabajo denominado `deploy`. Utilizando la directiva `needs: create-docker-image`, se establece una restricción de dependencia estricta: esta etapa no puede inicializarse si el empaquetado previo ha fallado.

Actualmente, este bloque opera como un punto de anclaje (*placeholder*) arquitectónico que ejecuta un comando de verificación en consola, diseñado específicamente para integrarse en fases posteriores del proyecto con herramientas de despliegue continuo (CD) en servidores de producción mediante protocolos seguros (como SSH, Webhooks o flujos GitOps).


---

#### B. Trabajo de Despliegue (`deploy`) y Limitaciones del Entorno

Para garantizar una separación formal de conceptos en la arquitectura de la integración, el pipeline implementa un segundo trabajo secuencial denominado `deploy`. Utilizando la directiva `needs: create-docker-image`, se establece una restricción de dependencia estricta: esta etapa no puede inicializarse si el empaquetado y la publicación previa de la imagen en el registro han fallado.

En la fase actual del proyecto, **esta etapa automatizada no ha sido implementada de forma activa y opera estrictamente como un punto de anclaje (*placeholder*) arquitectónico**. La justificación de esta decisión de diseño radica en las limitaciones técnicas del entorno de alojamiento seleccionado para las pruebas de concepto. La infraestructura de EVMAudit se despliega externamente en la plataforma PaaS **Railway** utilizando su modalidad de suscripción gratuita. Este nivel de servicio impone restricciones en las interfaces de programación (APIs) y en el uso de *webhooks*, impidiendo la ejecución de despliegues totalmente automatizados (*Automated CD Triggers*) desencadenados de forma directa mediante agentes de terceros como GitHub Actions.

Por consiguiente, el flujo de trabajo en este punto se limita a verificar la integridad de la secuencia de comandos en consola, quedando el aprovisionamiento de la infraestructura supeditado a los mecanismos nativos de la plataforma de destino. En el **siguiente apartado (X.5. Despliegue de la Infraestructura)**, se expondrá de manera más amplia la configuración, el aprovisionamiento y las características operativas de dicho entorno en Railway.