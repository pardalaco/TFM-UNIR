# Instalación y pruebas de herramientas de análisis

Pruebas realizadas el 2026-05-18. Entorno: macOS ARM64, Python 3.11.4, Homebrew 5.1.10.

---

## 1. Preparación del entorno

### Estructura de carpetas

```bash
mkdir -p ~/Documents/TFM-UNIR/tfm-analyzer-tests/contracts
cd ~/Documents/TFM-UNIR/tfm-analyzer-tests
```

### Entorno virtual Python (venv)

Usamos `venv` para aislar las dependencias de Slither y Mythril. Echidna se instala globalmente con Homebrew.

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Compilador Solidity (solc)

Slither y Mythril necesitan `solc` para compilar los contratos antes de analizarlos.

```bash
pip install solc-select
solc-select install 0.8.20
solc-select use 0.8.20

# Verificar
solc --version
# solc, the solidity compiler commandline interface
# Version: 0.8.20+commit.a1b79de6.Darwin.appleclang
```

## Entorno virtual Python (uv)

Usamos `uv` para gestionar dependencias de Python en un entorno virtual aislado. Esto permite evitar conflictos entre Slither y Mythril, aunque ambos funcionan con las mismas versiones de `eth-typing` y `eth-utils`.

```bash
uv sync # Instala dependencias en un entorno virtual aislado
uv shell # Activa el entorno virtual

# uv no tiene acceso a solc-select, hay que instalarlo dentro del entorno uv
solc-select install 0.8.20
solc-select use 0.8.20 
````


---

## 2. Instalación de herramientas

> **Nota:** Si usas `uv`, al hacer `uv sync` se instalará Slither dentro del entorno virtual aislado, evitando conflictos de dependencias con Mythril. Si usas `venv`, ambos se instalarán en el mismo entorno y generarán warnings de versiones incompatibles, aunque ambos funcionarán correctamente.

### 2.1 Slither

- **Tipo:** Análisis estático
- **Desarrollador:** Trail of Bits
- **Lenguaje:** Python

```bash
pip install slither-analyzer

# Verificar
slither --version
# 0.11.5
```

### 2.2 Mythril

- **Tipo:** Ejecución simbólica
- **Desarrollador:** ConsenSys
- **Lenguaje:** Python

```bash
pip install mythril

# Verificar
myth version
# Mythril version v0.24.8
```

> **Nota:** Mythril instala versiones de `eth-typing` y `eth-utils` incompatibles con Slither (downgrade). Ambas herramientas funcionan correctamente a pesar del warning.

### 2.3 Echidna

- **Tipo:** Fuzzing basado en propiedades
- **Desarrollador:** Trail of Bits
- **Lenguaje:** Haskell
- **Instalación:** Homebrew (independiente del virtualenv Python)

```bash
brew install echidna

# Verificar
echidna --version
# Echidna 2.3.2
```

> **Nota:** Echidna necesita `solc` en el PATH del sistema, no en el virtualenv. Al lanzarlo hay que pasarle el PATH del virtualenv:
>
> ```bash
> PATH="~/Documents/TFM-UNIR/tfm-analyzer-tests/venv/bin:$PATH" echidna ...
> ```

---

## 3. Contratos de prueba

Ubicación: `tfm-analyzer-tests/contracts/`

### 3.1 Reentrancy.sol — Vulnerabilidad de reentrancia

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract VulnerableBank {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Saldo insuficiente");

        // Vulnerable: llamada externa ANTES de actualizar estado
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Fallo al enviar ether");

        balances[msg.sender] -= amount;
    }
}
```

### 3.2 AccessControl.sol — Control de acceso ausente

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Vault {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    // Vulnerable: cualquiera puede vaciar el contrato
    function sweep(address payable to) external {
        to.transfer(address(this).balance);
    }

    receive() external payable {}
}
```

### 3.3 UncheckedArithmetic.sol — Overflow/underflow en bloque unchecked

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract UnsafeCounter {
    uint256 public counter;

    // Vulnerable: unchecked permite overflow silencioso
    function increment(uint256 amount) external {
        unchecked {
            counter += amount;
        }
    }

    function decrement(uint256 amount) external {
        unchecked {
            counter -= amount;
        }
    }
}
```

### 3.4 EchidnaTest.sol — Propiedades para fuzzing

Echidna requiere que el contrato de test extienda el contrato a analizar y defina funciones `echidna_*` que deben mantenerse `true` en todo momento.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract UnsafeCounter {
    uint256 public counter;

    function increment(uint256 amount) external {
        unchecked { counter += amount; }
    }

    function decrement(uint256 amount) external {
        unchecked { counter -= amount; }
    }
}

contract EchidnaTest is UnsafeCounter {

    // Esta propiedad siempre es verdadera (trivial)
    function echidna_counter_no_underflow() public view returns (bool) {
        return counter <= type(uint256).max;
    }

    // Esta propiedad DEBE ser violada por el overflow
    function echidna_counter_stays_bounded() public view returns (bool) {
        return counter < 2**128;
    }
}
```

---

## 4. Comandos de análisis

### 4.1 Slither

```bash
source venv/bin/activate

# Análisis básico (salida en consola)
slither contracts/Reentrancy.sol
slither contracts/AccessControl.sol
slither contracts/UncheckedArithmetic.sol

# Guardar resultado en JSON
slither contracts/Reentrancy.sol --json outputs/slither_reentrancy.json
slither contracts/AccessControl.sol --json outputs/slither_access.json
slither contracts/UncheckedArithmetic.sol --json outputs/slither_arithmetic.json
```

### 4.2 Mythril

```bash
source venv/bin/activate

# Análisis básico con timeout de 60 segundos
myth analyze contracts/Reentrancy.sol --execution-timeout 60
myth analyze contracts/AccessControl.sol --execution-timeout 60
myth analyze contracts/UncheckedArithmetic.sol --execution-timeout 60

# Guardar resultado en JSON
myth analyze contracts/Reentrancy.sol --execution-timeout 60 -o json > outputs/mythril_reentrancy.json
myth analyze contracts/AccessControl.sol --execution-timeout 60 -o json > outputs/mythril_access.json
myth analyze contracts/UncheckedArithmetic.sol --execution-timeout 60 -o json > outputs/mythril_arithmetic.json
```

### 4.3 Echidna

```bash
# Requiere PATH extendido para que encuentre solc
PATH="~/Documents/TFM-UNIR/tfm-analyzer-tests/venv/bin:$PATH" \
  echidna contracts/EchidnaTest.sol \
  --contract EchidnaTest \
  --test-limit 10000

# Guardar resultado (extraer solo la línea JSON final)
PATH="~/Documents/TFM-UNIR/tfm-analyzer-tests/venv/bin:$PATH" \
  echidna contracts/EchidnaTest.sol \
  --contract EchidnaTest \
  --test-limit 10000 \
  --format json 2>/dev/null | grep '^{' > outputs/echidna_arithmetic.json
```

---

## 5. Resultados obtenidos

### 5.1 Slither

**Velocidad:** ~1 segundo por contrato

#### Reentrancy.sol → 3 hallazgos

| Detector          | Severidad     | Descripción                                                         |
| ----------------- | ------------- | ------------------------------------------------------------------- |
| `reentrancy-eth`  | HIGH          | `withdraw()` realiza llamada externa antes de actualizar `balances` |
| `low-level-calls` | INFORMATIONAL | Uso de `.call{value}()` de bajo nivel                               |
| `solc-version`    | INFORMATIONAL | Versión ^0.8.20 con bugs conocidos                                  |

```
Reentrancy in VulnerableBank.withdraw(uint256):
  External calls: msg.sender.call{value: amount}()
  State written after: balances[msg.sender] -= amount
```

#### AccessControl.sol → 4 hallazgos

| Detector             | Severidad     | Descripción                                                |
| -------------------- | ------------- | ---------------------------------------------------------- |
| `arbitrary-send-eth` | HIGH          | `sweep()` envía ETH a dirección arbitraria sin restricción |
| `missing-zero-check` | LOW           | Parámetro `to` no valida dirección cero                    |
| `immutable-states`   | OPTIMIZATION  | `owner` podría ser `immutable`                             |
| `solc-version`       | INFORMATIONAL | Versión con bugs conocidos                                 |

```
Vault.sweep(address) sends eth to arbitrary user
  Dangerous call: to.transfer(address(this).balance)
```

#### UncheckedArithmetic.sol → 1 hallazgo

| Detector       | Severidad     | Descripción                |
| -------------- | ------------- | -------------------------- |
| `solc-version` | INFORMATIONAL | Versión con bugs conocidos |

> **Observación:** Slither NO detecta el overflow dentro de bloque `unchecked`. Solo avisa de la versión del compilador.

---

### 5.2 Mythril

**Velocidad:** 30–120 segundos por contrato

#### Reentrancy.sol → 3 hallazgos

| SWC ID  | Severidad | Descripción                                      |
| ------- | --------- | ------------------------------------------------ |
| SWC-107 | LOW       | External call a dirección controlada por usuario |
| SWC-107 | MEDIUM    | Lectura de estado tras llamada externa           |
| SWC-107 | MEDIUM    | Escritura de estado tras llamada externa         |

```
==== State access after external call ====
SWC ID: 107 | Severity: Medium
Function: withdraw(uint256) | Line: 18
  balances[msg.sender] -= amount

Transaction Sequence:
  Caller: [CREATOR] → deploy
  Caller: [ATTACKER] → withdraw(0)
```

#### AccessControl.sol → 1 hallazgo

| SWC ID  | Severidad | Descripción                                           |
| ------- | --------- | ----------------------------------------------------- |
| SWC-105 | HIGH      | Cualquier usuario puede retirar el Ether del contrato |

```
==== Unprotected Ether Withdrawal ====
SWC ID: 105 | Severity: High
Function: sweep(address) | Line: 13
  to.transfer(address(this).balance)

Transaction Sequence:
  Caller: [CREATOR] → deploy
  Caller: [ATTACKER] → sweep(0x...deadbeef)
```

#### UncheckedArithmetic.sol → 2 hallazgos

| SWC ID  | Severidad | Descripción                                          |
| ------- | --------- | ---------------------------------------------------- |
| SWC-101 | HIGH      | Overflow en `increment()` con valor `2^255 + 1`      |
| SWC-101 | HIGH      | Underflow en `decrement()` cuando `amount > counter` |

```
==== Integer Arithmetic Bugs ====
SWC ID: 101 | Severity: High
Function: decrement(uint256) | counter -= amount  →  underflow posible
Function: increment(uint256) | counter += amount  →  overflow posible
```

> **Observación:** Mythril SÍ detecta el overflow en `unchecked`, donde Slither falla. Mythril genera además la secuencia exacta de transacciones que reproduce el bug.

---

### 5.3 Echidna

**Velocidad:** ~1 segundo (10.000 llamadas)

#### EchidnaTest.sol → 1 propiedad violada, 1 pasada

```
echidna_counter_no_underflow: passing ✅
echidna_counter_stays_bounded: failed! 💥

Call sequence:
  EchidnaTest.increment(341078997830925091125591174416463107352)

Unique instructions: 253
Corpus size: 4
Total calls: 10152
```

> **Observación:** Echidna encontró en <1 segundo un valor concreto (`3.41 × 10^38`) que hace que `counter` supere `2^128`, violando la invariante. A diferencia de Slither/Mythril, Echidna da la llamada mínima exacta que reproduce el fallo.

---

## 6. Tabla comparativa de detección

| Vulnerabilidad          | Slither       | Mythril   | Echidna                        |
| ----------------------- | ------------- | --------- | ------------------------------ |
| Reentrancy              | ✅ HIGH       | ✅ MEDIUM | ➖ (requiere propiedad manual) |
| Access control ausente  | ✅ HIGH       | ✅ HIGH   | ➖ (requiere propiedad manual) |
| Overflow en `unchecked` | ❌ No detecta | ✅ HIGH   | ✅ (viola invariante)          |
| Velocidad               | ~1s           | 30–120s   | ~1s                            |
| Output estructurado     | ✅ JSON       | ✅ JSON   | ⚠️ Texto (JSON interno)        |

---

## 7. Conclusiones preliminares

1. **Slither y Mythril son complementarios:** Slither es más rápido y produce menos ruido en reentrancy/access control; Mythril detecta overflow en `unchecked` donde Slither falla y aporta secuencias de transacciones reproducibles.
2. **Echidna tiene un modelo diferente:** No hace análisis automático — requiere que el desarrollador escriba propiedades. Su valor está en validar invariantes de negocio complejas, no en detectar patrones.
3. **Conflicto de dependencias Slither + Mythril:** Instalarlos en el mismo virtualenv genera warnings de versiones incompatibles (`eth-typing`, `eth-utils`) pero ambos funcionan. Para producción se recomendaría virtualenvs separados.
4. **Integración en el analizador:** Slither y Mythril tienen outputs JSON estructurados fáciles de parsear. Echidna requiere parseo de texto o un wrapper que genere las propiedades automáticamente.
