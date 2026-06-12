# ANEXO F.	ENTORNO DE INTEGRACIÓN CONTINUA (CI/CD) Y PUBLICACIÓN AUTOMATIZADA

Para garantizar la integridad del software durante el ciclo de vida del desarrollo y agilizar el flujo de despliegue, se ha diseñado e implementado un pipeline de Integración Continua (CI) basado en **GitHub Actions**. Esta estrategia de ingeniería de software permite automatizar la compilación, verificación y empaquetado de la aplicación en cada iteración, mitigando los riesgos asociados a la integración manual de código y asegurando la disponibilidad inmediata de artefactos listos para producción.

## ANEXO F.1.	Arquitectura del Workflow y Disparadores (Triggers)

El flujo de trabajo automatizado se define de manera declarativa mediante la sintaxis YAML de GitHub Actions. Con el propósito de optimizar los recursos de cómputo y mantener un control estricto sobre la estabilidad de la rama principal, se han configurado dos disparadores específicos:

- **Eventos de Empuje (*Push*):** El pipeline se ejecuta de forma automática ante cualquier consolidación directa de código en la rama `main`, asegurando que cada incremento de software sea evaluado y empaquetado de inmediato.

- **Solicitudes de Extracción (*Pull Requests*):** La automatización actúa como una barrera de calidad (*quality gate*) ante cualquier intento de fusión hacia la rama `main`. Esto permite validar que las modificaciones propuestas por los desarrolladores no rompan el proceso de construcción del contenedor antes de que el código sea integrado definitivamente.

El entorno de ejecución seleccionado para los trabajos (*jobs*) es `ubuntu-latest`, lo que proporciona un entorno virtual limpio, aislado y actualizado de manera nativa por la infraestructura de GitHub.

## ANEXO F.2.	Desglose Técnico de las Etapas del Pipeline
El ciclo de vida del pipeline se divide en dos trabajos secuenciales y dependientes, los cuales ejecutan tareas críticas de aprovisionamiento, autenticación y despliegue:
 

### ANEXO F.2.1.	Trabajo de Construcción y Publicación (`create-docker-image`)

Es el núcleo técnico de la automatización y consta de los siguientes pasos detallados:

1.  **Clonación del Repositorio y Gestión de Submódulos:** Se utiliza la acción oficial `actions/checkout@v2`. Debido a la arquitectura desacoplada del proyecto, es indispensable configurar el parámetro `submodules: 'recursive'`. Esta directiva instruye al agente para que descargue e integre de manera automática el repositorio y código de `evmaudit` dentro de la estructura de directorios del pipeline.

2.  **Autenticación en el Registro de Contenedores (GHCR):** Mediante la acción `docker/login-action@v2`, el pipeline establece una conexión segura con el registro oficial de GitHub (`ghcr.io`). El proceso se autentica de forma dinámica utilizando el actor del ciclo de vida (`${{ github.actor }}`) y un token de acceso seguro almacenado de forma cifrada en los secretos del repositorio bajo la clave `${{ secrets.IMAGES_TFM_UNIR }}`.

3.  **Normalización del Espacio de Nombres y Doble Etiquetado (*Multi-tagging*):** Las especificaciones de Docker y el estándar de la Open Container Initiative (OCI) prohíben estrictamente el uso de caracteres en mayúscula para los nombres de las imágenes de contenedores. Para solucionar esto, el pipeline ejecuta un script en Bash que convierte dinámicamente el nombre del repositorio a minúsculas utilizando el comando `tr '[:upper:]' '[:lower:]'`. Posteriormente, se implementa una estrategia de doble etiquetado para optimizar la trazabilidad y la inmutabilidad:
	- **Etiqueta por SHA (**`IMAGE_SHA`**):** Vincula de forma unívoca el contenedor con el hash del *commit* específico de Git que originó la compilación (`${{ github.sha }}`). Esto permite realizar auditorías retrospectivas y despliegues deterministas en caso de fallos.
    - **Etiqueta de Última Versión (**`IMAGE_LATEST`**):** Sobrescribe el puntero `:latest` con la versión más reciente del software que haya superado la fase de construcción con éxito.

4.  **Construcción y *Push* Multiplataforma:** Se invoca de manera directa el comando `docker build`, forzando la compilación bajo la arquitectura destino `--platform linux/amd64` utilizando el `Dockerfile` del proyecto como plano de construcción. Una vez generadas las imágenes locales con sus respectivas etiquetas, se ejecutan las instrucciones de empuje (*push*) hacia el registro seguro de GitHub, quedando el artefacto disponible para su consumo.


### ANEXO F.2.2.	Trabajo de Despliegue (deploy) y Limitaciones del Entorno

Para garantizar una separación formal de conceptos en la arquitectura de la integración, el pipeline implementa un segundo trabajo secuencial denominado `deploy`. Utilizando la directiva `needs: create-docker-image`, se establece una restricción de dependencia estricta: esta etapa no puede inicializarse si el empaquetado y la publicación previa de la imagen en el registro han fallado.

En la fase actual del proyecto, **esta etapa automatizada no ha sido implementada de forma activa y opera estrictamente como un punto de anclaje (*placeholder*) arquitectónico**. La justificación de esta decisión de diseño radica en las limitaciones técnicas del entorno de alojamiento seleccionado para las pruebas de concepto. La infraestructura de EVMAudit se despliega externamente en la plataforma PaaS **Railway** utilizando su modalidad de suscripción gratuita. Este nivel de servicio impone restricciones en las interfaces de programación (APIs) y en el uso de *webhooks*, impidiendo la ejecución de despliegues totalmente automatizados (*Automated CD Triggers*) desencadenados de forma directa mediante agentes de terceros como GitHub Actions.

Por consiguiente, el flujo de trabajo en este punto se limita a verificar la integridad de la secuencia de comandos en consola, quedando el aprovisionamiento de la infraestructura supeditado a los mecanismos nativos de la plataforma de destino. En el **siguiente apartado (X.5. Despliegue de la Infraestructura)**, se expondrá de manera más amplia la configuración, el aprovisionamiento y las características operativas de dicho entorno en Railway.