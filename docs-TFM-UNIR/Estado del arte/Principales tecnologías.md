
# Principales tecnologías
## 1. Ethereum (Solidity)

Es la plataforma pionera y el estándar de la industria. **Solidity** es el lenguaje orientado a objetos diseñado específicamente para escribir contratos inteligentes en la Ethereum Virtual Machine (EVM).

  * **¿Qué hace / Ventajas?:** \* **Ecosistema masivo:** Es la red con más desarrolladores, herramientas y librerías (como OpenZeppelin).
      * **EVM Compatibility:** La mayoría de las otras redes (Polygon, Avalanche, BSC) usan la EVM, por lo que aprender Solidity te permite desplegar en múltiples cadenas.
      * **Seguridad probada:** Al ser la más antigua, sus vulnerabilidades y patrones de diseño están muy bien documentados.

**Documentación oficial:**
  * [Solidity Documentation](https://docs.soliditylang.org/)
  * [Ethereum Developer Resources](https://ethereum.org/en/developers/docs/smart-contracts/)

-----

## 2. Rust (Solana & Polkadot)

Rust no nació para blockchain, pero se ha convertido en el lenguaje favorito para redes de alto rendimiento debido a su gestión de memoria extremadamente segura y eficiente.

  * **¿Qué hace / Ventajas?:**
      * **Rendimiento extremo:** Permite procesar miles de transacciones por segundo (TPS) en redes como Solana.
      * **Seguridad de memoria:** Evita errores comunes de programación (como el desbordamiento de búfer) gracias a su sistema de "ownership".
      * **Versatilidad:** Se usa tanto en **Solana** (vía Anchor framework) como en **Polkadot** (vía el framework Substrate).

**Documentación oficial:**
  * [Solana Program Library (SPL)](https://solana.com/docs)
  * [Polkadot / Substrate Documentation](https://docs.substrate.io/)

-----

## 3. Vyper

Es el segundo lenguaje más popular para la Ethereum Virtual Machine. Tiene una sintaxis muy similar a **Python**.

  * **¿Qué hace / Ventajas?:**
      * **Legibilidad y Simplicidad:** Está diseñado para ser fácil de leer, lo que facilita las auditorías de seguridad.
      * **Seguridad por restricción:** A diferencia de Solidity, elimina características que suelen causar bugs (como la herencia o la recursividad), haciendo que el código sea más predecible.

**Documentación oficial:**
  * [Vyper Documentation](https://docs.vyperlang.org/)

-----

## 4. Move (Aptos & Sui)

Es un lenguaje de programación de nueva generación basado en Rust, desarrollado originalmente por Meta (Facebook) para el proyecto Libra/Diem.

  * **¿Qué hace / Ventajas?:**
      * **First-class Resources:** En Move, los activos digitales (tokens) no son solo números en un mapa, sino "recursos" reales que no pueden ser copiados o borrados accidentalmente.
      * **Seguridad Nativa:** Incluye el "Move Prover", una herramienta de verificación formal que asegura que el contrato se comporte exactamente como se espera matemáticamente.

**Documentación oficial:**
  * [Aptos Move Documentation](https://aptos.dev/build/guides/first-move-module)
  * [Sui Move Documentation](https://docs.sui.io/concepts/sui-move-concepts)

-----

## 5. Chainlink (Oráculos)

Aunque no es un lenguaje de programación *per se*, es la tecnología de infraestructura más crítica para que los Smart Contracts interactúen con el mundo real.

  * **¿Qué hace / Ventajas?:**
      * **Datos externos:** Permite que un contrato sepa el precio del Euro, el resultado de un partido de fútbol o el clima, de forma descentralizada.
      * **Automatización:** Sus "Keepers" permiten ejecutar funciones de contratos automáticamente bajo ciertas condiciones de tiempo o eventos.

**Documentación oficial:**

  * [Chainlink Documentation](https://docs.chain.link/)

-----

## Herramientas de Desarrollo (Tech Stack)

| Tecnología       | Propósito                                          | Link                                               |
| :--------------- | :------------------------------------------------- | :------------------------------------------------- |
| **Hardhat**      | Entorno de desarrollo para Ethereum (JS/TS).       | [hardhat.org](https://hardhat.org/)                |
| **Foundry**      | Toolkit de desarrollo en Rust, ultrarrápido.       | [book.getfoundry.sh](https://book.getfoundry.sh/)  |
| **OpenZeppelin** | Estándares de contratos seguros (ERC-20, ERC-721). | [openzeppelin.com](https://docs.openzeppelin.com/) |

