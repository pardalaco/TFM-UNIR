# Funciones de la librería

## Módulo 1: Ejecución de herramientas (`runner`)

**`run_slither(contract_path, config=None) → dict`**
Ejecuta Slither sobre un contrato Solidity especificado y devuelve los resultados crudos en formato estructurado. Acepta configuración opcional (detectores a activar, severidad mínima, versión del compilador).

**`run_mythril(contract_path, timeout=120, depth=22) → dict`**
Lanza Mythril en modo de ejecución simbólica sobre el contrato indicado. Controla el timeout y la profundidad de exploración para gestionar el problema de path explosion descrito en el estado del arte.

**`run_echidna(contract_path, config_path=None) → dict`**
Ejecuta Echidna en modo fuzzing sobre el contrato. Si no se proporciona configuración, usa valores por defecto razonables. Devuelve las propiedades violadas y las secuencias mínimas de transacciones que las rompen.

**`run_all(contract_path, tools=["slither","mythril","echidna"]) → dict`**
Orquestador que lanza todas las herramientas configuradas de forma secuencial (o paralela) y agrega sus salidas crudas en un único diccionario indexado por herramienta.

---

## Módulo 2: Normalización (`normalizer`)

**`normalize_slither_output(raw_output) → list[Finding]`**
Convierte la salida JSON de Slither al modelo de datos interno `Finding`, mapeando campos como detector name, severity, description y location a un esquema común.

**`normalize_mythril_output(raw_output) → list[Finding]`**
Equivalente para Mythril. Extrae los campos relevantes del JSON de Mythril (SWC ID, description, tx sequence) y los transforma al mismo esquema `Finding`.

**`normalize_echidna_output(raw_output) → list[Finding]`**
Transforma los resultados de Echidna (propiedades falsadas y call sequences) al modelo común, marcándolos con su categoría de vulnerabilidad correspondiente.

**`Finding` (dataclass)**
Estructura de datos común con campos: `tool`, `title`, `description`, `severity`, `category`, `location` (archivo + línea), `swc_id`, `raw`. Sobre este modelo opera todo el resto de la librería.

---

## Módulo 3: Correlación (`correlator`)

**`deduplicate_findings(findings: list[Finding]) → list[Finding]`**
Detecta hallazgos duplicados reportados por varias herramientas sobre el mismo punto del código (misma ubicación + misma categoría) y los colapsa en un único `Finding` enriquecido con las fuentes que lo confirmaron.

**`correlate_findings(findings: list[Finding]) → list[FindingGroup]`**
Agrupa hallazgos relacionados aunque no idénticos (por ejemplo, una dependencia de oracle detectada por Slither y un flash loan path detectado por Mythril en el mismo contrato) en `FindingGroup`, facilitando la comprensión de vulnerabilidades compuestas.

**`assign_confidence_score(finding: Finding, sources: list[str]) → float`**
Calcula una puntuación de confianza (0.0–1.0) para cada hallazgo en función de cuántas herramientas lo han confirmado y la complementariedad de sus técnicas de análisis (estático + simbólico + fuzzing).

**`filter_false_positives(findings: list[Finding], threshold=0.4) → list[Finding]`**
Filtra hallazgos con baja puntuación de confianza que tienen mayor probabilidad de ser falsos positivos, especialmente relevante dado que Mythril presenta tasas del 45–52% según el estado del arte.

---

## Módulo 4: Priorización (`prioritizer`)

**`calculate_severity_score(finding: Finding) → float`**
Calcula una puntuación numérica de severidad combinando la severidad declarada por la herramienta, la categoría de la vulnerabilidad (crítica/alta/media/baja) y la puntuación de confianza asignada.

**`rank_findings(findings: list[Finding]) → list[Finding]`**
Ordena los hallazgos de mayor a menor severidad combinada, produciendo una lista priorizada que facilita que el auditor centre su atención en los riesgos más relevantes primero.

**`classify_by_category(findings: list[Finding]) → dict[str, list[Finding]]`**
Agrupa los hallazgos según las cuatro categorías definidas en el trabajo: vulnerabilidades técnicas de ejecución, de control y privilegios, económicas y errores lógicos de negocio.

---

## Módulo 5: Análisis del contrato (`analyzer`)

**`extract_contract_metadata(contract_path) → ContractMetadata`**
Extrae metadatos estáticos del contrato: nombre, versión de Solidity, funciones públicas, modificadores, eventos, dependencias de herencia y uso de patrones conocidos (ReentrancyGuard, Ownable, etc.).

**`detect_upgrade_patterns(contract_path) → list[str]`**
Identifica si el contrato implementa patrones de actualización (proxy UUPS, Transparent Proxy, EIP-1967) y advierte sobre posibles riesgos de inicialización insegura, relevante dado el caso Poly Network analizado.

**`check_known_vulnerable_patterns(contract_path) → list[Finding]`**
Aplica un conjunto de reglas propias (independientes de Slither/Mythril) para detectar patrones de código directamente asociados a las vulnerabilidades del Anexo A: uso de `tx.origin`, `block.timestamp` como aleatoriedad, `transfer` en bucles, etc.

---

## Módulo 6: Generación de informes (`reporter`)

**`generate_report(findings: list[Finding], format="json") → str`**
Genera un informe completo de los hallazgos normalizados y priorizados. Soporta formatos JSON (para integración en pipelines) y Markdown (para lectura humana).

**`generate_summary(findings: list[Finding]) → dict`**
Produce un resumen ejecutivo con conteos por severidad, por categoría, por herramienta y una puntuación global de riesgo del contrato (0–100).

**`export_to_sarif(findings: list[Finding], output_path) → None`**
Exporta los hallazgos al formato estándar SARIF (Static Analysis Results Interchange Format), lo que permite la integración directa con plataformas de CI/CD como GitHub Actions y herramientas de revisión de código.

---

## Módulo 7: API principal (`evmaudit`)

**`audit_contract(contract_path, tools=None, output_format="json") → AuditResult`**
Función principal de alto nivel que orquesta todo el pipeline: ejecución de herramientas → normalización → correlación → priorización → generación de informe. Devuelve un objeto `AuditResult` con todos los hallazgos procesados y el informe generado.

**`load_contract_from_address(address, rpc_url) → str`**
Recupera el bytecode de un contrato ya desplegado en red (Ethereum mainnet, BNB Smart Chain Testnet u otras EVM-compatibles) a partir de su dirección, permitiendo auditar contratos sin acceso al código fuente.

**`compare_audits(audit_a: AuditResult, audit_b: AuditResult) → dict`**
Compara dos resultados de auditoría del mismo contrato (por ejemplo, antes y después de una actualización) e identifica vulnerabilidades nuevas, resueltas o persistentes.
