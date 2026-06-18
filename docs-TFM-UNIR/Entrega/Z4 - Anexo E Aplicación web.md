# Anexo E. Aplicación web desarrollada

Para facilitar la evaluación práctica del pipeline EVMAudit por parte de usuarios sin conocimientos de línea de comandos, se ha desarrollado una aplicación web que expone el analizador de contratos inteligentes a través de una interfaz gráfica accesible desde el navegador. El código de esta aplicación se encuentra en el directorio `webapp/` del repositorio del proyecto, de forma independiente al paquete `evmaudit` que contiene la lógica de análisis, lo que permite reutilizar dicho paquete como una librería sin acoplar la interfaz web a su implementación interna.

## Arquitectura general

La aplicación sigue una arquitectura cliente-servidor de dos capas. El backend está implementado en Python con el framework **FastAPI** y se ejecuta mediante el servidor ASGI **Uvicorn**. Este backend importa y reutiliza directamente los módulos del paquete `evmaudit` (`runner`, `normalizer`, `correlator`, `echidna_adapter` y `reporter`), de modo que el flujo de análisis ejecutado desde la interfaz web es exactamente el mismo que el que se ejecuta desde la línea de comandos. El frontend es una aplicación de página única (*Single Page Application*) construida con HTML, CSS y JavaScript sin frameworks ni dependencias externas, lo que simplifica su despliegue al no requerir un proceso de compilación (*build*).

## Backend: API REST

El backend expone los siguientes endpoints:

- **`GET /`**: sirve la página principal de la aplicación (`index.html`).
- **`POST /analyze`**: recibe un fichero Solidity (`.sol`) subido por el usuario, lo guarda en `jsons/_uploads/`, detecta el nombre del contrato y lanza el análisis en segundo plano, devolviendo un identificador de trabajo (`job_id`).
- **`POST /analyze-code`**: variante del endpoint anterior que recibe el código fuente del contrato directamente como texto en formato JSON, en lugar de un fichero, pensada para el editor integrado en la propia interfaz.
- **`GET /status/{job_id}`**: devuelve el estado de un análisis en curso (`running`, `done` o `error`), junto con el paso actual del pipeline (de 1 a 7) y un mensaje descriptivo, lo que permite a la interfaz mostrar el progreso en tiempo real.
- **`GET /result/{job_id}`**: una vez finalizado el análisis, devuelve el informe completo generado por `reporter.py`: metadatos del contrato, resumen (`risk_score`, número total de hallazgos, hallazgos confirmados y de severidad alta), el listado de hallazgos correlacionados y los resultados de las propiedades de Echidna.
- **`GET /result/{job_id}/pdf`**: genera y descarga el informe en formato PDF a partir del Markdown producido por el reporter.

## Ejecución asíncrona del pipeline

Dado que el análisis completo de un contrato (Slither, Mythril y Echidna) puede tardar entre varios segundos y varios minutos, cada solicitud de análisis se ejecuta en un hilo independiente (*daemon thread*) en segundo plano, mientras la API responde inmediatamente con el `job_id` generado. El estado de cada trabajo se mantiene en memoria, en un diccionario global indexado por `job_id`. El frontend consulta periódicamente (cada dos segundos, mediante *polling*) el endpoint `/status/{job_id}` hasta que el estado pasa a `done` o `error`, momento en el que solicita el resultado final a `/result/{job_id}`.

Internamente, el hilo de trabajo recorre las siete etapas del pipeline:

```python
set_step(1, "Ejecutando Slither...")
slither_raw = run_slither(contract_path)

set_step(2, "Ejecutando Mythril (puede tardar 2-3 min)...")
mythril_raw = run_mythril(contract_path, timeout=180, depth=22)

set_step(3, "Normalizando resultados...")
slither_norm = normalize_slither_output(slither_raw)
mythril_norm = normalize_mythril_output(mythril_raw)

set_step(4, "Correlacionando hallazgos...")
corr = correlate(slither_norm, mythril_norm, contract_path)

set_step(5, "Generando wrapper Echidna...")
meta = generate_echidna_wrapper(corr, contract_path, contract_name)

set_step(6, "Ejecutando Echidna (fuzzing)...")
echidna_raw = run_echidna(meta["wrapper_path"], meta["contract_name_echidna"],
                          output_contract_path=contract_path)

set_step(7, "Generando informe...")
report = generate_report(contract_path, corr, echidna_raw, meta)
```

El paso 6 solo se ejecuta si el adapter generó un wrapper (`meta["wrapper_path"]` no es `None`), es decir, cuando existe al menos una vulnerabilidad con plantilla Echidna disponible en el catálogo.

## Frontend: interfaz de usuario

La interfaz adopta un diseño en modo oscuro inspirado en herramientas de análisis de seguridad como VirusTotal, y se organiza en varias secciones que se muestran u ocultan dinámicamente según el estado del análisis:

- **Sección de entrada**: dos pestañas para subir un fichero `.sol` o pegar el código directamente en un editor integrado.
- **Sección de progreso**: barra de siete pasos que se va completando a medida que avanza el pipeline, con el mensaje descriptivo de cada etapa.
- **Sección de resultados**: círculo con la puntuación de riesgo (`risk_score`) en una escala de 0 a 10, coloreado en verde, naranja o rojo según el nivel de riesgo; tres indicadores numéricos (hallazgos totales, hallazgos confirmados y hallazgos de severidad alta); tabla de hallazgos correlacionados (severidad, categoría, función afectada, código SWC y nivel de confianza); tabla de resultados de las propiedades ejecutadas por Echidna.
- **Sección de error**: mensaje descriptivo del fallo y botón para reiniciar el análisis.

!TODO: insertar captura de pantalla de la interfaz web.

## Ejemplo de uso real: análisis de MultiVuln.sol

Para ilustrar el funcionamiento conjunto del backend y el frontend, se reproduce a continuación el flujo real seguido al analizar el contrato `MultiVuln.sol` a través de la interfaz web.

El usuario sube el fichero `MultiVuln.sol` desde la pestaña de carga de fichero, lo que desencadena una petición `POST /analyze` y la obtención de un `job_id`. A partir de ese momento, el frontend consulta `GET /status/{job_id}` cada dos segundos, mostrando el avance de la barra de progreso a medida que el backend completa cada una de las siete etapas.

Cuando el estado pasa a `done`, el frontend solicita `GET /result/{job_id}` y recibe el mismo informe que se obtendría ejecutando `evmaudit` por línea de comandos sobre el mismo contrato: una puntuación de riesgo (`risk_score`) de 8.3/10 y tres hallazgos confirmados de severidad alta y media (SWC-107, SWC-106 y SWC-115). La interfaz representa esta puntuación mediante un círculo de color rojo, junto con la tabla de hallazgos correlacionados y la tabla de resultados de las propiedades ejecutadas por Echidna (la correspondiente a SWC-106 finaliza con resultado `failed`, evidenciando la explotabilidad real de la función `kill`).

Este resultado confirma que la aplicación web no introduce ninguna divergencia respecto al pipeline subyacente: ambas interfaces son dos formas de acceso al mismo análisis.

!TODO: insertar captura de pantalla del resultado de MultiVuln.sol en la interfaz web.

## Pila tecnológica y ejecución

La aplicación se gestiona con las mismas herramientas que el resto del proyecto: el entorno y las dependencias se administran con `uv`, y requiere Python 3.12 o superior además de las herramientas de análisis (Slither, Mythril y Echidna 2.3.2) instaladas en el sistema. El servidor se arranca con el comando:

```bash
python3 -m uvicorn webapp.app:app --host 0.0.0.0 --port 8000
```

quedando la interfaz accesible en el navegador a través de dicho puerto. Los ficheros subidos y los resultados intermedios de cada análisis se almacenan, igual que en el resto del pipeline, bajo el directorio `jsons/`, organizados por nombre de contrato.

En su estado actual, la aplicación constituye una capa de demostración funcional sobre el pipeline de `evmaudit`, pensada para facilitar pruebas y demostraciones del proyecto sin necesidad de utilizar la línea de comandos. Además de su ejecución en local, la aplicación se ha desplegado en un entorno accesible públicamente, tal y como se describe en el Anexo G (Despliegue de la Infraestructura en la Nube).
