Aquí tienes los diagramas en **PlantUML** listos para pegar.

## 1. Arquitectura general

```plantuml
@startuml
title Arquitectura general de EVMAudit

skinparam componentStyle rectangle

actor Usuario

component "EVMAudit" {
  component "Runner" as Runner
  component "Normalizer" as Normalizer
  component "Correlator" as Correlator
  component "SWC Catalog" as Catalog
  component "Echidna Adapter" as Adapter
  component "Reporter" as Reporter
}

component "Slither" as Slither
component "Mythril" as Mythril
component "Echidna" as Echidna
artifact "Informe final" as Report

Usuario --> Runner
Runner --> Slither
Runner --> Mythril
Slither --> Normalizer
Mythril --> Normalizer
Normalizer --> Correlator
Correlator --> Catalog
Catalog --> Adapter
Adapter --> Echidna
Echidna --> Reporter
Correlator --> Reporter
Reporter --> Report

@enduml
```

## 2. Pipeline de análisis

```plantuml
@startuml
title Pipeline de análisis de EVMAudit

start

:Recibir contrato Solidity;
:Detectar nombre del contrato;
:Configurar versión de Solidity;

:Ejecutar Slither;
:Ejecutar Mythril;

:Normalizar resultados;
:Correlacionar hallazgos;

:Consultar catálogo SWC;
:Generar wrapper Solidity para Echidna;

if (¿Existen propiedades generadas?) then (Sí)
  :Ejecutar Echidna;
else (No)
  :Omitir fase de fuzzing;
endif

:Generar informe final;

stop
@enduml
```

## 3. Diagrama de paquetes

```plantuml
@startuml
title Estructura modular del paquete EVMAudit

package "evmaudit" {
  package "runner.py" as Runner
  package "normalizer.py" as Normalizer
  package "correlator.py" as Correlator
  package "echidna_adapter.py" as Adapter
  package "swc_catalog.py" as Catalog
  package "reporter.py" as Reporter
  package "exceptions.py" as Exceptions
  package "__init__.py" as Init
}

Init --> Runner
Init --> Normalizer
Init --> Correlator
Init --> Adapter
Init --> Reporter
Init --> Exceptions

Runner --> Exceptions
Normalizer --> Correlator
Correlator --> Catalog
Adapter --> Catalog
Reporter --> Correlator
Reporter --> Adapter

@enduml
```

## 4. Modelo de hallazgo normalizado

```plantuml
@startuml
title Modelo de datos de hallazgos

class NormalizedReport {
  +tool: str
  +findings: List<Finding>
}

class Finding {
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

NormalizedReport "1" --> "*" Finding
Finding --> CorrelatedFinding : correlación

@enduml
```

## 5. Proceso de correlación

```plantuml
@startuml
title Proceso de correlación de hallazgos

start

:Recibir resultados normalizados;
:Extraer findings de Slither;
:Extraer findings de Mythril;

:Construir clave de correlación;
note right
Clave:
contrato + función + SWC
end note

:Agrupar hallazgos equivalentes;

if (¿Detectado por varias herramientas?) then (Sí)
  :Asignar status = confirmed;
  :Asignar confidence_score = 3;
else (No)
  :Asignar status = detected;
  :Asignar confidence_score = 2;
endif

:Seleccionar severidad máxima;
:Unificar líneas afectadas;
:Preservar evidencias originales;
:Generar hallazgo correlacionado;

stop
@enduml
```

## 6. Secuencia completa

```plantuml
@startuml
title Secuencia completa de ejecución

actor Usuario
participant "main.py / API" as Main
participant "Runner" as Runner
participant "Slither" as Slither
participant "Mythril" as Mythril
participant "Normalizer" as Normalizer
participant "Correlator" as Correlator
participant "Echidna Adapter" as Adapter
participant "Echidna" as Echidna
participant "Reporter" as Reporter

Usuario -> Main : Enviar contrato Solidity
Main -> Runner : detect_contract_name()
Main -> Runner : run_slither()
Runner -> Slither : Ejecutar análisis estático
Slither --> Runner : JSON crudo

Main -> Runner : run_mythril()
Runner -> Mythril : Ejecutar ejecución simbólica
Mythril --> Runner : JSON crudo

Main -> Normalizer : normalize_slither_output()
Main -> Normalizer : normalize_mythril_output()
Normalizer --> Main : Resultados normalizados

Main -> Correlator : correlate()
Correlator --> Main : Hallazgos correlacionados

Main -> Adapter : generate_echidna_wrapper()
Adapter --> Main : Wrapper + metadatos

alt Wrapper generado
  Main -> Runner : run_echidna()
  Runner -> Echidna : Ejecutar fuzzing
  Echidna --> Runner : Resultados fuzzing
end

Main -> Reporter : generate_report()
Reporter --> Main : Informe final
Main --> Usuario : Mostrar resultados

@enduml
```

## 7. Generación de wrapper Echidna

```plantuml
@startuml
title Generación de wrapper para Echidna

start

:Recibir hallazgos correlacionados;

repeat
  :Extraer SWC del hallazgo;
  :Consultar catálogo SWC;
  
  if (¿Existe plantilla?) then (Sí)
    :Obtener plantilla Echidna;
    :Sustituir función vulnerable;
    
    if (¿Vulnerabilidad testable?) then (Sí)
      :Añadir propiedad al wrapper;
    else (No)
      :Añadir propiedad con advertencia;
      :Marcar como no testable;
    endif
    
  else (No)
    :Marcar hallazgo como omitido;
  endif

repeat while (¿Quedan hallazgos?)

:Construir contrato wrapper;
:Guardar wrapper Solidity;
:Guardar metadatos;

stop
@enduml
```

## 8. Relación SWC Catalog y Echidna Adapter

```plantuml
@startuml
title Relación entre SWC Catalog y Echidna Adapter

component "Correlated Finding" as Finding {
  [swc_id]
  [function]
  [confirmed_by]
}

component "SWC Catalog" as Catalog {
  [SWC]
  [Título]
  [Impacto]
  [Plantilla]
  [Limitación]
  [echidna_testable]
}

component "Echidna Adapter" as Adapter
artifact "Wrapper Solidity" as Wrapper
component "Echidna" as Echidna

Finding --> Adapter
Adapter --> Catalog : consultar plantilla por SWC
Catalog --> Adapter : devolver plantilla
Adapter --> Wrapper : generar contrato
Wrapper --> Echidna : ejecutar fuzzing

@enduml
```

## 9. Gestión de errores

```plantuml
@startuml
title Jerarquía de excepciones de EVMAudit

class EVMAuditError {
  Excepción base del paquete
}

class ToolNotFoundError {
  Herramienta externa no instalada
  o no localizada en PATH
}

class AnalysisError {
  Error crítico durante
  el análisis
}

EVMAuditError <|-- ToolNotFoundError
EVMAuditError <|-- AnalysisError

@enduml
```

## 10. Aplicación web como caso de uso

```plantuml
@startuml
title Aplicación web como caso de uso de EVMAudit

actor Usuario

component "Frontend\nHTML/CSS/JS" as Frontend
component "Backend\nFastAPI" as Backend
component "EVMAudit" as EVMAudit
database "Jobs en memoria" as Jobs
artifact "Contrato Solidity" as Contract
artifact "Informe JSON" as Report

Usuario --> Frontend : Subir archivo o pegar código
Frontend --> Backend : POST /analyze
Backend --> Contract : guardar contrato
Backend --> Jobs : crear job_id
Backend --> EVMAudit : ejecutar pipeline
EVMAudit --> Report : generar informe
Backend --> Jobs : actualizar estado
Frontend --> Backend : GET /status/{job_id}
Frontend --> Backend : GET /result/{job_id}
Backend --> Frontend : devolver resultados
Frontend --> Usuario : mostrar informe

@enduml
```

## 11. Despliegue web

```plantuml
@startuml
title Despliegue de la aplicación web

node "Cliente web" {
  artifact "Navegador" as Browser
}

node "Railway" {
  node "Contenedor aplicación" {
    component "FastAPI" as FastAPI
    component "EVMAudit" as EVMAudit
    component "Slither" as Slither
    component "Mythril" as Mythril
    component "Echidna" as Echidna
  }
}

Browser --> FastAPI : HTTPS
FastAPI --> EVMAudit
EVMAudit --> Slither
EVMAudit --> Mythril
EVMAudit --> Echidna

@enduml
```
