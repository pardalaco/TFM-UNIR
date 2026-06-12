# ANEXO. Ejemplos de vulnerabilidades en contratos inteligentes

Este anexo presenta ejemplos simplificados de vulnerabilidades representativas en contratos inteligentes desarrollados en Solidity. El objetivo es ilustrar de forma práctica los principales tipos de debilidades descritas en la sección 4.4, facilitando su comprensión y su posterior detección mediante herramientas automáticas.

Cada ejemplo incluye: descripción, fragmento de código vulnerable, impacto y estrategia de mitigación.

## ANEXO.1. Vulnerabilidades técnicas de ejecución

### ANEXO.1.1. Reentrancy

La vulnerabilidad de [**reentrancy**](https://www.cyfrin.io/blog/what-is-a-reentrancy-attack-solidity-smart-contracts) se produce cuando un contrato realiza una llamada externa antes de actualizar su estado interno, permitiendo que el contrato receptor reingrese en la función original en un estado inconsistente.

Código vulnerable
```js
contract VulnerableBank {

    mapping(address => uint256) public balances;

    function deposit() public payable {

        balances[msg.sender] += msg.value;

    }

    function withdraw(uint256 amount) public {

        require(balances[msg.sender] >= amount);

        (bool success, ) = msg.sender.call{value: amount}("");

        require(success);

        balances[msg.sender] -= amount;

    }

}
```

- **Impacto**: Un atacante puede drenar fondos repitiendo la llamada antes de que el balance sea actualizado.
- Mitigación:
	- Patrón [_Checks-Effects-Interactions_](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html)
	- Uso de ReentrancyGuard
	- Actualizar el estado antes de llamadas externas

  
### ANEXO.1.2. Integer Overflow / Underflow

Errores aritméticos que provocan desbordamientos en operaciones enteras. Aunque mitigados en Solidity ≥0.8, siguen siendo relevantes en bloques unchecked.

Código vulnerable
```js
function increment(uint256 x) public pure returns (uint256) {

    unchecked {

        return x + 1;

    }

}
```

- **Impacto**: Puede alterar balances o condiciones lógicas críticas.
- Mitigación:
	- Evitar unchecked salvo casos justificados
	- Uso de validaciones explícitas

### ANEXO.1.3. Uso inseguro de delegatecall

La función delegatecall ejecuta código externo en el contexto de almacenamiento del contrato llamador.

Código vulnerable
```js
contract Proxy {

    address public implementation;

    function execute(bytes memory data) public {

        (bool success, ) = implementation.delegatecall(data);

        require(success);

    }

}
```

- **Impacto**: Compromiso total del almacenamiento del contrato.
- Mitigación:
	- Control estricto de la dirección implementation
	- Uso de patrones proxy auditados ([EIP-1967](https://eips.ethereum.org/EIPS/eip-1967), [UUPS](https://docs.openzeppelin.com/contracts-stylus/uups-proxy))

### ANEXO.1.4. Denegación de servicio (DoS)

Bloqueo de ejecución debido a fallos en llamadas externas o estructuras no acotadas.

Código vulnerable
```js
function payout(address[] memory recipients) public {

    for (uint i = 0; i < recipients.length; i++) {

        payable(recipients[i]).transfer(1 ether);

    }

}
```
- **Impacto**: Un solo fallo revierte toda la operación.
- Mitigación
	- Uso de [patrón _pull over push_](https://medium.com/@markojauregui/the-pull-over-push-model-in-solidity-a-secure-pattern-for-fund-withdrawals-10c2e6628626)
	- Evitar bucles dependientes de input externo

## ANEXO.2. Vulnerabilidades técnicas de control y privilegios

### ANEXO.2.1. Falta de control de acceso

Funciones críticas accesibles por cualquier usuario.

Código vulnerable
```js
contract Ownable {

    address public owner;

    function withdrawAll() public {

        payable(msg.sender).transfer(address(this).balance);

    }

}
```

- **Impacto**: Pérdida total de fondos.
- Mitigación:
	- Uso de onlyOwner
	- Librerías como [OpenZeppelin AccessControl](https://docs.openzeppelin.com/contracts/5.x/access-control)

### ANEXO.2.2. Uso de tx.origin

Uso incorrecto de tx.origin para autenticación.

Código vulnerable
```js
function withdraw() public {

    require(tx.origin == owner);

    payable(msg.sender).transfer(address(this).balance);

}
```
- **Impacto**: Ataques mediante contratos intermediarios.
- **Mitigación**: Usar msg.sender para autenticación

### ANEXO.2.3. Inicialización insegura (contratos upgradeables)

En contratos upgradeables, la inicialización se realiza mediante funciones externas (initialize) en lugar de constructores. Si no están protegidas, cualquier usuario puede ejecutarlas y asumir el control del contrato.

Código vulnerable
```js
function initialize(address _owner) public {

    owner = _owner;

}
```
- **Impacto**: Un atacante puede inicializar el contrato antes que el legítimo propietario.
- Mitigación:
	- Uso de [initializer (OpenZeppelin)](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable)
	- Bloqueo de inicialización tras ejecución

## ANEXO.3. Vulnerabilidades económicas y del entorno

### ANEXO.3.1. Front-running / MEV

Un atacante observa la mempool y ejecuta transacciones antes que la víctimANEXO.

Código vulnerable
```js
function buy(uint price) public {

    require(price == currentPrice);

    // compra

}
```
- **Impacto**: Manipulación de operaciones (arbitraje, liquidaciones, subastas).
- Mitigación:
	- [_Commit-reveal_](https://medium.com/coinmonks/commit-reveal-scheme-in-solidity-c06eba4091bb)
	- Subastas ciegas
	- Uso de _relayers_ privados

### ANEXO.3.2. Dependencia de oráculos

Uso de datos externos manipulables.

Código vulnerable
```
function getPrice() public view returns (uint) {

    return externalOracle.price();

}
```

- **Impacto**: Manipulación de precios en DeFi.
- Mitigación:
	- Oráculos descentralizados (ej. [Chainlink](https://chain.link/))
	- Promedios temporales ([TWAP](https://www.binance.com/es-MX/support/faq/detail/80655cc54d8a4b2bb8ea097001844fd1))

### ANEXO.3.3. Uso de block.timestamp

El uso de block.timestamp como fuente de aleatoriedad o para decisiones críticas es inseguro, ya que su valor puede ser parcialmente manipulado por mineros o validadores dentro de ciertos límites.

Código vulnerable
```
function random() public view returns (uint) {

    return uint(keccak256(abi.encodePacked(block.timestamp)));

}
```
- **Impacto**: Resultados predecibles o manipulables por mineros/validadores.
- Mitigación:
	- VRF ([Verifiable Random Functions](https://chain.link/education-hub/verifiable-random-function-vrf))
	- Fuentes externas verificables

## ANEXO.4. Errores lógicos de negocio

### ANEXO.4.1. Error en cálculo de balances

Errores en operadores lógicos o condiciones de validación pueden provocar inconsistencias en la gestión de balances, especialmente en casos límite donde las condiciones no cubren todos los escenarios posibles.

Código vulnerable
```js
function withdraw(uint amount) public {

    require(balances[msg.sender] > amount);

    balances[msg.sender] -= amount;

}
```
- **Impacto**: Comportamiento incorrecto en condiciones límite.
- Mitigación:
	- Uso de > en lugar de >=.

### ANEXO.4.2. Distribución incorrecta de recompensas

La lógica de distribución puede introducir errores debido a divisiones enteras o falta de gestión de restos, provocando pérdida de precisión y fondos no asignados correctamente.

Código vulnerable
```js
function distribute() public {

    uint reward = total / users.length;

    for (uint i = 0; i < users.length; i++) {

        balances[users[i]] += reward;

    }

}
```
- Impacto:
	- Pérdida de fondos debido a errores de redondeo (truncamiento en división entera)
	- Acumulación de saldo no distribuido en el contrato
	- Distribuciones injustas entre usuarios
	- Posibles vectores de explotación si un atacante manipula el número de participantes

- Mitigación:
	- Uso de patrones de distribución que gestionen residuos (por ejemplo, acumuladores o “_remainder handling_”)
	- Empleo de mayor precisión mediante escalado ([_fixed-point arithmetic_](https://rareskills.io/post/solidity-fixed-point))
	- Validación de invariantes económicas (la suma distribuida debe coincidir con el total)
	- Testing específico de casos límite (número de usuarios, valores pequeños, etc.)

### ANEXO.4.3. Estados inconsistentes

La falta de control adecuado sobre las transiciones de estado puede permitir la ejecución de funciones en condiciones no válidas, generando comportamientos inconsistentes en el contrato.

Código vulnerable
```js
enum State { Open, Closed }

State public state;

function close() public {

    state = State.Closed;

}

function bid() public payable {

    require(state == State.Open);

}
```
- Impacto:
	- Ejecución de funciones en estados no válidos
	- Comportamiento inesperado del contrato
	- Bloqueo o bypass de lógica de negocio
	- Posible explotación combinada con otras vulnerabilidades (por ejemplo, _front-running_ o _reentrancy_
- Mitigación:
	- Implementación de máquinas de estados explícitas y completas
	- Uso de modificadores para validar estado (inState(State.Open))
	- Restricción de transiciones de estado válidas
	- Aplicación de patrones [_state machines_](https://fravoll.github.io/solidity-patterns/state_machine.html)

## ANEXO.5. Resumen de vulnerabilidades

| **_ID_** | **Categoría** | **Vulnerabilidad**    | **Tipo**            | **Impacto** | **Detectable automáticamente** | **Ejemplo sección** |
| -------- | ------------- | --------------------- | ------------------- | ----------- | ------------------------------ | ------------------- |
| _V1_     | Técnica       | Reentrancy            | Ejecución           | Crítico     | Sí (Slither/Mythril)           | ANEXO.1.1               |
| _V2_     | Técnica       | Overflow              | Aritmético          | Medio       | Sí (Slither)                   | ANEXO.1.2               |
| _V3_     | Técnica       | Delegatecall          | Ejecución           | Crítico     | Parcial                        | ANEXO.1.3               |
| _V4_     | Control       | Acceso no restringido | Autorización        | Crítico     | Sí                             | ANEXO.2.1               |
| _V5_     | Control       | tx.origin             | Autenticación       | Alto        | Sí                             | ANEXO.2.2               |
| _V6_     | Económica     | Front-running         | MEV                 | Alto        | No                             | ANEXO.3.1               |
| _V7_     | Económica     | Oráculos              | Dependencia externa | Crítico     | No                             | ANEXO.3.2               |
| _V8_     | Lógica        | Error de balance      | Lógica              | Variable    | No                             | ANEXO.4.1               |