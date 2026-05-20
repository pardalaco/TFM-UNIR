# Ejecución y Formato de Resultados — Slither, Mythril, Echidna

## Contratos de prueba utilizados

Se han diseñado 3 contratos Solidity, cada uno con una vulnerabilidad distinta e intencionada:

| Fichero | Contrato | Vulnerabilidad |
|---|---|---|
| `Reentrancy.sol` | `VulnerableBank` | Reentrancy: llamada externa antes de actualizar estado |
| `UncheckedArithmetic.sol` | `UnsafeCounter` | Overflow/underflow silencioso con `unchecked` |
| `AccessControl.sol` | `Vault` | Control de acceso: cualquiera puede vaciar el contrato |

```solidity
// Reentrancy.sol — patrón vulnerable clásico
function withdraw(uint256 amount) external {
    require(balances[msg.sender] >= amount, "Saldo insuficiente");
    (bool success, ) = msg.sender.call{value: amount}("");  // ← llamada ANTES de actualizar
    require(success, "Fallo al enviar ether");
    balances[msg.sender] -= amount;                         // ← estado actualizado DESPUÉS
}
```

```solidity
// UncheckedArithmetic.sol — overflow silencioso
function increment(uint256 amount) external {
    unchecked { counter += amount; }  // ← sin protección de desbordamiento
}
```

```solidity
// AccessControl.sol — sin restricción de acceso
function sweep(address payable to) external {
    to.transfer(address(this).balance);  // ← cualquier dirección puede llamar
}
```

---

## 1. Slither — Análisis estático

### Qué hace
Analiza el bytecode/AST del contrato **sin ejecutarlo**. Detecta patrones de vulnerabilidad conocidos mediante detectores predefinidos. Muy rápido (segundos).

### Comando de ejecución

```bash
slither contracts/Reentrancy.sol --json outputs/slither_reentrancy.json
slither contracts/UncheckedArithmetic.sol --json outputs/slither_arithmetic.json
slither contracts/AccessControl.sol --json outputs/slither_access.json
```

### Formato del resultado (JSON)

```json
{
  "success": true,
  "error": null,
  "results": {
    "detectors": [
      {
        "check": "reentrancy-eth",
        "impact": "High",
        "confidence": "Medium",
        "description": "VulnerableBank.withdraw(uint256) ...",
        "elements": [
          {
            "type": "function",
            "name": "withdraw",
            "source_mapping": {
              "filename_short": "contracts/Reentrancy.sol",
              "lines": [11, 12, 13, 14, 15, 16, 17, 18, 19]
            }
          }
        ]
      }
    ]
  }
}
```

### Campos clave

| Campo | Descripción |
|---|---|
| `check` | ID del detector (ej. `reentrancy-eth`, `solc-version`) |
| `impact` | Severidad: `High` / `Medium` / `Low` / `Informational` |
| `confidence` | Confianza en el hallazgo: `High` / `Medium` / `Low` |
| `description` | Explicación en texto de la vulnerabilidad |
| `elements[].source_mapping.lines` | Líneas del contrato donde se detecta |

### Resultado real sobre `Reentrancy.sol`
Slither detectó reentrancy en la función `withdraw` (líneas 11–19) con impacto **High**. También detectó lectura/escritura de estado tras llamada externa.

---

## 2. Mythril — Análisis simbólico

### Qué hace
Ejecuta el contrato de forma **simbólica**: simula todas las rutas posibles de ejecución mediante un motor SMT (Z3). Puede demostrar formalmente que una vulnerabilidad es alcanzable. Más lento (minutos).

### Comando de ejecución

```bash
myth analyze contracts/Reentrancy.sol \
  --solv 0.8.20 \
  --execution-timeout 60 \
  -o json > outputs/mythril_reentrancy.json

myth analyze contracts/UncheckedArithmetic.sol \
  --solv 0.8.20 \
  --execution-timeout 60 \
  -o json > outputs/mythril_arithmetic.json

myth analyze contracts/AccessControl.sol \
  --solv 0.8.20 \
  --execution-timeout 60 \
  -o json > outputs/mythril_access.json
```

### Formato del resultado (JSON)

```json
{
  "error": null,
  "success": true,
  "issues": [
    {
      "title": "State access after external call",
      "swc-id": "107",
      "severity": "Medium",
      "contract": "VulnerableBank",
      "function": "withdraw(uint256)",
      "filename": "contracts/Reentrancy.sol",
      "lineno": 18,
      "description": "The contract account state is accessed after an external call...",
      "code": "balances[msg.sender] -= amount",
      "min_gas_used": 8487,
      "max_gas_used": 63431,
      "tx_sequence": { ... }
    }
  ]
}
```

### Campos clave

| Campo | Descripción |
|---|---|
| `title` | Nombre del tipo de vulnerabilidad |
| `swc-id` | ID del estándar SWC (Smart Contract Weakness Classification) |
| `severity` | `High` / `Medium` / `Low` |
| `function` | Función afectada |
| `lineno` | Línea exacta del problema |
| `code` | Fragmento de código vulnerable |
| `tx_sequence` | Secuencia de transacciones que reproduce el exploit |
| `min/max_gas_used` | Gas consumido en la transacción maliciosa |

### Resultado real sobre `Reentrancy.sol`
Mythril encontró **3 issues** en `withdraw()`:
- Línea 15: llamada externa a dirección suministrada por el usuario (SWC-107, Low)
- Línea 18: lectura de estado tras llamada externa (SWC-107, Medium)
- Línea 18: escritura de estado tras llamada externa (SWC-107, Medium)

---

## 3. Echidna — Fuzzing basado en propiedades

### Qué hace
Genera inputs aleatorios masivamente para intentar **violar propiedades** que el desarrollador define. El tester escribe invariantes (`echidna_*`) que deben cumplirse siempre; Echidna trata de encontrar un caso que las rompa.

### Contrato de prueba (requiere contrato especial)

```solidity
// EchidnaTest.sol
contract EchidnaTest is UnsafeCounter {

    // Propiedad que Echidna intentará violar:
    // el contador no debería superar 2^128 si el uso es normal
    function echidna_counter_stays_bounded() public view returns (bool) {
        return counter < 2**128;
    }

    // Esta propiedad es trivialmente verdadera (benchmark):
    function echidna_counter_no_underflow() public view returns (bool) {
        return counter <= type(uint256).max;
    }
}
```

### Comando de ejecución

```bash
# Ejecución con output JSON
echidna contracts/EchidnaTest.sol \
  --contract EchidnaTest \
  --format json \
  --test-limit 10000 \
  > outputs/echidna_arithmetic.json

# Ejecución con output legible (texto)
echidna contracts/EchidnaTest.sol \
  --contract EchidnaTest \
  --test-limit 10000 \
  2>&1 | tee outputs/echidna_arithmetic_summary.txt
```

### Formato del resultado (texto — más legible)

```
[2026-05-18 11:09:41] [status] tests: 1/2, fuzzing: 10152/10000, cov: 253

echidna_counter_no_underflow: passing
echidna_counter_stays_bounded: failed! 💥
  Call sequence:
    EchidnaTest.increment(341078997830925091125591174416463107352)

Unique instructions: 253
Corpus size: 4
Seed: 239813294802217856
Total calls: 10152
```

### Formato del resultado (JSON)

```json
{
  "success": true,
  "error": null,
  "seed": 239813294802217856,
  "tests": [
    {
      "name": "echidna_counter_no_underflow",
      "status": "fuzzing",
      "transactions": null,
      "type": "property"
    },
    {
      "name": "echidna_counter_stays_bounded",
      "status": "shrinking",
      "transactions": [
        {
          "function": "decrement",
          "arguments": ["1"],
          "gas": "12500000",
          "value": "0x0"
        }
      ],
      "type": "property"
    }
  ],
  "coverage": { ... }
}
```

### Campos clave

| Campo | Descripción |
|---|---|
| `tests[].name` | Nombre de la propiedad (`echidna_*`) |
| `tests[].status` | `passing` / `failed` / `shrinking` / `fuzzing` |
| `tests[].transactions` | Secuencia mínima que rompe la propiedad (tras shrinking) |
| `seed` | Semilla usada — permite reproducir la ejecución exacta |
| `coverage` | Mapa de cobertura de bytecode |

### Resultado real sobre `EchidnaTest.sol`
- `echidna_counter_no_underflow`: **passing** (trivialmente verdadera)
- `echidna_counter_stays_bounded`: **failed** con `increment(341078997830925091...)` — un solo incremento masivo desborda el límite de 2^128

---

## Resumen comparativo

| | Slither | Mythril | Echidna |
|---|---|---|---|
| **Técnica** | Análisis estático | Ejecución simbólica | Fuzzing |
| **Velocidad** | Segundos | Minutos | Minutos–Horas |
| **Falsos positivos** | Altos | Bajos | Muy bajos |
| **Requiere ejecución** | No | Simulada | Sí (EVM) |
| **Output principal** | `detectors[]` | `issues[]` | `tests[]` |
| **Severidad** | `impact` + `confidence` | `severity` + `swc-id` | passed/failed |
| **Localización** | `source_mapping.lines` | `lineno` + `code` | `transactions` (call sequence) |

## Capa Python de integración — Arquitectura

La idea principal tiene tres pasos bien separados: **normalizar → correlacionar → puntuar**.

---

### El problema central

Cada herramienta habla un idioma distinto:

| | Tipo de hallazgo | Localización | Severidad |
|---|---|---|---|
| **Slither** | `detectors[].check` | `source_mapping.lines[]` | `impact` + `confidence` |
| **Mythril** | `issues[].swc-id` | `lineno` | `severity` |
| **Echidna** | `tests[].status` | `transactions` (call sequence) | `passed` / `failed` |

No se pueden mezclar directamente — hay que normalizarlos primero.

---

### Arquitectura propuesta

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

---

### Capa 1: Schema común (`Finding`)

```python
@dataclass
class Finding:
    tool: str          # "slither" | "mythril" | "echidna"
    vuln_type: str     # tipo normalizado, ej. "reentrancy"
    swc_id: str        # ej. "SWC-107" (mapeado desde Slither si hace falta)
    severity: str      # "high" | "medium" | "low" | "info"
    confidence: str    # "high" | "medium" | "low"
    file: str
    lines: list[int]
    description: str
    evidence: dict     # raw: tx_sequence, code snippet, etc.
```

El truco está en el **mapeo de Slither → SWC**, porque Mythril ya lo da y Slither no:

```python
SLITHER_TO_SWC = {
    "reentrancy-eth":      "SWC-107",
    "arbitrary-send-eth":  "SWC-105",
    "suicidal":            "SWC-106",
    "unchecked-lowlevel":  "SWC-104",
    ...
}
```

---

### Capa 2: Correlación

Dos findings se consideran el mismo si coinciden en `swc_id` y están en líneas solapadas (±3 líneas de margen):

```python
def same_finding(a: Finding, b: Finding) -> bool:
    same_vuln = a.swc_id == b.swc_id
    overlap   = set(a.lines) & set(b.lines)  # o distancia < 3
    return same_vuln and (bool(overlap) or a.file == b.file)
```

---

### Capa 3: Scoring

La confianza final sube según cuántas herramientas confirman el mismo hallazgo:

```python
TOOL_WEIGHTS = {"slither": 1, "mythril": 2, "echidna": 3}
# Echidna pesa más porque demuestra explotabilidad real

def score(group: list[Finding]) -> float:
    return sum(TOOL_WEIGHTS[f.tool] for f in group)

# score >= 5 → confirmed  (2+ herramientas)
# score == 3 → probable   (solo Echidna)
# score == 2 → candidate  (solo Mythril)
# score == 1 → hint       (solo Slither)
```

---

### Resultado unificado

```json
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
        "mythril": { "lineno": 18, "tx_sequence": {} }
      }
    }
  ]
}
```

---

### Recomendación de implementación

Empezar por la **Capa 1** (los 3 parsers + el dataclass `Finding`) porque es la parte que desbloquea todo lo demás y es independiente de cómo se decida correlacionar después. Las Capas 2 y 3 son iterables una vez se tengan los findings normalizados.
