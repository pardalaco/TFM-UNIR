# 1. Diagrama de componentes UML — Arquitectura general

```plantuml
@startuml
title Arquitectura general de EVMAudit

skinparam componentStyle rectangle
skinparam shadowing false

actor "Usuario" as User

component "Cliente CLI\nmain.py" as CLI
component "Aplicación web\nFastAPI" as Web

package "EVMAudit" {
  component "Runner" as Runner
  component "Normalizer" as Normalizer
  component "Correlator" as Correlator
  component "SWC Catalog" as Catalog
  component "Echidna Adapter" as Adapter
  component "Reporter" as Reporter
  component "Exceptions" as Exceptions
}

component "Slither" as Slither <<external>>
component "Mythril" as Mythril <<external>>
component "Echidna" as Echidna <<external>>

artifact "JSON crudo" as RawJSON
artifact "Finding normalizado" as NormalizedFinding
artifact "Finding correlacionado" as CorrelatedFinding
artifact "Wrapper Solidity" as Wrapper
artifact "Informe final" as FinalReport

User --> CLI
User --> Web

CLI --> Runner
Web --> Runner

Runner --> Slither
Runner --> Mythril
Runner --> Echidna
Runner --> RawJSON

RawJSON --> Normalizer
Normalizer --> NormalizedFinding
NormalizedFinding --> Correlator
Correlator --> CorrelatedFinding

CorrelatedFinding --> Adapter
Adapter --> Catalog
Adapter --> Wrapper
Wrapper --> Runner

CorrelatedFinding --> Reporter
Runner --> Reporter
Adapter --> Reporter
Reporter --> FinalReport

Runner ..> Exceptions
Normalizer ..> Exceptions
Reporter ..> Exceptions

@enduml
```

---

# 2. Diagrama de actividad UML — Pipeline completo

```plantuml
@startuml
title Pipeline completo de análisis de EVMAudit

skinparam shadowing false

start

:Recibir contrato Solidity;

if (¿Se proporciona nombre del contrato?) then (Sí)
  :Usar nombre proporcionado;
else (No)
  :Detectar nombre del contrato;
endif

:Leer pragma Solidity;
:Configurar versión de solc;

partition "Análisis con herramientas" {
  :Ejecutar Slither;
  :Guardar JSON crudo de Slither;

  :Ejecutar Mythril;
  :Guardar JSON crudo de Mythril;
}

partition "Normalización" {
  :Normalizar salida de Slither;
  :Normalizar salida de Mythril;
}

partition "Correlación" {
  :Agrupar hallazgos por contrato, función y SWC;
  :Calcular severidad máxima;
  :Calcular nivel de confianza;
  :Generar hallazgos correlacionados;
}

partition "Validación con Echidna" {
  :Consultar catálogo SWC;
  :Generar wrapper Solidity;

  if (¿Wrapper generado?) then (Sí)
    :Ejecutar Echidna;
    :Corregir nombres y estados si es necesario;
    :Guardar resultados de fuzzing;
  else (No)
    :Omitir ejecución de Echidna;
  endif
}

:Generar informe final;

stop
@enduml
```

---

# 3. Diagrama de paquetes UML — Estructura modular

```plantuml
@startuml
title Estructura modular de EVMAudit

skinparam packageStyle rectangle
skinparam shadowing false

package "evmaudit" {

  component "__init__.py" as Init

  component "runner.py" as Runner
  component "normalizer.py" as Normalizer
  component "correlator.py" as Correlator
  component "echidna_adapter.py" as Adapter
  component "swc_catalog.py" as Catalog
  component "reporter.py" as Reporter
  component "exceptions.py" as Exceptions
}

Init ..> Runner
Init ..> Normalizer
Init ..> Correlator
Init ..> Adapter
Init ..> Reporter
Init ..> Exceptions

Runner ..> Exceptions
Normalizer ..> Correlator : formato común
Correlator ..> Catalog : tipos SWC
Adapter ..> Catalog : plantillas Echidna
Reporter ..> Correlator : findings correlacionados
Reporter ..> Adapter : metadatos Echidna

@enduml
```

---

# 4. Diagrama de clases UML — Modelo de datos

```plantuml
@startuml
title Modelo lógico de datos de EVMAudit

skinparam shadowing false

class NormalizedReport {
  +tool: str
  +findings: List<NormalizedFinding>
}

class NormalizedFinding {
  +title: str
  +description: str
  +severity: str
  +category: str
  +contract: str
  +function: str
  +location: dict
  +swc_id: str
  +raw: dict
}

class CorrelatedReport {
  +contract: str
  +findings: List<CorrelatedFinding>
}

class CorrelatedFinding {
  +contract: str
  +function: str
  +swc_id: str
  +vuln_type: str
  +severity: str
  +confidence_score: int
  +status: str
  +lines: List<int>
  +confirmed_by: List<str>
  +evidence: dict
}

class AdapterMetadata {
  +wrapper_path: str
  +contract_name_echidna: str
  +vulnerabilities: List<EchidnaVulnerability>
  +testable_count: int
  +non_testable_count: int
  +skipped_count: int
}

class EchidnaVulnerability {
  +swc_id: str
  +function: str
  +confirmed_by: List<str>
  +detectors: List<str>
  +echidna_testable: bool
  +warning: str
}

class FinalReport {
  +meta: dict
  +summary: dict
  +findings: List<CorrelatedFinding>
  +echidna_results: list
}

NormalizedReport "1" o-- "*" NormalizedFinding
CorrelatedReport "1" o-- "*" CorrelatedFinding
AdapterMetadata "1" o-- "*" EchidnaVulnerability
FinalReport "1" o-- "*" CorrelatedFinding

NormalizedFinding --> CorrelatedFinding : correlación
CorrelatedFinding --> EchidnaVulnerability : generación de propiedades

@enduml
```

---

# 5. Diagrama de actividad UML — Correlación

```plantuml
@startuml
title Proceso de correlación de hallazgos

skinparam shadowing false

start

:Recibir reportes normalizados;
:Extraer findings de Slither;
:Extraer findings de Mythril;

:Homogeneizar localización de líneas;
:Construir clave de correlación;

note right
Clave utilizada:
contrato + función + SWC
end note

:Agrupar hallazgos por clave;

repeat
  :Seleccionar grupo de hallazgos;
  :Obtener herramientas que detectaron el hallazgo;

  if (¿Detectado por más de una herramienta?) then (Sí)
    :status = confirmed;
    :confidence_score = 3;
  else (No)
    :status = detected;
    :confidence_score = 2;
  endif

  :Calcular severidad máxima;
  :Unificar líneas afectadas;
  :Fusionar evidencias originales;
  :Crear CorrelatedFinding;

repeat while (¿Quedan grupos?)

:Generar reporte correlacionado;
:Guardar JSON correlacionado;

stop
@enduml
```

---

# 6. Diagrama de secuencia UML — Ejecución completa

```plantuml
@startuml
title Secuencia completa de ejecución de EVMAudit

skinparam shadowing false

actor Usuario
participant "CLI / Web App" as Client
participant "Runner" as Runner
participant "Slither" as Slither
participant "Mythril" as Mythril
participant "Normalizer" as Normalizer
participant "Correlator" as Correlator
participant "Echidna Adapter" as Adapter
participant "SWC Catalog" as Catalog
participant "Echidna" as Echidna
participant "Reporter" as Reporter

Usuario -> Client : Proporcionar contrato Solidity

Client -> Runner : detect_contract_name(contract_path)
Runner --> Client : contract_name

Client -> Runner : run_slither(contract_path)
Runner -> Slither : ejecutar análisis estático
Slither --> Runner : JSON crudo
Runner --> Client : slither_raw

Client -> Runner : run_mythril(contract_path)
Runner -> Mythril : ejecutar ejecución simbólica
Mythril --> Runner : JSON crudo
Runner --> Client : mythril_raw

Client -> Normalizer : normalize_slither_output(slither_raw)
Normalizer --> Client : slither_normalized

Client -> Normalizer : normalize_mythril_output(mythril_raw)
Normalizer --> Client : mythril_normalized

Client -> Correlator : correlate(slither_normalized, mythril_normalized)
Correlator --> Client : correlated_report

Client -> Adapter : generate(correlated_report, contract_path, contract_name)
Adapter -> Catalog : detector_from_swc(swc_id)
Catalog --> Adapter : plantillas disponibles
Adapter --> Client : wrapper + metadata

alt Existe wrapper generado
  Client -> Runner : run_echidna(wrapper_path, contract_name_echidna)
  Runner -> Echidna : ejecutar fuzzing
  Echidna --> Runner : resultados
  Runner --> Client : echidna_raw
else Sin propiedades generadas
  Client -> Client : omitir fuzzing
end

Client -> Reporter : generate_report(contract_path, correlated_report, echidna_raw, metadata)
Reporter --> Client : informe final

Client --> Usuario : Mostrar resultados

@enduml
```

---

# 7. Diagrama de actividad UML — Generación de wrapper Echidna

```plantuml
@startuml
title Generación automática de wrapper para Echidna

skinparam shadowing false

start

:Recibir hallazgos correlacionados;
:Inicializar lista de vulnerabilidades;
:Inicializar contador de omitidas;

repeat
  :Seleccionar hallazgo correlacionado;
  :Extraer SWC;
  :Extraer función afectada;
  :Obtener herramientas confirmadoras;

  :Consultar detectores asociados al SWC;

  if (¿Existen detectores en el catálogo?) then (Sí)
    :Recuperar plantillas Echidna;
    :Evaluar si la vulnerabilidad es testable;

    if (¿Testable automáticamente?) then (Sí)
      :Generar propiedad sin advertencia;
    else (No)
      :Generar propiedad con advertencia;
      :Registrar limitación;
    endif

    :Añadir vulnerabilidad a metadatos;
  else (No)
    :Incrementar skipped_count;
  endif

repeat while (¿Quedan hallazgos?)

if (¿Se generó alguna propiedad?) then (Sí)
  :Construir contrato wrapper;
  :Copiar contrato original al directorio de análisis;
  :Guardar wrapper Solidity;
else (No)
  :No generar wrapper;
endif

:Guardar metadatos del adaptador;

stop
@enduml
```

---

# 8. Diagrama de componentes UML — SWC Catalog y Echidna Adapter

```plantuml
@startuml
title Relación entre SWC Catalog y Echidna Adapter

skinparam componentStyle rectangle
skinparam shadowing false

component "CorrelatedFinding" as Finding {
  [swc_id]
  [function]
  [confirmed_by]
}

component "SWC Catalog" as Catalog {
  [CATALOG]
  [MYTHRIL_TO_DETECTOR]
  [detector_from_swc()]
  [get_template()]
}

component "Echidna Adapter" as Adapter {
  [generate()]
  [_generate_wrapper()]
  [_save_wrapper()]
  [_save_metadata()]
}

artifact "Plantilla Echidna" as Template
artifact "Wrapper Solidity" as Wrapper
artifact "Adapter metadata" as Metadata

Finding --> Adapter : hallazgo correlacionado
Adapter --> Catalog : consultar por swc_id
Catalog --> Template : recuperar plantilla
Template --> Adapter : plantilla parametrizable
Adapter --> Wrapper : generar contrato
Adapter --> Metadata : registrar testabilidad

@enduml
```

---

# 9. Diagrama de clases UML — Gestión de errores

```plantuml
@startuml
title Jerarquía de excepciones de EVMAudit

skinparam shadowing false

class EVMAuditError {
  +mensaje: str
}

class ToolNotFoundError {
  +mensaje: str
}

class AnalysisError {
  +mensaje: str
}

EVMAuditError <|-- ToolNotFoundError
EVMAuditError <|-- AnalysisError

note right of ToolNotFoundError
Se lanza cuando una herramienta externa
no está instalada o no se encuentra en PATH.
end note

note right of AnalysisError
Se lanza cuando una herramienta falla,
cuando se produce un timeout o cuando
no se puede parsear la salida.
end note

@enduml
```

---

# 10. Diagrama de componentes UML — Aplicación web como caso de uso

```plantuml
@startuml
title Aplicación web como caso de uso de EVMAudit

skinparam componentStyle rectangle
skinparam shadowing false

actor Usuario

component "Frontend\nHTML/CSS/JavaScript" as Frontend
component "Backend\nFastAPI" as Backend

component "EVMAudit" as EVMAudit {
  component "Runner" as Runner
  component "Normalizer" as Normalizer
  component "Correlator" as Correlator
  component "Echidna Adapter" as Adapter
  component "Reporter" as Reporter
}

database "Jobs en memoria" as Jobs
folder "jsons/_uploads" as Uploads

artifact "Contrato Solidity" as Contract
artifact "Informe JSON" as Report

Usuario --> Frontend : subir archivo / pegar código

Frontend --> Backend : POST /analyze
Frontend --> Backend : POST /analyze-code

Backend --> Uploads : guardar contrato
Uploads --> Contract

Backend --> Jobs : crear job_id
Backend --> EVMAudit : ejecutar pipeline en segundo plano

EVMAudit --> Report : generar informe

Backend --> Jobs : actualizar estado
Frontend --> Backend : GET /status/{job_id}
Frontend --> Backend : GET /result/{job_id}

Backend --> Frontend : devolver progreso/resultados
Frontend --> Usuario : mostrar informe

@enduml
```

---

# 11. Diagrama de despliegue UML — Aplicación web

```plantuml
@startuml
title Despliegue de la aplicación web EVMAudit

skinparam shadowing false

node "Cliente" {
  artifact "Navegador web" as Browser
}

node "Railway" {
  node "Contenedor de aplicación" {
    component "FastAPI" as FastAPI
    component "Frontend estático" as Static
    component "EVMAudit" as EVMAudit
    component "Slither" as Slither
    component "Mythril" as Mythril
    component "Echidna" as Echidna
    folder "jsons/" as Jsons
  }
}

Browser --> FastAPI : HTTPS
FastAPI --> Static : sirve interfaz
FastAPI --> EVMAudit : invoca análisis
EVMAudit --> Slither
EVMAudit --> Mythril
EVMAudit --> Echidna
EVMAudit --> Jsons : guarda resultados

@enduml
```
