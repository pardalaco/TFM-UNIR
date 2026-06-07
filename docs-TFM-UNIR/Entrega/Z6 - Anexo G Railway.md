# ANEXO G.	DESPLIEGUE DE LA INFRAESTRUCTURA EN LA NUBE (RAILWAY) 
Para validar la operatividad de EVMAudit en un entorno accesible y simular un escenario de producción real, se ha procedido al despliegue de la arquitectura contenedorizada en la plataforma de Plataforma como Servicio (PaaS) Railway. A continuación, se detallan las especificaciones del entorno, las restricciones técnicas de hardware identificadas y las optimizaciones de ingeniería aplicadas en el código fuente para garantizar la estabilidad del sistema.
5.2.15. Aprovisionamiento y Configuración del Entorno Cloud
El proceso de despliegue en la infraestructura de la nube se ha estructurado bajo las siguientes directrices operativas:
•	Selección del Nivel de Servicio: La instancia se ha instanciado haciendo uso del nivel gratuito (Free Tier) de la plataforma, el cual provee un crédito base de $5 USD o un límite temporal de 30 días de cómputo.
•	Aislamiento Regional: Con el objetivo de minimizar la latencia de red en las peticiones HTTP y optimizar la transferencia de datos, se ha seleccionado la región europea con nodo central en Ámsterdam (EU).
•	Mapeo de Infraestructura y Orquestación: El aprovisionamiento se realiza directamente vinculando el contenedor web a la imagen Docker compilada y almacenada en el registro de GitHub (ghcr.io), exponiendo de manera transparente la API del backend desarrollada en FastAPI.
•	Enrutamiento y Capa de Enlace (SSL): La plataforma genera de manera dinámica un nombre de dominio completamente cualificado (FQDN) provisto de seguridad criptográfica TLS/SSL (HTTPS) para el acceso público a la interfaz de usuario: https://evmaudit-production.up.railway.app/.
5.2.16. Limitaciones de Hardware y el Problema del Desbordamiento de Memoria (OOM)
La modalidad gratuita de la plataforma PaaS impone restricciones estrictas sobre los recursos de hardware asignados a cada contenedor, parametrizados de la siguiente forma:
•	Capacidad de Cómputo (CPU): 2 vCPU virtuales compartidas.
•	Memoria Volátil (RAM): 1 GB con un límite estricto de cuota (Plan Limit).
Bajo un escenario de despliegue convencional en servidores dedicados o infraestructura local, el pipeline de análisis de EVMAudit se ejecuta sin restricciones debido a la disponibilidad de memoria elástica. Sin embargo, en el entorno de la nube restringido, el motor de fuzzing basado en propiedades Echidna presenta un problema crítico de arquitectura.
Echidna, al estar desarrollado en Haskell, requiere de forma nativa una reserva inicial y un espacio de intercambio que supera con creces el gigabyte de memoria RAM para gestionar el mapa de cobertura del binario y la generación de casos de prueba. Al alcanzar el umbral crítico de 1 GB asignado por Railway, el demonio del sistema operativo anfitrión (Kernel Out-of-Memory Killer) destruía de manera abrupta el contenedor para salvaguardar la integridad del nodo, provocando la caída del servicio web y reportando un error de tipo OOM.
5.2.17. Optimización del Sistema en Tiempo de Ejecución (RTS) de Haskell
Para mitigar el desbordamiento de memoria sin alterar las capacidades analíticas esenciales de la herramienta, se realizó una intervención a nivel de código en el módulo de control del pipeline (run_echidna). La solución consistió en inyectar directivas específicas orientadas a reconfigurar los parámetros del Runtime System (RTS) del compilador de Glasgow Haskell (GHC) empaquetados dentro del binario de Echidna.
La estructura de invocación del proceso fue modificada e implementada en Python mediante el siguiente diseño de argumentos:
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
A continuación se expone la justificación técnica detrás de los modificadores inyectados:
•	Restricción de Ensayos (--test-limit 100): Al parametrizar el límite de pruebas en 100 iteraciones, se acota la profundidad del grafo de ejecución generado por el fuzzer. Esto reduce el consumo de memoria acumulativo a lo largo del tiempo de computación.
•	Techo Infranqueable de Memoria (-M950m): Esta directiva establece que el asignador de memoria de Haskell tiene prohibido estrictamente reclamar más de 950 megabytes del espacio de usuario. Al situar este límite ligeramente por debajo del gigabyte real de Railway, se evita que el sistema operativo de la nube elimine el proceso por exceder la cuota física.
•	Recolección de Basura Agresiva (-c): Activa un algoritmo de recolección de residuos más severo en el recolector de basura de Haskell (Garbage Collector). En lugar de acumular objetos intermedios en la memoria RAM, el sistema libera los recursos obsoletos inmediatamente después de cada evaluación de propiedad.
•	Concurrencia Confinada (-N1): Limita la ejecución del entorno de ejecución a un único hilo de procesamiento, evitando la duplicación de estructuras de datos en memoria asociadas al paralelismo de hilos nativos.
Es importante destacar que la optimización descrita no se integró de forma estática en la construcción del archivo Dockerfile (lo que habría alterado el comportamiento de la imagen base de manera permanente), sino que se aplicó directamente sobre el código fuente desplegado en el contenedor en ejecución (runtime). Bajo condiciones de despliegue convencionales en infraestructuras con escalabilidad elástica o recursos dedicados de hardware, esta intervención técnica resultaría completamente innecesaria, ya que la aplicación contaría con la memoria suficiente para procesar el pipeline por defecto. Por consiguiente, esta modificación responde de manera estricta a un mecanismo de mitigación ad hoc, implementado exclusivamente para sortear las limitaciones físicas del entorno gratuito y evitar la interrupción forzada del servicio web por falta de memoria.
Conclusión del Despliegue: La implementación de estas salvaguardas de bajo nivel ha permitido que la aplicación web de EVMAudit opere de manera completamente estable y fluida en la nube. Pese a las severas restricciones del entorno gratuito de Railway, el sistema es capaz de completar con éxito el pipeline completo de auditoría en siete pasos sin registrar caídas en el servicio ni excepciones por falta de recursos.

 

