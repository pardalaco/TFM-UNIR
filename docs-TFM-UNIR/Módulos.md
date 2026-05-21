## Módulos

Nuestro paquete/librería evmaudit se organiza en cinco módulos principales, cada uno con responsabilidades claras y funciones específicas que contribuyen al flujo completo de análisis de seguridad de contratos inteligentes:

### Módulo 1: Ejecución de herramientas (runner)

Este módulo se encarga de lanzar las herramientas de análisis (Slither, Mythril, Echidna) sobre los contratos inteligentes. Proporciona funciones para ejecutar cada herramienta individualmente con configuraciones personalizadas, así como una función orquestadora que puede ejecutar todas las herramientas de forma secuencial o paralela y recopilar sus resultados crudos.

Finalmente la salida de estas funciones es un json con la salida cruda de cada herramienta, que luego será procesada por el módulo de normalización. Por ejemplo:

```python
{
    "slither": { ... },  # Salida JSON de Slither
    "mythril": { ... },  # Salida JSON de Mythril
    "echidna": { ... }   # Salida JSON de Echidna
}
```

Este módulo consta de las siguientes funciones:

- run_slither(contract_path, config=None) → dict
- run_mythril(contract_path, timeout=120, depth=22) → dict
- run_echidna(contract_path, config_path=None) → dict

Cada función se encarga de ejecutar la herramienta correspondiente y devolver su salida cruda en formato JSON, que luego será procesada por el módulo de normalización para extraer los hallazgos relevantes.

### Módulo 2: Normalización (normalizer)

Este módulo se encarga de transformar las salidas crudas de cada herramienta en un formato común y estructurado. Cada función de normalización toma la salida JSON de una herramienta específica y extrae los campos relevantes para mapearlos al modelo de datos común.

El resultado es un json con una lista de hallazgos normalizados, cada uno con campos como:
o Vulnerabilidad
o Línea de código
o Severidad
o Evidencia
o Código SWC

Las funciones de este módulo incluyen:

- normalize_slither_output(raw_output)
- normalize_mythril_output(raw_output)
- normalize_echidna_output(raw_output)

Cada función se encarga de procesar la salida de su herramienta correspondiente y devolver una lista de hallazgos normalizados que luego serán correlacionados en el siguiente módulo.

La salida de estos módulos es un json con la siguiente estructura:

```python
{
    "findings": [
        {
            "tool": "slither",
            "title": "Reentrancy vulnerability",
            "description": "The function withdraw() is vulnerable to reentrancy attacks...",
            "severity": "high",
            "category": "execution",
            "location": {"file": "VulnerableBank.sol", "line": 18},
            "swc_id": "SWC-107",
            "raw": { ... }  # Datos adicionales específicos de la herramienta
        },
        ...
    ]
}
```

### Módulo 3: Correlación (correlator)

Este módulo se encarga de juntar los hallazgos normalizados de las diferentes herramientas y detectar aquellos que se refieren a la misma vulnerabilidad o punto del código. Utiliza técnicas de deduplicación y agrupamiento para consolidar hallazgos relacionados, asignarles una puntuación de confianza basada en cuántas herramientas los han confirmado y filtrar aquellos que tienen baja probabilidad de ser verdaderos positivos.

El resultado es un json con hallazgos correlacionados, cada uno con información sobre las herramientas que lo confirmaron, su puntuación de confianza y su estado (confirmado, potencial, falso positivo). Por ejemplo:

```python
{
    "contract": "VulnerableBank",
    "findings": [
      {
        "swc_id": "SWC-107",
        "vuln_type": "reentrancy",
        "severity": "high",
        "confidence_score": 3,
        "status": "confirmed",
        "lines": [15, 18],
        "confirmed_by": ["slither", "mythril"],
        "evidence": {
          "slither": { "check": "reentrancy-eth", "impact": "High" },
          "mythril": { "lineno": 18, "tx_sequence": { ... } }
        }
      }
    ]
  }
```

### Módulo 4: Priorización (prioritizer)

Este módulo se encarga de asignar una puntuación de severidad combinada a cada hallazgo correlacionado, teniendo en cuenta la severidad declarada por las herramientas, la categoría de la vulnerabilidad y la puntuación de confianza asignada en el módulo de correlación. Luego ordena los hallazgos de mayor a menor severidad para facilitar que el auditor centre su atención en los riesgos más relevantes primero. También proporciona funciones para clasificar los hallazgos por categoría (ejecución, control, económicas, lógica de negocio) para facilitar su análisis.

### Módulo 5: Generación de informes (reporter)

Este módulo se encarga de generar informes finales a partir de los hallazgos priorizados. Proporciona funciones para exportar los hallazgos en diferentes formatos (JSON, CSV, HTML, Markdown) y para generar resúmenes ejecutivos que destaquen las vulnerabilidades más críticas y sus implicaciones. También puede incluir recomendaciones de mitigación basadas en las mejores prácticas de seguridad para cada tipo de vulnerabilidad detectada.
