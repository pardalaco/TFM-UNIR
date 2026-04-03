# 1. Contexto de seguridad en smart contracts

Los contratos inteligentes presentan un modelo de riesgo distinto al del software tradicional por varias razones:

- **Inmutabilidad**. Una vez desplegado, el código no puede modificarse fácilmente.
- **Ejecución pública y adversarial**. El bytecode, las funciones y muchas veces el código fuente son observables por atacantes.
- **Gestión directa de activos**. Un fallo no suele comprometer solo disponibilidad o integridad lógica, sino fondos reales.
- **Composición con terceros**. Protocolos DeFi, oráculos, proxies, bridges y tokens externos amplían la superficie de ataque.
- **Semántica no trivial de la EVM**. Aspectos como `call`, `delegatecall`, `msg.sender`, `tx.origin`, gas y almacenamiento generan errores frecuentes.


Por ello, una vulnerabilidad en Solidity no debe entenderse solo como un “bug de programación”, sino como un fallo de seguridad explotable dentro de un entorno descentralizado y adversarial con incentivos económicos directos.

---

# 2. Reentrancy

## 2.1. Descripción técnica

La **reentrancy** ocurre cuando un contrato realiza una llamada externa a otro contrato antes de haber actualizado completamente su propio estado. El contrato atacante puede aprovechar esa llamada para volver a entrar en la función vulnerable y ejecutar lógica repetidamente con un estado aún inconsistente.

Es una de las vulnerabilidades más emblemáticas de Ethereum porque rompe una suposición incorrecta muy común: pensar que una llamada externa es una operación “pasiva”, cuando en realidad transfiere control de ejecución.

## 2.2. Ejemplo vulnerable

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

        // Llamada externa antes de actualizar el estado
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Fallo al enviar ether");

        balances[msg.sender] -= amount;
    }
}
```

## 2.3. Contrato atacante

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IVulnerableBank {
    function deposit() external payable;
    function withdraw(uint256 amount) external;
}

contract ReentrancyAttacker {
    IVulnerableBank public target;
    uint256 public attackAmount;

    constructor(address _target) {
        target = IVulnerableBank(_target);
    }

    function attack() external payable {
        require(msg.value >= 1 ether, "Necesitas al menos 1 ether");
        attackAmount = 1 ether;

        target.deposit{value: 1 ether}();
        target.withdraw(1 ether);
    }

    receive() external payable {
        if (address(target).balance >= attackAmount) {
            target.withdraw(attackAmount);
        }
    }
}
```

## 2.4. Por qué funciona

La secuencia es la siguiente:

1. El atacante deposita fondos.
2. Llama a `withdraw`.
3. El banco ejecuta `call{value: amount}` hacia el atacante.
4. El `receive()` del atacante se ejecuta antes de que `balances[msg.sender]` sea decrementado.
5. El atacante vuelve a llamar a `withdraw`.
6. El proceso se repite mientras el contrato víctima tenga fondos.

## 2.5. Impacto

- Robo total o parcial de fondos
- Corrupción de invariantes contables
- Encadenamiento con otras fallas lógicas

## 2.6. Mitigación

### a) Checks-Effects-Interactions

Actualizar primero el estado y luego interactuar con terceros.

```solidity
function withdraw(uint256 amount) external {
    require(balances[msg.sender] >= amount, "Saldo insuficiente");

    balances[msg.sender] -= amount;

    (bool success, ) = msg.sender.call{value: amount}("");
    require(success, "Fallo al enviar ether");
}
```

### b) Reentrancy guard

```solidity
bool private locked;

modifier nonReentrant() {
    require(!locked, "Reentrancy detectada");
    locked = true;
    _;
    locked = false;
}
```

### c) Pull over push

En vez de enviar fondos automáticamente, permitir que el usuario los reclame en operaciones separadas.

---

# 3. Integer overflow y underflow

## 3.1. Descripción técnica

Un **overflow** ocurre cuando una operación aritmética supera el valor máximo representable. Un **underflow** ocurre cuando una resta produce un valor inferior al mínimo permitido.

Antes de Solidity 0.8, estas operaciones no revertían por defecto y se producían “wrap arounds”. Desde Solidity 0.8, el compilador incorpora comprobaciones automáticas, pero el problema sigue siendo relevante:

- en contratos antiguos
- en bloques `unchecked`
- en lógica financiera compleja donde la aritmética es semánticamente incorrecta aunque no haya wraparound

## 3.2. Ejemplo vulnerable en versiones antiguas

```solidity
pragma solidity ^0.7.6;

contract TokenVulnerable {
    mapping(address => uint256) public balances;

    function transfer(address to, uint256 amount) external {
        require(balances[msg.sender] >= amount, "Fondos insuficientes");

        balances[msg.sender] -= amount;
        balances[to] += amount;
    }
}
```

Si existía una operación mal validada, un atacante podía provocar underflow y obtener un valor enorme.

Ejemplo clásico:

```solidity
pragma solidity ^0.7.6;

contract UnderflowExample {
    mapping(address => uint256) public balances;

    function decrease(uint256 amount) external {
        balances[msg.sender] -= amount;
    }
}
```

Si `balances[msg.sender]` era 0 y `amount` era 1, el resultado sería `2^256 - 1`.

## 3.3. En Solidity moderno

```solidity
pragma solidity ^0.8.20;

contract SafeArithmetic {
    function sub(uint256 a, uint256 b) external pure returns (uint256) {
        return a - b; // revierte automáticamente si b > a
    }
}
```

## 3.4. Riesgo actual real

El riesgo ya no es solo el overflow “clásico”, sino también:

- Uso incorrecto de `unchecked`
- Errores en escalado decimal
- Redondeos peligrosos
- Errores en reparto de recompensas o colateralización

Ejemplo con `unchecked`:

```solidity
pragma solidity ^0.8.20;

contract UnsafeUnchecked {
    uint256 public counter;

    function increment() external {
        unchecked {
            counter += 1;
        }
    }
}
```

## 3.5. Mitigación

- Usar Solidity `^0.8.x`
- Evitar `unchecked` salvo justificación formal
- Auditar fórmulas financieras
- Añadir tests de límites y fuzzing

---

# 4. Access control issues

## 4.1. Descripción técnica

Los problemas de **control de acceso** aparecen cuando funciones sensibles pueden ser invocadas por entidades no autorizadas o cuando el modelo de privilegios es incompleto.

No se trata solo de olvidar un `onlyOwner`. También incluye:

- Roles mal definidos
- Inicialización insegura
- Transferencia de ownership defectuosa
- Uso indebido de `tx.origin`
- Permisos excesivos

## 4.2. Ejemplo vulnerable

```solidity
pragma solidity ^0.8.20;

contract Vault {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function sweep(address payable to) external {
        to.transfer(address(this).balance);
    }

    receive() external payable {}
}
```

Cualquiera puede vaciar el contrato porque no existe restricción.

## 4.3. Versión mitigada

```solidity
pragma solidity ^0.8.20;

contract VaultSafe {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "No autorizado");
        _;
    }

    function sweep(address payable to) external onlyOwner {
        to.transfer(address(this).balance);
    }

    receive() external payable {}
}
```

## 4.4. Error crítico con `tx.origin`

```solidity
pragma solidity ^0.8.20;

contract BadAuth {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function withdrawAll(address payable to) external {
        require(tx.origin == owner, "No autorizado");
        to.transfer(address(this).balance);
    }

    receive() external payable {}
}
```

### Problema

`tx.origin` representa el originador externo de toda la transacción, no el llamador inmediato. Un atacante puede inducir al propietario a interactuar con un contrato malicioso que, a su vez, invoque `withdrawAll`.

### Mitigación

Siempre usar `msg.sender` para autenticación.

---

# 5. Delegatecall vulnerabilities

## 5.1. Descripción técnica

`delegatecall` ejecuta código de otro contrato **en el contexto de almacenamiento del contrato llamador**. Es esencial en proxies y patrones upgradeable, pero extremadamente peligroso si no se controla.

Riesgos principales:

- Corrupción del storage
- Ejecución arbitraria
- Toma de control del contrato
- Colisiones de layout entre implementaciones

## 5.2. Ejemplo vulnerable

```solidity
pragma solidity ^0.8.20;

contract LibraryContract {
    uint256 public someNumber;

    function setNumber(uint256 _num) external {
        someNumber = _num;
    }
}

contract MainContract {
    address public lib;
    address public owner;
    uint256 public someNumber;

    constructor(address _lib) {
        lib = _lib;
        owner = msg.sender;
    }

    function execute(bytes calldata data) external {
        (bool success, ) = lib.delegatecall(data);
        require(success, "delegatecall fallo");
    }
}
```

## 5.3. Problema

El código de `LibraryContract` modifica el almacenamiento de `MainContract`. Si el layout no coincide o si el contrato delegado es malicioso, puede sobrescribirse `owner`, `lib` u otras variables críticas.

Un caso peor sería permitir cambiar `lib` sin control, de modo que el atacante apunte a una implementación maliciosa.

## 5.4. Ejemplo conceptual de takeover

Si el contrato delegado escribe en el slot 0 y en `MainContract` el slot 0 corresponde a `lib`, el atacante puede modificarlo y redirigir futuras llamadas a su propio contrato.

## 5.5. Mitigación

- Restringir estrictamente qué direcciones pueden ser objetivo de `delegatecall`
- Mantener layout de almacenamiento bien definido
- Usar estándares seguros como EIP-1967 o UUPS correctamente implementados
- Auditar inicializadores y upgrades
- Evitar `delegatecall` arbitrario con `bytes` controlados por el usuario

---

# 6. Denial of Service (DoS)

## 6.1. Descripción técnica

Un **DoS** en smart contracts no siempre busca tumbar una infraestructura. A menudo persigue que una función importante quede bloqueada económicamente o lógicamente.

Patrones frecuentes:

- Bucles sobre arrays crecientes
- Reversiones inducidas por un destinatario    
- Gas exhaustion
- Bloqueo de retiradas o liquidaciones


## 6.2. Ejemplo vulnerable por push payments

```solidity
pragma solidity ^0.8.20;

contract Auction {
    address public highestBidder;
    uint256 public highestBid;

    function bid() external payable {
        require(msg.value > highestBid, "Oferta insuficiente");

        if (highestBidder != address(0)) {
            payable(highestBidder).transfer(highestBid);
        }

        highestBidder = msg.sender;
        highestBid = msg.value;
    }
}
```

## 6.3. Problema

Si el anterior `highestBidder` es un contrato cuyo fallback revierte, entonces la devolución falla y nadie puede superar la puja. El proceso queda bloqueado.

## 6.4. Mitigación con pull payments

```solidity
pragma solidity ^0.8.20;

contract AuctionSafe {
    address public highestBidder;
    uint256 public highestBid;
    mapping(address => uint256) public refunds;

    function bid() external payable {
        require(msg.value > highestBid, "Oferta insuficiente");

        if (highestBidder != address(0)) {
            refunds[highestBidder] += highestBid;
        }

        highestBidder = msg.sender;
        highestBid = msg.value;
    }

    function withdrawRefund() external {
        uint256 amount = refunds[msg.sender];
        require(amount > 0, "Nada que retirar");

        refunds[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Fallo al retirar");
    }
}
```

## 6.5. Otro patrón DoS: bucles no acotados

```solidity
pragma solidity ^0.8.20;

contract MassPayout {
    address[] public users;

    function distribute() external payable {
        uint256 share = msg.value / users.length;

        for (uint256 i = 0; i < users.length; i++) {
            payable(users[i]).transfer(share);
        }
    }
}
```

Si `users.length` crece mucho, la función puede hacerse inejecutable por límite de gas.

## 6.6. Mitigación

- Evitar iteraciones no acotadas en operaciones críticas
- Diseñar por lotes
- Aplicar pull payments
- Analizar complejidad de gas en el peor caso

---

# 7. Front-running y MEV

## 7.1. Descripción técnica

El **front-running** ocurre cuando un actor observa una transacción pendiente en la mempool y envía otra con mayor prioridad para ejecutarse antes. En Ethereum moderno este fenómeno se integra dentro del problema más amplio de **MEV**o _Maximal Extractable Value_.

No es un bug puramente sintáctico de Solidity, sino una vulnerabilidad de diseño económico y de interacción con el entorno.

## 7.2. Ejemplo conceptual

Supongamos una función para comprar un activo a un precio favorable:

```solidity
pragma solidity ^0.8.20;

contract SimpleDEX {
    uint256 public price = 1 ether;

    function buy() external payable {
        require(msg.value >= price, "Fondos insuficientes");
        // entrega del activo
    }

    function setPrice(uint256 newPrice) external {
        price = newPrice;
    }
}
```

Si un usuario detecta una oportunidad y manda una compra, un bot puede verla en mempool y adelantarse pagando más comisión. El resultado es que el primer usuario pierde la oportunidad económica.

## 7.3. Impacto

- Arbitraje adversarial
- Sandwitch attacks en AMMs
- Liquidaciones manipuladas
- Degradación de equidad del protocolo

## 7.4. Mitigación

- Commit-reveal para operaciones sensibles
- Subastas por lotes
- Slippage controls
- Private order flow
- Precios TWAP en vez de spot instantáneo
- Diseño resistente a MEV

## 7.5. Ejemplo commit-reveal simplificado

```solidity
pragma solidity ^0.8.20;

contract CommitRevealBid {
    mapping(address => bytes32) public commitments;

    function commit(bytes32 commitment) external {
        commitments[msg.sender] = commitment;
    }

    function reveal(uint256 amount, bytes32 salt) external {
        require(
            commitments[msg.sender] == keccak256(abi.encode(amount, salt)),
            "Commitment invalido"
        );

        // procesar la puja revelada
    }
}
```

Esto no elimina todo el MEV, pero reduce el front-running directo en la fase inicial.

---

# 8. Timestamp dependence

## 8.1. Descripción técnica

Los contratos pueden depender de `block.timestamp` para:

- Ventanas temporales
- Sorteos
- Desbloqueo de fondos
- Cálculo de intereses

El problema es que el timestamp no debe tratarse como una fuente de aleatoriedad ni como una señal perfectamente precisa, ya que el productor del bloque tiene cierto margen sobre su valor.

## 8.2. Ejemplo vulnerable

```solidity
pragma solidity ^0.8.20;

contract TimestampLottery {
    function play() external payable returns (bool) {
        require(msg.value == 1 ether, "Debes enviar 1 ETH");

        if (block.timestamp % 2 == 0) {
            payable(msg.sender).transfer(2 ether);
            return true;
        }

        return false;
    }

    receive() external payable {}
}
```

## 8.3. Problema

La lógica usa el timestamp como fuente pseudoaleatoria. Un validador con incentivos suficientes podría influir en el bloque para favorecer determinado resultado.

## 8.4. Mitigación

- No usar `block.timestamp` como aleatoriedad
- Usar VRF o mecanismos criptográficos verificables
- Permitir tolerancias temporales razonables
- Evitar condiciones críticas decididas por timestamp exacto

---

# 9. Weak randomness

Aunque está relacionada con el punto anterior, merece tratamiento separado. Muchos contratos intentan generar aleatoriedad con variables on-chain previsibles.

## 9.1. Ejemplo vulnerable

```solidity
pragma solidity ^0.8.20;

contract BadRandom {
    function random() public view returns (uint256) {
        return uint256(
            keccak256(
                abi.encodePacked(block.timestamp, block.prevrandao, msg.sender)
            )
        );
    }
}
```

## 9.2. Problema

Aunque la mezcla parezca robusta, las entradas no son completamente impredecibles ni inmunes a manipulación contextual. En juegos, sorteos o asignación de rarezas, esto puede romper la seguridad económica.

## 9.3. Mitigación

- Chainlink VRF o soluciones equivalentes
- Commit-reveal con incentivos bien diseñados
- Esquemas multipartitos verificables

---

# 10. Logic flaws

## 10.1. Descripción técnica

Las **logic flaws** son especialmente importantes porque no siempre encajan en patrones clásicos de herramientas automáticas. El código puede ser sintácticamente correcto y no contener underflows, reentrancy o accesos evidentes, pero implementar una lógica de negocio insegura.

Ejemplos típicos:

- Cálculo incorrecto de colateral
- Retiro múltiple permitido por una secuencia anómala
- Precios manipulables
- Estados imposibles no contemplados
- Reparto injusto por redondeo

## 10.2. Ejemplo

```solidity
pragma solidity ^0.8.20;

contract RewardPool {
    mapping(address => uint256) public deposits;
    uint256 public totalDeposits;

    function deposit() external payable {
        deposits[msg.sender] += msg.value;
        totalDeposits += msg.value;
    }

    function withdraw() external {
        uint256 userShare = address(this).balance * deposits[msg.sender] / totalDeposits;

        deposits[msg.sender] = 0;
        totalDeposits -= deposits[msg.sender];

        (bool success, ) = msg.sender.call{value: userShare}("");
        require(success, "Fallo");
    }
}
```

## 10.3. Problema

Hay un error lógico: `totalDeposits -= deposits[msg.sender]` ocurre después de poner `deposits[msg.sender] = 0`, por lo que nunca se decrementa correctamente. Esto rompe la contabilidad y puede producir retiros erróneos.

## 10.4. Mitigación

- Modelado de invariantes
- Revisión manual orientada a negocio
- Tests basados en propiedades
- Fuzzing con condiciones de consistencia

---

# 11. Unsafe external calls

## 11.1. Descripción técnica

Toda llamada a contratos externos introduce riesgo porque:

- Puede revertir
- Puede consumir gas inesperadamente
- Puede ejecutar lógica arbitraria
- Puede devolver datos malformados
- Puede no seguir el estándar esperado

## 11.2. Ejemplo con token no estándar

```solidity
pragma solidity ^0.8.20;

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}

contract TokenSender {
    function sendToken(address token, address to, uint256 amount) external {
        IERC20(token).transfer(to, amount);
    }
}
```

## 11.3. Problema

No todos los tokens ERC-20 implementan correctamente `transfer` devolviendo `bool`. Algunos revierten, otros no devuelven nada. Si no se usa una librería segura, el contrato puede comportarse incorrectamente.

## 11.4. Mitigación

- Usar wrappers seguros como `SafeERC20`
- Tratar toda dependencia externa como no confiable
- Validar retornos y fallos
- Minimizar suposiciones sobre estándares

---

# 12. Uninitialized proxy / initializer vulnerabilities

## 12.1. Descripción técnica

En contratos upgradeables, el constructor se sustituye por funciones `initialize`. Si el inicializador no se protege, cualquiera puede ejecutarlo y convertirse en administrador.

## 12.2. Ejemplo conceptual

```solidity
pragma solidity ^0.8.20;

contract UpgradeableVault {
    address public owner;
    bool public initialized;

    function initialize(address _owner) external {
        require(!initialized, "Ya inicializado");
        owner = _owner;
        initialized = true;
    }

    function sweep(address payable to) external {
        require(msg.sender == owner, "No autorizado");
        to.transfer(address(this).balance);
    }

    receive() external payable {}
}
```

## 12.3. Problema

Si el despliegue no llama inmediatamente a `initialize`, un atacante puede ejecutarla antes.

## 12.4. Mitigación

- Inicializar en el mismo flujo de despliegue
- Usar librerías estándar auditadas
- Deshabilitar inicializadores en implementaciones lógicas cuando proceda

---

# 13. Signature replay y verificación incorrecta

## 13.1. Descripción técnica

Muchos contratos aceptan operaciones autorizadas por firma off-chain. Si la firma no incluye `nonce`, `chainId`, dominio o contexto suficiente, puede reutilizarse indebidamente.

## 13.2. Ejemplo vulnerable

```solidity
pragma solidity ^0.8.20;

contract ReplayVulnerable {
    mapping(address => uint256) public balances;

    function executeWithdraw(
        address user,
        uint256 amount,
        bytes32 hash,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) external {
        address signer = ecrecover(hash, v, r, s);
        require(signer == user, "Firma invalida");

        balances[user] -= amount;
        payable(user).transfer(amount);
    }

    receive() external payable {}
}
```

## 13.3. Problema

La misma firma puede reutilizarse múltiples veces si `hash` no incluye un `nonce` consumible ni un dominio único.

## 13.4. Mitigación

- Usar EIP-712
- Incluir `nonce`, `deadline`, `chainId`, `address(this)`
- Invalidar firmas tras su uso

---

# 14. Oracle manipulation

## 14.1. Descripción técnica

Muchos protocolos dependen de precios externos. Si el contrato usa un precio manipulable, por ejemplo de baja liquidez o instantáneo en un AMM, un atacante puede alterarlo temporalmente y explotar la lógica de préstamos, liquidaciones o colateral.

## 14.2. Ejemplo conceptual

```solidity
pragma solidity ^0.8.20;

interface IPriceOracle {
    function getPrice() external view returns (uint256);
}

contract LendingProtocol {
    IPriceOracle public oracle;

    constructor(address _oracle) {
        oracle = IPriceOracle(_oracle);
    }

    function borrow(uint256 collateralAmount) external view returns (uint256) {
        uint256 price = oracle.getPrice();
        return collateralAmount * price / 2;
    }
}
```

## 14.3. Problema

Si `getPrice()` proviene de una fuente manipulable en un solo bloque, el atacante puede inflar artificialmente el colateral, pedir más préstamo del debido y dejar deuda incobrable.

## 14.4. Mitigación

- Usar oráculos robustos y descentralizados
- Usar TWAP
- Validaciones cruzadas
- Límites de variación
- Pausas de emergencia

---

# 15. Selfdestruct y suposiciones erróneas sobre Ether recibido

Históricamente, un contrato podía recibir Ether sin ejecutar su lógica mediante `selfdestruct`. Aunque la semántica de `SELFDESTRUCT` ha evolucionado en Ethereum, la idea de fondo sigue siendo importante: **no se debe asumir que el balance del contrato solo cambia a través de funciones previstas**.

## Ejemplo conceptual

```solidity
pragma solidity ^0.8.20;

contract BalanceDependent {
    function isGoalReached() external view returns (bool) {
        return address(this).balance == 10 ether;
    }

    receive() external payable {}
}
```

Si la lógica depende de que el balance coincida exactamente con cierto valor, entradas inesperadas pueden romper invariantes.

## Mitigación

- No modelar estado crítico solo con `address(this).balance`
- Mantener variables internas de contabilidad
- Diseñar invariantes robustos ante Ether forzado

---

# 16. Problemas específicos de Solidity y diseño inseguro

Además de vulnerabilidades “clásicas”, en auditoría real aparecen con frecuencia estos errores:

## 16.1. Falta de validación de entradas

```solidity
function setFee(uint256 fee) external onlyOwner {
    protocolFee = fee;
}
```

Si no se impone un máximo razonable, el propietario o una clave comprometida puede inutilizar el protocolo.

## 16.2. Estados no sincronizados

Variables duplicadas o caches que pueden divergir del almacenamiento real.

## 16.3. Errores en herencia y override

Contratos que asumen un orden de resolución de métodos erróneo.

## 16.4. Dependencia excesiva de privilegios

Aunque no haya un bug técnico, un contrato con funciones administrativas demasiado poderosas presenta riesgo sistémico.

---

# 17. Clasificación útil para auditoría

En una auditoría de contratos inteligentes, conviene clasificar hallazgos en estas categorías:

## A. Vulnerabilidades técnicas de ejecución

- Reentrancy
- Overflow/underflow
- Delegatecall unsafe
- Llamadas externas inseguras

## B. Vulnerabilidades de control

- Permisos insuficientes
- Inicialización insegura
- Privilegios excesivos
- Uso de `tx.origin`

## C. Vulnerabilidades económicas

- Front-running
- Manipulación de oráculos
- MEV
- Incentivos perversos

## D. Vulnerabilidades lógicas

- Errores de contabilidad
- Estados inconsistentes
- Fórmulas defectuosas
- Bypass de restricciones de negocio

Esta clasificación es importante porque muchas herramientas automáticas detectan bien A y parcialmente B, pero tienen limitaciones claras en C y D.

---

# 18. Buenas prácticas de mitigación

## A nivel de implementación

- Aplicar patrón **Checks-Effects-Interactions**
- Usar librerías auditadas
- Minimizar llamadas externas
- Evitar complejidad innecesaria
- Documentar invariantes

## A nivel de diseño

- Asumir mempool adversarial
- Modelar incentivos económicos
- Desacoplar privilegios críticos
- Limitar confianza en terceros

## A nivel de verificación

- Static analysis
- Symbolic execution
- Fuzzing
- Tests unitarios e integración
- Revisión manual
- Formal verification en componentes críticos

---

# 19. Conclusión 

La seguridad de contratos inteligentes no puede reducirse a una lista de patrones vulnerables. El mayor error metodológico en auditoría es pensar que la ausencia de hallazgos automáticos implica seguridad. En la práctica:

- Las vulnerabilidades más destructivas combinan fallo técnico y explotación económica
- Los errores de lógica de negocio suelen escapar a detectores basados en patrones
- La composabilidad multiplica riesgos no previstos en el diseño aislado del contrato
- Una auditoría rigurosa debe analizar sintaxis, semántica, interacción con la EVM y comportamiento económico del protocolo

Por eso, el análisis de contratos inteligentes debe plantearse como una combinación de **ingeniería segura, análisis programático y evaluación adversarial del modelo económico**.

