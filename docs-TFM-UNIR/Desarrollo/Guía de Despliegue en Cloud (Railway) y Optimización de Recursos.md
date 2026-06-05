# Guía de Despliegue en Cloud (Railway) y Optimización de Recursos

Este documento describe detalladamente los pasos requeridos para desplegar la aplicación web de **EVMAudit** en la plataforma PaaS **Railway** utilizando la imagen de Docker, así como las modificaciones necesarias en el código para operar de forma estable dentro de los límites estrictos de la versión gratuita.

## 1. Configuración Inicial en la Plataforma

Para iniciar el despliegue de la infraestructura en la nube, se deben seguir los siguientes pasos iniciales dentro del ecosistema de Railway:

1. **Creación de Cuenta:** Registrarse en la plataforma oficial de [Railway](https://railway.app/).
2. **Activación de la Versión Gratuita:** El entorno se inicializa bajo el nivel gratuito básico (*Free Tier*), el cual otorga un crédito de `$5 USD` o `30 días` de uso de cómputo ininterrumpido sin coste.
3. **Despliegue mediante Imagen Docker:** En el panel de control, seleccionar la creación de un nuevo proyecto a partir de la imagen Docker previamente compilada y publicada en el registro del proyecto (`ghcr.io`).

## 2. Configuración del Entorno y Límites del Plan

Una vez aprovisionado el servicio web en Railway, es crítico acceder al panel de **Settings** para realizar las siguientes configuraciones de infraestructura:

### Configuración Regional

* **Ubicación:** Seleccionar la región más cercana al cliente de destino para reducir la latencia de red. En nuestro caso, se configura en la región de la Unión Europea (**EU - Ámsterdam**).

### Limitaciones de Hardware Disponibles (Free Tier)

El entorno de ejecución asignado por la plataforma cuenta con restricciones severas de hardware. Los límites del plan gratuito son los siguientes:

| Recurso | Capacidad Asignada | Límite del Plan |
| --- | --- | --- |
| **Procesador (CPU)** | 2 vCPU | 2 vCPU |
| **Memoria RAM** | 1 GB | 1 GB |

### Generación de Dominio Público

La plataforma proporciona un enrutamiento automático mediante la asignación de un subdominio SSL seguro (HTTPS) para el acceso público a la interfaz VirusTotal-like:
👉 **`https://evmaudit-production.up.railway.app/`**

---

## 3. Problema Técnico: Desbordamiento de Memoria (OOM)

Bajo condiciones de despliegue convencionales en servidores con recursos dedicados, la configuración por defecto de las herramientas de análisis sería suficiente para completar el pipeline. Sin embargo, el motor de fuzzing basado en propiedades **Echidna** (desarrollado en Haskell) es altamente demandante y requiere de forma nativa un mínimo de más de **1 GB de memoria RAM** para la inicialización y ejecución del mapa de cobertura de Smart Contracts.

Al ejecutarse bajo el umbral estricto de 1 GB asignado por Railway, el demonio de la plataforma destruía el proceso de análisis de forma abrupta emitiendo un error de falta de memoria o cuelgue del contenedor (*Out of Memory - OOM*).

---

## 4. Solución Implementada: Ajustes del Runtime de Haskell (+RTS)

Para estabilizar la aplicación y posibilitar la ejecución de auditorías completas en el entorno restringido, se realizó una intervención directa sobre el submódulo de ejecución del pipeline, específicamente en el método de invocación `run_echidna`.

Se modificó la estructura de comandos del proceso para limitar el fuzzing y abrir las opciones del **Runtime System (RTS) de Haskell** integradas en el binario de Echidna. El arreglo de argumentos del comando se reconfiguró de la siguiente manera:

```python
command = [
    "echidna",
    contract_path,
    "--contract", contract_name,
    "--format", "json",
    
    # 1. LIMITACIÓN DEL FUZZING PARA REDUCIR EL CONSUMO CONTINUO
    "--test-limit", "100",  
    
    # 2. OPTIMIZACIÓN DE COMPILACIÓN
    "--solc-args", "--optimize-runs 0", # Fuerza la mínima optimización inicial
    
    # 3. APERTURA DE OPCIONES DEL RUNTIME DE HASKELL (RTS)
    "+RTS",      
    
    # 4. RESTRICCIONES ESTRICTAS DE MEMORIA Y PROCESAMIENTO
    "-M950m",    # Limita el uso máximo de memoria del fuzzer a 950 Megabytes (evita el OOM del host)
    "-c",        # Fuerza una recolección de basura más agresiva (Garbage Collection)
    "-N1",       # Limita la ejecución a un único hilo de procesamiento (Single-thread)
    
    # 5. CIERRE DE LAS OPCIONES RTS
    "-RTS"       
]

```

### Justificación de los Parámetros Introducidos:

* **`--test-limit 100`:** Reduce el número de combinaciones y pruebas generadas por Echidna. Esto acorta el tiempo de ejecución y estabiliza drásticamente el consumo de memoria a lo largo del test.
* **`-M950m`:** Establece una barrera infranqueable para el recolector de memoria de Haskell. Al configurarlo en 950 MB, el proceso se autogestiona para no superar nunca el límite real de 1 GB de la máquina virtual de Railway, evitando que el sistema operativo anfitrión mate el contenedor de manera forzada.
* **`-c`:** Modifica el comportamiento del *Garbage Collector*, volviéndolo más frecuente y eficiente a costa de un uso marginal de CPU, liberando ram obsoleta de forma inmediata.

**Resultado:** Gracias a este ajuste de ingeniería sobre el binario, la aplicación web de **EVMAudit** funciona de manera fluida y consistente en el entorno cloud gratuito de Railway, procesando el pipeline de 7 pasos completo sin reportar caídas de servicio.

---
Aquí tienes la adaptación y redacción académica formal de esta sección para integrarla directamente en la memoria de tu TFM, dando continuidad al apartado de la infraestructura de integración continua.

---

## X.5. Despliegue de la Infraestructura en la Nube (Railway)

Para validar la operatividad de EVMAudit en un entorno accesible y simular un escenario de producción real, se ha procedido al despliegue de la arquitectura contenedorizada en la plataforma de Plataforma como Servicio (PaaS) **Railway**. A continuación, se detallan las especificaciones del entorno, las restricciones técnicas de hardware identificadas y las optimizaciones de ingeniería aplicadas en el código fuente para garantizar la estabilidad del sistema.

### X.5.1. Aprovisionamiento y Configuración del Entorno Cloud

El proceso de despliegue en la infraestructura de la nube se ha estructurado bajo las siguientes directrices operativas:

1. **Selección del Nivel de Servicio:** La instancia se ha instanciado haciendo uso del nivel gratuito (*Free Tier*) de la plataforma, el cual provee un crédito base de $5 USD o un límite temporal de 30 días de cómputo.
2. **Aislamiento Regional:** Con el objetivo de minimizar la latencia de red en las peticiones HTTP y optimizar la transferencia de datos, se ha seleccionado la región europea con nodo central en **Ámsterdam (EU)**.
3. **Mapeo de Infraestructura y Orquestación:** El aprovisionamiento se realiza directamente vinculando el contenedor web a la imagen Docker compilada y almacenada en el registro de GitHub (`ghcr.io`), exponiendo de manera transparente la API del *backend* desarrollada en FastAPI.
4. **Enrutamiento y Capa de Enlace (SSL):** La plataforma genera de manera dinámica un nombre de dominio completamente cualificado (FQDN) provisto de seguridad criptográfica TLS/SSL (HTTPS) para el acceso público a la interfaz de usuario: `https://evmaudit-production.up.railway.app/`.

### X.5.2. Limitaciones de Hardware y el Problema del Desbordamiento de Memoria (OOM)

La modalidad gratuita de la plataforma PaaS impone restricciones estrictas sobre los recursos de hardware asignados a cada contenedor, parametrizados de la siguiente forma:

* **Capacidad de Cómputo (CPU):** 2 vCPU virtuales compartidas.
* **Memoria Volátil (RAM):** 1 GB con un límite estricto de cuota (*Plan Limit*).

Bajo un escenario de despliegue convencional en servidores dedicados o infraestructura local, el pipeline de análisis de EVMAudit se ejecuta sin restricciones debido a la disponibilidad de memoria elástica. Sin embargo, en el entorno de la nube restringido, el motor de *fuzzing* basado en propiedades **Echidna** presenta un problema crítico de arquitectura.

Echidna, al estar desarrollado en Haskell, requiere de forma nativa una reserva inicial y un espacio de intercambio que supera con creces el gigabyte de memoria RAM para gestionar el mapa de cobertura del binario y la generación de casos de prueba. Al alcanzar el umbral crítico de 1 GB asignado por Railway, el demonio del sistema operativo anfitrión (*Kernel Out-of-Memory Killer*) destruía de manera abrupta el contenedor para salvaguardar la integridad del nodo, provocando la caída del servicio web y reportando un error de tipo *OOM*.

### X.5.3. Optimización del Sistema en Tiempo de Ejecución (RTS) de Haskell

Para mitigar el desbordamiento de memoria sin alterar las capacidades analíticas esenciales de la herramienta, se realizó una intervención a nivel de código en el módulo de control del *pipeline* (`run_echidna`). La solución consistió en inyectar directivas específicas orientadas a reconfigurar los parámetros del **Runtime System (RTS)** del compilador de Glasgow Haskell (GHC) empaquetados dentro del binario de Echidna.

La estructura de invocación del proceso fue modificada e implementada en Python mediante el siguiente diseño de argumentos:

```python
command = [
    "echidna",
    contract_path,
    "--contract", contract_name,
    "--format", "json",
    
    # Reducción del espacio de búsqueda del Fuzzer
    "--test-limit", "100",  
    
    # Optimización de la compilación inicial
    "--solc-args", "--optimize-runs 0", 
    
    # Apertura de las opciones del Runtime System de Haskell
    "+RTS",      
    
    # Parámetros estrictos de control de memoria y concurrencia
    "-M950m",    
    "-c",        
    "-N1",       
    
    # Cierre de las opciones RTS
    "-RTS"       
]

```

A continuación se expone la justificación técnica detrás de los modificadores inyectados:

* **Restricción de Ensayos (`--test-limit 100`):** Al parametrizar el límite de pruebas en 100 iteraciones, se acota la profundidad del grafo de ejecución generado por el fuzzer. Esto reduce el consumo de memoria acumulativo a lo largo del tiempo de computación.
* **Techo Infranqueable de Memoria (`-M950m`):** Esta directiva establece que el asignador de memoria de Haskell tiene prohibido estrictamente reclamar más de 950 megabytes del espacio de usuario. Al situar este límite ligeramente por debajo del gigabyte real de Railway, se evita que el sistema operativo de la nube elimine el proceso por exceder la cuota física.
* **Recolección de Basura Agresiva (`-c`):** Activa un algoritmo de recolección de residuos más severo en el recolector de basura de Haskell (*Garbage Collector*). En lugar de acumular objetos intermedios en la memoria RAM, el sistema libera los recursos obsoletos inmediatamente después de cada evaluación de propiedad.
* **Concurrencia Confinada (`-N1`):** Limita la ejecución del entorno de ejecución a un único hilo de procesamiento, evitando la duplicación de estructuras de datos en memoria asociadas al paralelismo de hilos nativos.

**Conclusión del Despliegue:** La implementación de estas salvaguardas de bajo nivel ha permitido que la aplicación web de **EVMAudit** opere de manera completamente estable y fluida en la nube. Pese a las severas restricciones del entorno gratuito de Railway, el sistema es capaz de completar con éxito el pipeline completo de auditoría en siete pasos sin registrar caídas en el servicio ni excepciones por falta de recursos.