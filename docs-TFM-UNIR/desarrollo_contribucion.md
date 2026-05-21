# 4. Desarrollo específico de la contribución

## 4.1. Tipo 2. Desarrollo de software

### 4.1.1. Identificación de requisitos

El desarrollo de la librería `evmaudit` parte de un conjunto de requisitos funcionales y no funcionales derivados directamente de las limitaciones identificadas en el estado del arte y de los objetivos específicos definidos en el capítulo anterior.

Desde el punto de vista funcional, el sistema debe ser capaz de ejecutar las herramientas de análisis Slither, Mythril y Echidna sobre contratos inteligentes en formato de código fuente Solidity, recopilar sus resultados crudos y procesarlos de forma automatizada. Asimismo, debe transformar dichos resultados a un esquema de datos común que permita operar sobre ellos de forma uniforme con independencia de la herramienta que los haya generado. El sistema debe detectar hallazgos duplicados o relacionados reportados por múltiples herramientas, consolidarlos en grupos coherentes y asignarles una puntuación de confianza basada en el grado de confirmación cruzada. Finalmente, debe presentar los hallazgos ordenados por severidad y exportar el resultado en formatos estructurados adecuados tanto para consumo humano como para integración en pipelines automatizados.

Desde el punto de vista no funcional, se priorizan la modularidad y la extensibilidad, de forma que sea posible incorporar nuevas herramientas de análisis o nuevos formatos de salida sin modificar el núcleo del sistema. La librería debe ejecutarse íntegramente en entornos locales sin dependencias de servicios externos de pago, estar implementada en Python y ser compatible con contratos desarrollados para redes EVM, incluyendo Ethereum mainnet y BNB Smart Chain Testnet como entorno de pruebas principal.

### 4.1.2. Descripción de la herramienta software desarrollada

#### Arquitectura general

La librería `evmaudit` se organiza en torno a una arquitectura de pipeline en capas, en la que cada capa recibe como entrada la salida de la capa anterior y produce un resultado más elaborado y estructurado. Este diseño facilita la separación de responsabilidades, simplifica las pruebas unitarias de cada componente y permite sustituir o ampliar módulos individuales sin afectar al resto del sistema.

El flujo de procesamiento completo puede representarse de la siguiente forma:

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  slither    │   │   mythril   │   │   echidna   │
│  .json      │   │   .json     │   │   .json     │
└──────┬──────┘   └──────┬──────┘   └──────┬──────┘
       │                 │                 │
       ▼                 ▼                 ▼
┌─────────────────────────────────────────────────┐
│              CAPA 1 — Normalización             │
│   Convierte cada output al mismo Finding schema │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│            CAPA 2 — Correlación                 │
│   Agrupa findings por (vuln_type + línea)       │
│   Si 2+ herramientas coinciden → mismo grupo   │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│            CAPA 3 — Scoring                     │
│   Más herramientas coinciden = mayor confianza  │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
                  resultado.json
```

El paquete se estructura en cinco módulos principales que implementan cada una de las fases del pipeline:

- `evmaudit.runner`: ejecución de las herramientas externas y recopilación de salidas crudas.
- `evmaudit.normalizer`: transformación de cada salida cruda al esquema de datos común `Finding`.
- `evmaudit.correlator`: agrupación, deduplicación y scoring de hallazgos cruzados.
- `evmaudit.prioritizer`: ordenación y clasificación por categoría de vulnerabilidad.
- `evmaudit.reporter`: generación de informes en múltiples formatos.

---

#### Módulo 1: Ejecución de herramientas (`evmaudit.runner`)

Este módulo constituye el punto de entrada del pipeline. Su responsabilidad es lanzar las herramientas de análisis externas sobre el contrato objetivo y recopilar sus salidas en formato JSON sin ningún tipo de procesamiento adicional. De este modo, el módulo actúa como una capa de integración que desacopla el resto del sistema de los detalles de invocación de cada herramienta, facilitando futuras incorporaciones de nuevas herramientas sin modificar las capas superiores.

Cada función de este módulo invoca la herramienta correspondiente como subproceso del sistema operativo, captura su salida estándar y de error, gestiona los posibles códigos de retorno anómalos (por ejemplo, timeouts en Mythril o errores de compilación en Slither) y devuelve un diccionario Python con los resultados crudos listos para ser procesados por el módulo de normalización.

Las funciones implementadas en este módulo son las siguientes:

**`run_slither(contract_path: str, config: dict = None) → dict`**

Ejecuta Slither sobre el archivo Solidity especificado en `contract_path` y devuelve su salida en formato JSON. Slither se invoca con la opción `--json -` para obtener la salida estructurada por la salida estándar, evitando así la generación de archivos intermedios. El parámetro `config` permite especificar opciones adicionales de ejecución, como el subconjunto de detectores a activar, la versión del compilador Solidity (`solc`) o la ruta a un archivo de configuración YAML propio de Slither. En caso de que Slither no detecte ninguna vulnerabilidad, la función devuelve igualmente un diccionario con estructura válida y lista de hallazgos vacía, evitando que el pipeline se interrumpa por ausencia de resultados.

```python
resultado = run_slither("contratos/VulnerableBank.sol")
# Devuelve:
{
    "success": true,
    "tool": "slither",
    "raw": { ... }   # Salida JSON completa de Slither
}
```

**`run_mythril(contract_path: str, timeout: int = 120, depth: int = 22) → dict`**

Ejecuta Mythril en modo de análisis de seguridad (`analyze`) sobre el contrato especificado. Los parámetros `timeout` y `depth` permiten controlar respectivamente el tiempo máximo de ejecución y la profundidad de exploración del grafo de estados simbólicos, dos variables críticas para gestionar el problema de explosión de caminos (*path explosion*) descrito en el estado del arte. El valor por defecto de `depth=22` es el recomendado por la documentación oficial de Mythril para contratos de complejidad media. La función detecta automáticamente si la herramienta ha terminado por timeout y lo indica en el campo `status` del resultado devuelto, de forma que las capas posteriores puedan ponderar adecuadamente la confianza de los hallazgos obtenidos bajo análisis incompleto.

```python
resultado = run_mythril("contratos/VulnerableBank.sol", timeout=60, depth=10)
# Devuelve:
{
    "success": true,
    "tool": "mythril",
    "status": "complete",   # O "timeout" si se agotó el tiempo
    "raw": { ... }          # Salida JSON completa de Mythril
}
```

**`run_echidna(contract_path: str, config_path: str = None) → dict`**

Ejecuta Echidna sobre el contrato especificado en modo de fuzzing basado en propiedades. El parámetro opcional `config_path` permite proporcionar un archivo de configuración YAML con parámetros de la campaña de fuzzing, como el número de transacciones a generar, la semilla aleatoria o el nombre del contrato a analizar. Si no se proporciona configuración, la función aplica una configuración por defecto razonable para análisis de propósito general. Dado que Echidna requiere que las propiedades a verificar estén definidas como funciones con el prefijo `echidna_` dentro del propio contrato, esta función es especialmente útil cuando los contratos bajo análisis ya incorporan este tipo de aserciones, siendo complementaria a Slither y Mythril en contratos que no las incluyan.

```python
resultado = run_echidna("contratos/VulnerableBank.sol")
# Devuelve:
{
    "success": true,
    "tool": "echidna",
    "raw": { ... }   # Salida JSON completa de Echidna
}
```

La salida agregada de las tres funciones anteriores constituye el objeto de entrada de la capa de normalización y tiene la siguiente estructura:

```python
{
    "slither": { "success": true, "tool": "slither", "raw": { ... } },
    "mythril":  { "success": true, "tool": "mythril", "status": "complete", "raw": { ... } },
    "echidna":  { "success": true, "tool": "echidna", "raw": { ... } }
}
```

---

#### Módulo 2: Normalización (`evmaudit.normalizer`)

Este módulo implementa la primera capa de transformación del pipeline. Su objetivo es convertir las salidas heterogéneas de Slither, Mythril y Echidna en una lista uniforme de objetos `Finding`, eliminando las diferencias de formato, nomenclatura y nivel de detalle que caracterizan a cada herramienta y que, tal como se describe en el estado del arte, constituyen uno de los principales obstáculos para la correlación automatizada de resultados.

El modelo de datos común `Finding` es una clase de datos Python (`dataclass`) con los siguientes campos obligatorios:

- `tool`: nombre de la herramienta que generó el hallazgo (`"slither"`, `"mythril"` o `"echidna"`).
- `title`: descripción breve del tipo de vulnerabilidad detectada.
- `description`: descripción detallada del hallazgo, incluyendo el contexto de ejecución cuando esté disponible.
- `severity`: nivel de severidad normalizado al esquema común (`"critical"`, `"high"`, `"medium"`, `"low"`, `"informational"`).
- `category`: categoría de vulnerabilidad según la clasificación utilizada en el estado del arte (`"execution"`, `"access_control"`, `"economic"`, `"business_logic"`).
- `location`: diccionario con los campos `file` y `line`, indicando la ubicación exacta del hallazgo en el código fuente.
- `swc_id`: identificador del estándar Smart Contract Weakness Classification (SWC), cuando la herramienta lo proporciona o puede inferirse del tipo de detector.
- `raw`: datos adicionales específicos de la herramienta, preservados íntegramente para consulta posterior.

Las funciones implementadas en este módulo son las siguientes:

**`normalize_slither_output(raw_output: dict) → list[Finding]`**

Procesa la salida JSON de Slither y extrae los hallazgos relevantes. La salida de Slither organiza los resultados en una lista de detectores activados, cada uno con campos como `check` (nombre del detector), `impact` (severidad declarada), `confidence`, `description` y una lista de elementos (`elements`) que identifican las ubicaciones del código afectadas. Esta función itera sobre dicha lista, mapea el campo `impact` al esquema de severidad común (traduciendo, por ejemplo, `"High"` a `"high"`), asigna la categoría de vulnerabilidad correspondiente a partir de una tabla de correspondencia entre nombres de detectores de Slither y las categorías definidas en el trabajo, e infiere el identificador SWC cuando existe un mapeo establecido por la comunidad. En casos donde un mismo detector de Slither reporte múltiples ubicaciones afectadas, la función genera un objeto `Finding` independiente por cada ubicación, facilitando su posterior correlación línea a línea.

**`normalize_mythril_output(raw_output: dict) → list[Finding]`**

Procesa la salida JSON de Mythril, cuya estructura difiere significativamente de la de Slither. Mythril organiza sus resultados como una lista de `issues`, cada uno con campos como `swc-id`, `title`, `description`, `severity`, `lineno` y opcionalmente una secuencia de transacciones (`tx_sequence`) que permite reproducir el exploit. Esta función extrae directamente el `swc_id` cuando está disponible, mapea la severidad al esquema común y construye la ubicación del hallazgo a partir del campo `lineno`. La presencia de la traza de transacciones se incorpora al campo `raw` del objeto `Finding` para que pueda ser consultada en el informe final.

**`normalize_echidna_output(raw_output: dict) → list[Finding]`**

Procesa la salida de Echidna, que reporta las propiedades falsadas durante la campaña de fuzzing junto con la secuencia mínima de transacciones que produce la violación. Dado que Echidna no asigna identificadores SWC ni categorías de vulnerabilidad de forma explícita, esta función infiere la categoría a partir del nombre de la propiedad violada cuando sigue la convención de nomenclatura estándar (`echidna_no_reentrancy`, `echidna_balance_invariant`, etc.), y asigna una severidad por defecto de `"high"` dado que cualquier violación de propiedad representa un comportamiento inesperado confirmado mediante ejecución real del contrato. La secuencia de llamadas que produce la violación se preserva en el campo `raw`.

La salida de este módulo es una lista consolidada de objetos `Finding` de todas las herramientas, con la siguiente representación JSON:

```json
{
    "findings": [
        {
            "tool": "slither",
            "title": "Reentrancy vulnerability",
            "description": "La función withdraw() realiza una llamada externa antes de actualizar el balance interno...",
            "severity": "high",
            "category": "execution",
            "location": { "file": "VulnerableBank.sol", "line": 18 },
            "swc_id": "SWC-107",
            "raw": { ... }
        },
        {
            "tool": "mythril",
            "title": "External Call To User-Supplied Address",
            "description": "Se detecta una llamada externa en un estado en el que el balance no ha sido actualizado...",
            "severity": "high",
            "category": "execution",
            "location": { "file": "VulnerableBank.sol", "line": 18 },
            "swc_id": "SWC-107",
            "raw": { ... }
        }
    ]
}
```

---

#### Módulo 3: Correlación (`evmaudit.correlator`)

Este módulo implementa la segunda capa del pipeline y constituye la contribución técnica central de la librería. Su objetivo es identificar qué hallazgos de distintas herramientas se refieren a la misma vulnerabilidad concreta en el código, agruparlos en un único objeto correlacionado y asignarle una puntuación de confianza proporcional al grado de confirmación cruzada obtenido. Este proceso aborda directamente los problemas de detección redundante y de elevada tasa de falsos positivos identificados como limitaciones del estado del arte.

El principio de funcionamiento del módulo se basa en la hipótesis de que si dos o más herramientas con técnicas de análisis complementarias (análisis estático, ejecución simbólica y fuzzing) coinciden en señalar el mismo tipo de vulnerabilidad en la misma región del código, la probabilidad de que el hallazgo sea un verdadero positivo aumenta significativamente. Esta hipótesis está respaldada por los resultados del estudio empírico de Durieux et al. [26], que demuestra que la tasa de falsos positivos de herramientas individuales como Mythril puede alcanzar el 52%, mientras que la confirmación cruzada entre herramientas reduce considerablemente dicha tasa.

Las funciones implementadas en este módulo son las siguientes:

**`deduplicate_findings(findings: list[Finding]) → list[FindingGroup]`**

Recibe la lista de hallazgos normalizados producida por el módulo anterior e identifica aquellos que se refieren a la misma vulnerabilidad. El criterio de agrupación combina dos dimensiones: el tipo de vulnerabilidad (campo `swc_id` cuando está disponible, o `category` en su defecto) y la proximidad de la ubicación en el código fuente (campo `location.line`). Dos hallazgos se consideran duplicados si comparten el mismo `swc_id` y sus líneas de código se encuentran dentro de un margen de tolerancia configurable (por defecto, ±3 líneas), margen que compensa las diferencias menores en la identificación de líneas entre herramientas que operan sobre el AST (Slither) frente a las que operan sobre el bytecode (Mythril).

El resultado es una lista de objetos `FindingGroup`, cada uno de los cuales agrega todos los hallazgos individuales correspondientes a la misma vulnerabilidad detectada, independientemente de la herramienta que los haya generado.

**`assign_confidence_score(group: FindingGroup) → FindingGroup`**

Calcula y asigna la puntuación de confianza (`confidence_score`) a cada grupo de hallazgos correlacionados. La puntuación se calcula en función del número de herramientas distintas que han confirmado la vulnerabilidad:

- Un hallazgo confirmado únicamente por una herramienta recibe una puntuación de 1, lo que indica baja confianza y mayor probabilidad de ser un falso positivo.
- Si dos herramientas lo han confirmado, la puntuación asciende a 2, indicando confianza moderada.
- Si las tres herramientas coinciden, la puntuación alcanza su valor máximo de 3, indicando alta confianza en la existencia real de la vulnerabilidad.

Adicionalmente, la función pondera la combinación de herramientas que confirman el hallazgo: la coincidencia entre Slither (análisis estático) y Mythril (ejecución simbólica) se considera especialmente significativa al tratarse de técnicas complementarias que operan a distintos niveles de abstracción. La puntuación final puede extenderse en el futuro para incorporar factores adicionales como la severidad declarada o la especificidad del detector activado.

**`correlate_findings(findings: list[Finding]) → list[FindingGroup]`**

Función orquestadora que combina internamente `deduplicate_findings` y `assign_confidence_score`, devolviendo directamente la lista de grupos correlacionados con sus puntuaciones de confianza asignadas. Es la función principal de este módulo en el uso típico de la librería.

La salida del módulo de correlación tiene la siguiente estructura JSON:

```json
{
    "contract": "VulnerableBank",
    "findings": [
        {
            "swc_id": "SWC-107",
            "vuln_type": "reentrancy",
            "severity": "high",
            "confidence_score": 2,
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

El campo `status` puede tomar los valores `"confirmed"` (dos o más herramientas), `"potential"` (una única herramienta) o `"low_confidence"` (cuando la herramienta que lo reporta tiene una tasa de falsos positivos históricamente elevada para ese tipo de detector concreto, según la tabla de referencia incorporada en el módulo).

---

#### Módulo 4: Priorización (`evmaudit.prioritizer`)

Este módulo implementa la tercera capa del pipeline y tiene como objetivo ordenar los hallazgos correlacionados de mayor a menor relevancia para el auditor, facilitando que los riesgos más críticos sean atendidos en primer lugar. Para ello, combina dos dimensiones de evaluación: la severidad intrínseca de la vulnerabilidad y la confianza en que el hallazgo es un verdadero positivo.

Las funciones implementadas en este módulo son las siguientes:

**`calculate_severity_score(group: FindingGroup) → float`**

Calcula una puntuación numérica de severidad combinada para cada grupo de hallazgos correlacionados. La puntuación se obtiene a partir de dos factores. El primero es la severidad normalizada del hallazgo, codificada numéricamente como `critical=4`, `high=3`, `medium=2`, `low=1` e `informational=0`. El segundo es la puntuación de confianza asignada por el módulo de correlación, normalizada al rango [0, 1] dividiéndola entre el valor máximo posible (3). La puntuación combinada se calcula como el producto de ambos factores, lo que produce una escala continua en el rango [0, 4] que pondera conjuntamente la gravedad potencial y la fiabilidad del hallazgo. Un hallazgo crítico confirmado por tres herramientas obtendrá la puntuación máxima de 4.0, mientras que un hallazgo de severidad media reportado por una sola herramienta obtendrá una puntuación de aproximadamente 0.67, reflejando la incertidumbre asociada.

**`rank_findings(groups: list[FindingGroup]) → list[FindingGroup]`**

Ordena la lista de grupos de hallazgos de mayor a menor puntuación de severidad combinada. En caso de empate en la puntuación, los hallazgos se ordenan secundariamente por el número de herramientas que los han confirmado y, en tercer lugar, alfabéticamente por el identificador SWC para garantizar un orden determinista en la salida. El resultado es una lista ordenada que permite al auditor abordar los hallazgos en el orden de prioridad más adecuado.

**`classify_by_category(groups: list[FindingGroup]) → dict[str, list[FindingGroup]]`**

Organiza los hallazgos en un diccionario indexado por las cuatro categorías de vulnerabilidad definidas en el estado del arte: `"execution"` para vulnerabilidades técnicas de ejecución (reentrancy, overflow, delegatecall inseguro, DoS), `"access_control"` para problemas de control y privilegios (funciones sin restricciones, uso de tx.origin, inicialización insegura), `"economic"` para vulnerabilidades económicas y de dependencia del entorno (front-running, manipulación de oráculos, block.timestamp) y `"business_logic"` para errores lógicos de negocio (cálculos incorrectos de balances, distribución de recompensas, estados inconsistentes). Esta clasificación facilita el análisis estructurado por parte del auditor y permite generar secciones temáticas en el informe final.

---

#### Módulo 5: Generación de informes (`evmaudit.reporter`)

Este módulo constituye la capa de salida del pipeline y se encarga de transformar los hallazgos priorizados en informes consumibles. Su diseño tiene en cuenta dos perfiles de uso diferenciados: por un lado, auditores de seguridad que necesitan un documento estructurado y legible con contexto suficiente para validar y remediar cada hallazgo; por otro, sistemas automatizados de CI/CD que consumen los resultados como datos estructurados para integrarse en flujos de revisión de código.

Las funciones implementadas en este módulo son las siguientes:

**`generate_summary(groups: list[FindingGroup]) → dict`**

Produce un resumen ejecutivo en forma de diccionario Python con los siguientes campos: número total de hallazgos, desglose por severidad (`critical`, `high`, `medium`, `low`, `informational`), desglose por categoría de vulnerabilidad, desglose por herramienta origen y una puntuación global de riesgo del contrato calculada como la media ponderada de las puntuaciones de severidad combinada de todos los hallazgos, expresada en una escala de 0 a 100. Este resumen está concebido para proporcionar una visión inmediata del estado de seguridad del contrato antes de descender al detalle de cada hallazgo individual.

```json
{
    "total_findings": 5,
    "by_severity": { "critical": 0, "high": 2, "medium": 2, "low": 1, "informational": 0 },
    "by_category": { "execution": 2, "access_control": 1, "economic": 1, "business_logic": 1 },
    "by_tool": { "slither": 4, "mythril": 3, "echidna": 1 },
    "risk_score": 68.4
}
```

**`generate_report(groups: list[FindingGroup], format: str = "json", output_path: str = None) → str`**

Genera el informe completo de auditoría a partir de los hallazgos priorizados. El parámetro `format` controla el formato de salida: `"json"` produce un objeto JSON estructurado con todos los grupos de hallazgos y su metadatos completos; `"markdown"` produce un documento Markdown con secciones por categoría de vulnerabilidad, tablas de hallazgos ordenados por prioridad y bloques de código que ilustran la ubicación de cada vulnerabilidad; `"csv"` produce un archivo de valores separados por comas adecuado para su importación en hojas de cálculo o herramientas de gestión de vulnerabilidades. Si se proporciona `output_path`, el informe se escribe en disco en la ruta indicada; en caso contrario, se devuelve como cadena de texto. El informe en formato Markdown incluye, para cada hallazgo, una descripción de la vulnerabilidad, la evidencia aportada por cada herramienta confirmante, la ubicación exacta en el código y una recomendación de mitigación basada en las mejores prácticas descritas en el Anexo A del presente trabajo.

**`export_to_sarif(groups: list[FindingGroup], output_path: str) → None`**

Exporta los hallazgos al formato estándar SARIF 2.1.0 (*Static Analysis Results Interchange Format*), especificación abierta mantenida por OASIS que es reconocida de forma nativa por plataformas de revisión de código como GitHub Code Scanning y Azure DevOps. Este formato permite presentar los hallazgos directamente en la interfaz de revisión de código de los repositorios, anotando las líneas afectadas con los problemas detectados. Su inclusión en la librería responde al objetivo de facilitar la integración de `evmaudit` en flujos de trabajo de DevSecOps, posibilitando el análisis automático de contratos en cada *pull request* antes de su despliegue.

---

### 4.1.3. Evaluación

La evaluación de la librería se realizará en dos fases complementarias: una fase de validación funcional sobre contratos con vulnerabilidades conocidas y una fase de evaluación comparativa sobre contratos reales de código abierto desplegados en BNB Smart Chain Testnet.

En la fase de validación funcional se utilizarán los contratos del Anexo A del presente trabajo, diseñados específicamente para contener vulnerabilidades representativas de cada una de las cuatro categorías definidas. Para cada contrato vulnerable se verificará que la librería detecta y prioriza correctamente las vulnerabilidades esperadas, que el módulo de correlación agrupa adecuadamente los hallazgos redundantes y que la puntuación de confianza asignada es coherente con el número de herramientas que los confirman.

En la fase de evaluación comparativa se seleccionarán contratos reales de código abierto, incluyendo implementaciones simplificadas de protocolos DeFi y contratos de tokens ERC-20, para comparar los resultados de la librería con los obtenidos ejecutando cada herramienta de forma independiente. Se medirá la reducción en el número de hallazgos presentados al auditor (como indicador de la efectividad de la deduplicación), la proporción de hallazgos confirmados por múltiples herramientas frente a hallazgos reportados por una sola (como indicador de la reducción de falsos positivos) y la consistencia de la priorización con evaluaciones manuales de referencia realizadas sobre un subconjunto de contratos.
