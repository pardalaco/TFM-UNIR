# Ataques Reales en Blockchain

---

## Resumen Estadístico

| Año                     | Pérdidas totales estimadas |
| ----------------------- | -------------------------- |
| 2021                    | ~$14,000M                  |
| 2022                    | ~$4,000M                   |
| 2023                    | ~$1,700M                   |
| 2024                    | ~$2,200M                   |
| 2025 (parcial, solo Q1) | >$1,500M                   |

---

## Ataques por Categoría

| Tipo de Ataque             | Descripción breve                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------- |
| **Reentrancy**             | Un contrato malicioso re-invoca una función antes de que se actualice el estado               |
| **Flash Loan Attack**      | Uso de préstamos sin colateral dentro de una transacción para manipular precios o protocolos  |
| **Access Control**         | Funciones críticas accesibles por actores no autorizados por falta de controles               |
| **Bridge Exploit**         | Explotación de vulnerabilidades en puentes cross-chain                                        |
| **Private Key Compromise** | Robo o filtración de claves privadas de validadores o admins                                  |
| **Governance Attack**      | Manipulación del sistema de votación de un protocolo para aprobación de propuestas maliciosas |
| **Oracle Manipulation**    | Manipulación del precio de un oráculo para beneficiarse en préstamos o liquidaciones          |
| **Logic Error**            | Error en la lógica de negocio del smart contract explotado por el atacante                    |
| **Rug Pull / Exit Scam**   | Los propios desarrolladores drenan el protocolo y desaparecen                                 |

---

## Listado de Ataques Reales

---

### 1. The DAO Hack

**Fecha:** Junio 2016 **Blockchain:** Ethereum **Tipo de ataque:** Reentrancy

**Descripción:** The DAO era un fondo de inversión descentralizado construido sobre Ethereum que recaudó 150 millones de dólares en ETH de más de 11.000 participantes —uno de los mayores crowdfundings de la historia hasta ese momento. El 17 de junio de 2016, un atacante explotó una vulnerabilidad de _reentrancy_ en la función `withdraw()` del contrato. El contrato enviaba ETH al atacante antes de actualizar el balance del usuario, lo que permitió al atacante re-invocar la función repetidamente en un bucle, drenando fondos de manera recursiva.

El resultado fue tan grave que la comunidad de Ethereum debatió activamente cómo responder. Finalmente se ejecutó un _hard fork_ controvertido en el bloque 1.920.000 (20 de julio de 2016), que revirtió las transacciones del ataque. Una parte de la comunidad rechazó el fork, dando lugar a la bifurcación que hoy conocemos como **Ethereum Classic (ETC)**.

**Coste económico:** ~$60M (≈3,6 millones de ETH; equivalente a ~$150M si se valora al precio del momento del fork)

**Fuentes:**

- 🔗 [Chainlink – Reentrancy Attacks and The DAO Hack Explained](https://blog.chain.link/reentrancy-attacks-and-the-dao-hack/)
- 🔗 [CoinDesk – How The DAO Hack Changed Ethereum and Crypto](https://www.coindesk.com/consensus-magazine/2023/05/09/coindesk-turns-10-how-the-dao-hack-changed-ethereum-and-crypto)
- 🔗 [Gemini – The DAO Hack](https://www.gemini.com/cryptopedia/the-dao-hack-makerdao)
- 🔗 [Bitstamp – Ethereum DAO Hack](https://www.bitstamp.net/learn/crypto-101/ethereum-dao-hack/)

---

### 2. Parity Wallet Hack (Primera vez)

**Fecha:** Julio 2017 **Blockchain:** Ethereum **Tipo de ataque:** Access Control (visibilidad de funciones)

**Descripción:** El smart contract de la wallet multisig de Parity Technologies contenía dos funciones críticas —`initWallet()` y `kill()`— que fueron dejadas accidentalmente como `public`, cuando deberían haber sido `internal`. Un atacante llamó a `initWallet()` para convertirse en el propietario de tres wallets de alto valor y drenar su contenido mediante `execute()`. Afectó principalmente a tres wallets multisig de proyectos recién financiados en ICOs.

**Coste económico:** ~$30M (~153.000 ETH)

**Fuentes:**

- 🔗 [Parity Technologies – Security Alert](https://www.parity.io/blog/security-alert/)
- 🔗 [Hacken – Parity Wallet Hack](https://hacken.io/discover/most-common-smart-contract-attacks/)
- 🔗 [Análisis técnico en GitHub](https://github.com/paritytech/parity-ethereum/issues/6527)

---

### 3. Parity Wallet Freeze (Segunda vez)

**Fecha:** Noviembre 2017 **Blockchain:** Ethereum **Tipo de ataque:** Logic Error (destrucción accidental del contrato biblioteca)

**Descripción:** Un usuario, aparentemente por accidente, llamó a la función `initWallet()` del contrato biblioteca (library contract) compartido por todas las wallets multisig de Parity, convirtiéndose en su propietario. A continuación, invocó la función `kill()`, que destruyó el contrato biblioteca mediante `selfdestruct`. Dado que todas las wallets multisig delegaban su lógica en esta biblioteca, quedaron permanentemente congeladas e inoperativas. A diferencia del hack anterior, los fondos no fueron robados, sino que quedaron bloqueados para siempre.

**Coste económico:** ~$150M (~513.000 ETH congelados permanentemente)

**Fuentes:**

- 🔗 [Parity Technologies – Security Alert 2](https://www.parity.io/blog/a-postmortem-on-the-parity-multi-sig-library-self-destruct/)

---

### 4. Mt. Gox

**Fecha:** 2011–2014 (descubierto en febrero de 2014) **Blockchain:** Bitcoin **Tipo de ataque:** Compromiso de infraestructura / robo progresivo interno

**Descripción:** Mt. Gox fue durante años el exchange de Bitcoin más grande del mundo, llegando a gestionar el 70% de todas las transacciones de BTC. El hack no fue un único evento, sino un robo continuado que se prolongó durante años gracias a vulnerabilidades en su sistema de gestión de claves privadas y controles internos deficientes. En febrero de 2014 el exchange suspendió todas las operaciones y se declaró en bancarrota, revelando la pérdida de aproximadamente 850.000 BTC de sus clientes (de los cuales 200.000 fueron posteriormente recuperados).

El caso desencadenó un proceso legal que se extendió por años y marcó un antes y un después en la concienciación sobre la custodia de activos en exchanges centralizados.

**Coste económico:** ~$470M (al precio de 2014); en precios actuales, equivaldría a decenas de miles de millones de dólares

**Fuentes:**

- 🔗 [Wired – The Rise and Fall of the World's Largest Bitcoin Exchange](https://www.wired.com/2014/03/bitcoin-exchange/)
- 🔗 [Wikipedia – Mt. Gox](https://en.wikipedia.org/wiki/Mt._Gox)

---

### 5. Coincheck

**Fecha:** Enero 2018 **Blockchain:** NEM (XEM) **Tipo de ataque:** Hot Wallet Compromise

**Descripción:** El exchange japonés Coincheck almacenaba una enorme cantidad de tokens NEM (XEM) en una única hot wallet conectada a internet, sin usar multisig ni almacenamiento en frío. Los atacantes accedieron a las claves privadas de dicha wallet y drenaron todos los fondos en una sola transacción. Coincheck indemnizó posteriormente a los afectados usando fondos propios.

**Coste económico:** ~$532M (526 millones de XEM)

**Fuentes:**

- 🔗 [BBC – Coincheck: The $530m cryptocurrency heist](https://www.bbc.com/news/technology-42845505)
- 🔗 [Reuters – Japan's Coincheck says it lost $400 mln in cryptocurrency to hackers](https://www.reuters.com/article/us-japan-cryptocurrency-hack/japans-coincheck-says-it-lost-400-mln-in-cryptocurrency-to-hackers-idUSKBN1FJ0CX/)

---

### 6. bZx Flash Loan Attacks

**Fecha:** Febrero 2020 (dos ataques en el mismo mes) **Blockchain:** Ethereum **Tipo de ataque:** Flash Loan + Oracle Manipulation

**Descripción:** bZx fue uno de los primeros protocolos DeFi en sufrir ataques de _flash loan_ a gran escala, y supuso un punto de inflexión en la concienciación sobre este vector. En el primer ataque (14 de febrero de 2020), el atacante tomó un préstamo flash de 10.000 ETH desde dYdX, abrió una posición corta en bZx, y usó parte de los fondos para manipular el precio de WBTC/ETH a través de Uniswap, obteniendo beneficio al cerrar la posición. En el segundo ataque (18 de febrero), el atacante manipuló el oráculo de precio de sUSD en Kyber Network para inflar su valor artificialmente y tomar prestado mucho más valor del que depositó como colateral.

**Coste económico:** ~$954.000 (primer ataque) + ~$600.000 (segundo ataque)

**Fuentes:**

- 🔗 [PeckShield – bZx Hack Analysis](https://peckshield.medium.com/bzx-hack-full-disclosure-with-detailed-profit-analysis-e6b1fa9b18fc)

---

### 7. Harvest Finance

**Fecha:** Octubre 2020 **Blockchain:** Ethereum **Tipo de ataque:** Flash Loan + Oracle Manipulation (USDC/USDT Curve pool)

**Descripción:** El atacante usó un flash loan masivo para manipular el precio de USDC en el pool de Curve Finance. Esto permitió depositar en Harvest Finance a un precio artificialmente bajo, y retirar inmediatamente a un precio normal, obteniendo beneficio. El ciclo se repitió múltiples veces en la misma transacción. El ataque puso de manifiesto los riesgos de depender de precios en tiempo real de pools de liquidez como oráculos de precio.

**Coste económico:** ~$34M

**Fuentes:**

- 🔗 [Rekt.news – Harvest Finance](https://rekt.news/harvest-finance-rekt/)

---

### 8. Compound / Yearn Finance (Cream Finance — múltiples ataques)

**Fecha:** 2021 (tres ataques distintos: febrero, agosto y octubre) **Blockchain:** Ethereum **Tipo de ataque:** Flash Loan + Reentrancy / Price Oracle Manipulation

**Descripción:** Cream Finance sufrió tres ataques relevantes en 2021. El más significativo ocurrió en octubre de 2021, cuando un atacante explotó una vulnerabilidad de reentrancy en el contrato de la versión de Cream que integraba tokens AMP (con callbacks ERC-777). El atacante tomó prestado ETH, disparó el callback del token AMP para re-entrar en la función de préstamo antes de que el saldo fuese actualizado, y repitió la operación 17 veces en una sola transacción.

**Coste económico:** ~$130M (sumando los tres ataques de 2021)

**Fuentes:**

- 🔗 [Rekt.news – Cream Finance](https://rekt.news/cream-rekt-2/)

---

### 9. Poly Network

**Fecha:** 10 de agosto de 2021 **Blockchain:** Ethereum, BNB Chain, Polygon (simultáneamente) **Tipo de ataque:** Access Control (cross-contract function call exploit)

**Descripción:** Poly Network es un protocolo de interoperabilidad cross-chain. El atacante explotó una vulnerabilidad en la función `verifyHeaderAndExecuteTx` del contrato `EthCrossChainManager`, que permitía llamar a la función `PutCurEpochConPubKeyBytes` del contrato `EthCrossChainData`. Esto posibilitó reasignar el rol de _keeper_ (la cuenta con permisos para ejecutar transacciones cross-chain) a la propia dirección del atacante, tomando control sobre los fondos del protocolo en tres blockchains simultáneamente.

En un giro inesperado, el atacante devolvió prácticamente todos los fondos, afirmando haberlo hecho "por diversión" y para demostrar la vulnerabilidad. Poly Network llegó a ofrecerle el puesto de Chief Security Officer.

**Coste económico:** ~$611M (la mayor parte fue devuelta)

**Fuentes:**

- 🔗 [Kudelski Security – Poly Network Hack Explained](https://research.kudelskisecurity.com/2021/08/12/the-poly-network-hack-explained/)

---

### 10. Compound Governance Attack (Proposal 62)

**Fecha:** Septiembre 2021 **Blockchain:** Ethereum **Tipo de ataque:** Logic Error en distribución de recompensas (bug, no ataque intencionado malicioso)

**Descripción:** Una propuesta de gobernanza en Compound Finance (Proposal 62) fue aprobada e implementó un bug en el contrato `Comptroller` que distribuyó erróneamente COMP tokens (recompensas) a usuarios que no las habían ganado. Aunque técnicamente fue un bug y no un exploit activo, ilustra el riesgo de actualizaciones en protocolos de gobernanza on-chain. El fundador del protocolo pidió públicamente a los beneficiarios que devolvieran los fondos. Se estima que ~$80M fueron distribuidos incorrectamente, de los cuales solo una parte fue recuperada.

**Coste económico:** ~$80M en COMP distribuidos incorrectamente

---

### 11. Wormhole Bridge

**Fecha:** 2 de febrero de 2022 **Blockchain:** Solana / Ethereum (bridge cross-chain) **Tipo de ataque:** Signature Verification Bypass (Logic Error)

**Descripción:** Wormhole es un puente cross-chain que conecta Solana con Ethereum y otras blockchains. El atacante explotó una vulnerabilidad en la verificación de firmas del lado de Solana. La función `verify_signatures` utilizaba una instrucción de sistema de Solana (`load_instruction_at`) que había sido marcada como deprecada, pero no eliminada del código. El atacante fabricó una instrucción de sistema falsa que pasó la validación de firmas, lo que le permitió acuñar 120.000 wETH (Wrapped ETH) en Solana sin bloquear ningún ETH real en Ethereum. Posteriormente retiró 80.000 wETH en ETH nativo a través del bridge.

Jump Crypto (firma detrás de Wormhole) restituyó los ~$320M con fondos propios el mismo día. En febrero de 2023, Jump Crypto y el protocolo Oasis recuperaron los fondos mediante un contra-exploit.

**Coste económico:** ~$320M (repuesto por Jump Crypto)

**Fuentes:**

- 🔗 [Kudelski Security – Wormhole Attack Analysis](https://kudelskisecurity.com/research/quick-analysis-of-the-wormhole-attack)
- 🔗 [Certik – Wormhole Bridge Exploit Analysis](https://certik.medium.com/wormhole-bridge-exploit-analysis-5068d79cbb71)
- 🔗 [CBS News – Wormhole restores funds](https://www.cbsnews.com/news/wormhole-ether-cryptocurrency-320-million-hack/)

---

### 12. Ronin Network / Axie Infinity

**Fecha:** 23 de marzo de 2022 (descubierto el 29 de marzo) **Blockchain:** Ronin (sidechain EVM para Axie Infinity) **Tipo de ataque:** Private Key Compromise + Social Engineering

**Descripción:** Ronin es la sidechain construida por Sky Mavis para soportar el juego blockchain Axie Infinity. La red requería 5 de 9 firmas de validadores para aprobar depósitos o retiros. Los atacantes, identificados posteriormente como el grupo norcoreano **Lazarus Group**, comprometieron las claves privadas de 4 validadores controlados por Sky Mavis. Para obtener la quinta firma necesaria, aprovecharon un backdoor: en noviembre de 2021, Axie DAO había cedido temporalmente a Sky Mavis permisos para firmar en su nombre debido a una alta carga de usuarios, pero dicho acceso **nunca fue revocado**. Con las 5 firmas en su poder, los atacantes forjaron retiros fraudulentos en dos transacciones, pasando desapercibidos durante 6 días.

El FBI atribuyó oficialmente el ataque al Lazarus Group. El Departamento del Tesoro de EEUU sancionó las wallets implicadas y Chainalysis logró recuperar más de $30M mediante análisis on-chain.

**Coste económico:** ~$625M (173.600 ETH + 25,5M USDC)

**Fuentes:**

- 🔗 [Chainalysis – Axie Infinity Ronin Bridge DPRK Hack](https://www.chainalysis.com/blog/axie-infinity-ronin-bridge-dprk-hack-seizure/)
- 🔗 [CoinDesk – Axie Infinity's Ronin Network Suffers $625M Exploit](https://www.coindesk.com/tech/2022/03/29/axie-infinitys-ronin-network-suffers-625m-exploit)
- 🔗 [CNN – Ronin Network Hack](https://www.cnn.com/2022/03/29/tech/axie-infinity-ronin-hack)

---

### 13. Beanstalk Farms (Governance Attack)

**Fecha:** 17 de abril de 2022 **Blockchain:** Ethereum **Tipo de ataque:** Flash Loan + Governance Attack

**Descripción:** Beanstalk era un protocolo de stablecoin algorítmica. El atacante tomó un flash loan masivo para adquirir temporalmente una supermayoría (~67%) de los tokens de gobernanza STALK. Con este poder de voto, aprobó una propuesta maliciosa que transfirió todos los fondos del protocolo —incluyendo colateral en ETH, BEAN y otros activos— a su propia wallet, todo dentro de una única transacción. El sistema de gobernanza de Beanstalk no tenía ningún mecanismo de timelock ni de veto de emergencia que lo impidiera.

**Coste económico:** ~$182M

**Fuentes:**

- 🔗 [Rekt.news – Beanstalk](https://rekt.news/beanstalk-rekt/)
- 🔗 [Halborn – Beanstalk Governance Attack](https://www.halborn.com/blog/post/explained-the-beanstalk-protocol-hack-april-2022)
- 🔗 [PeckShield – Beanstalk Analysis](https://twitter.com/peckshield/status/1515680335769636865)

---

### 14. Nomad Bridge

**Fecha:** 1 de agosto de 2022 **Blockchain:** Ethereum / multiple chains **Tipo de ataque:** Trusted Root Exploit (Input Validation Error)

**Descripción:** Una actualización de rutina en el contrato bridge de Nomad inicializó accidentalmente el valor de `committedRoot` (la raíz Merkle de confianza) a `0x00`. Dado que este valor era el mismo que el de mensajes no procesados, cualquier mensaje pasaba la validación automáticamente. El exploit fue especialmente peculiar: una vez publicado el primer ataque exitoso, cientos de usuarios copiaron la transacción simplemente cambiando la dirección de destino por la suya propia, sin necesitar ningún conocimiento técnico especializado. Fue descrito como un "hack libre para todos".

**Coste económico:** ~$190M (se recuperaron ~$36M de whitehats)

**Fuentes:**

- 🔗 [Elliptic – Nomad Bridge Hack Analysis](https://www.elliptic.co/blog/analysis/nomad-loses-156-million-in-seventh-major-crypto-bridge-exploit-of-2022)

---

### 15. BNB Chain Bridge (BSC Token Hub)

**Fecha:** 7 de octubre de 2022 **Blockchain:** BNB Chain **Tipo de ataque:** Proof Verifier Bug (Forja de mensajes cross-chain)

**Descripción:** El puente nativo de BNB Chain (`BSC Token Hub`) utilizaba un sistema de verificación de pruebas Merkle para validar mensajes cross-chain desde la Beacon Chain. El atacante explotó un bug en el verificador de pruebas que permitía forjar mensajes arbitrarios, y los utilizó para acuñar 2 millones de BNB directamente en su wallet. Binance reaccionó de forma extraordinaria pausando toda la BNB Chain para evitar que el atacante pudiese mover los fondos fuera de la cadena, logrando limitar el daño efectivo a entre $100M–$110M a pesar de los $566M en BNB acuñados fraudulentamente.

**Coste económico:** ~$100–110M efectivos (~$566M en BNB acuñados, mayoritariamente congelados)

**Fuentes:**

- 🔗 [Binance – Declaración oficial](https://www.bnbchain.org/en/blog/bnb-chain-ecosystem-update/)
- 🔗 [QuillHash – BSC Token Hub Bridge Hack Analysis](https://blog.quillhash.com/2022/10/11/the-million-dollars-bsc-token-hub-bridge-hack-analysis/)
- 🔗 [Hackenproof – Web3 Bridge Hacks](https://hackenproof.com/blog/for-hackers/web3-bridge-hacks)

---

### 16. FTX Hack

**Fecha:** 11 de noviembre de 2022 (día de la declaración de quiebra) **Blockchain:** Ethereum, Solana, BNB Chain **Tipo de ataque:** Hot Wallet Compromise (posiblemente insider)

**Descripción:** El mismo día en que FTX, uno de los mayores exchanges del mundo, presentó su solicitud de quiebra, más de $477M fueron drenados de sus wallets en múltiples blockchains. FTX confirmó el hack y advirtió a los usuarios de riesgos de malware. La naturaleza del ataque —ejecutado con precisión en el peor momento posible para los usuarios— llevó a numerosas investigaciones sobre si se trató de un ataque externo o interno. El nuevo CEO de FTX, John J. Ray III, describió el estado de la empresa como un "completo fracaso de controles internos".

**Coste económico:** ~$477M


---

### 17. Euler Finance

**Fecha:** 13 de marzo de 2023 **Blockchain:** Ethereum **Tipo de ataque:** Flash Loan + Logic Error (función `donateToReserves`)

**Descripción:** Euler Finance era un protocolo de préstamos y depósitos en Ethereum. El atacante explotó una combinación de dos vulnerabilidades: la función `donateToReserves` (añadida en una actualización previa) no verificaba adecuadamente el estado de liquidez de la cuenta del donante. Esto, combinado con la capacidad de auto-colateralización de los préstamos en Euler, permitió al atacante crear una posición deliberadamente insolvente y luego auto-liquidarla para capturar la totalidad del colateral del protocolo.

El atacante tomó inicialmente un flash loan de 30M DAI desde Aave, lo depositó en Euler para recibir eDAI, y usó el apalancamiento permitido por el protocolo para construir posiciones de 195M eDAI y 200M dDAI. La posterior auto-liquidación con el penalizador dinámico de Euler le transfirió los fondos de las reservas del protocolo.

En un desenlace inusual, el atacante devolvió la práctica totalidad de los fondos semanas después de una negociación directa con el equipo de Euler a través de mensajes on-chain.

**Coste económico:** ~$197M (fondos recuperados en su mayor parte)

**Fuentes:**

- 🔗 [Chainalysis – Euler Finance Flash Loan Attack](https://www.chainalysis.com/blog/euler-finance-flash-loan-attack/)
- 🔗 [Cyfrin – How Did the Euler Finance Hack Happen](https://www.cyfrin.io/blog/how-did-the-euler-finance-hack-happen-hack-analysis)
- 🔗 [QuillAudits – Decoding Euler Finance's $197 Million Exploit](https://medium.com/coinmonks/decoding-euler-finances-197-million-exploit-quillaudits-c70fed910d2c)
- 🔗 [The Block – 10 Largest Crypto Hacks 2023](https://www.theblock.co/post/268831/the-10-largest-crypto-hacks-and-exploits-of-2023)

---

### 18. Curve Finance (Vyper Re-entrancy)

**Fecha:** 30 de julio de 2023 **Blockchain:** Ethereum **Tipo de ataque:** Reentrancy (bug en el compilador de Vyper)

**Descripción:** Varios pools de liquidez de Curve Finance fueron drenados debido a una vulnerabilidad en el **compilador de Vyper** (versiones 0.2.15, 0.2.16 y 0.3.0). Estas versiones tenían un bug en la implementación del _reentrancy lock_, lo que hacía que el guard no funcionase correctamente y los pools que lo usaban fueran vulnerables a ataques de reentrancy. Los pools afectados incluían pETH/ETH, msETH/ETH, alETH/ETH y CRV/ETH. El impacto sistémico fue mayor porque el fundador de Curve (Michael Egorov) tenía préstamos colateralizados con CRV, y el desplome del precio de CRV amenazó con desencadenar liquidaciones masivas en varios protocolos DeFi.

**Coste económico:** ~$62M (directamente); riesgo sistémico adicional estimado en >$100M

**Fuentes:**

- 🔗 [Curve Finance – Declaración oficial](https://twitter.com/CurveFinance/status/1685693202722848768)
- 🔗 [Rekt.news – Curve Finance](https://rekt.news/curve-vyper-rekt/)

---

### 19. Mixin Network

**Fecha:** 23 de septiembre de 2023 **Blockchain:** Múltiples (cloud infrastructure) **Tipo de ataque:** Compromiso de base de datos cloud (infraestructura off-chain)

**Descripción:** La base de datos en la nube del proveedor de servicios de Mixin Network fue comprometida por atacantes que accedieron a activos almacenados en el nodo de base de datos. A diferencia de la mayoría de ataques DeFi, no fue un exploit de smart contract sino un ataque a la infraestructura cloud centralizada del protocolo. Mixin suspendió todos los depósitos y retiros tras detectar el incidente.

**Coste económico:** ~$200M

**Fuentes:**

- 🔗 [Rekt.news – Mixin](https://rekt.news/mixin-rekt/)

---

### 20. PlayDapp

**Fecha:** Febrero 2024 **Blockchain:** Ethereum **Tipo de ataque:** Access Control (Unauthorized Minting)

**Descripción:** PlayDapp es una plataforma de juegos blockchain. El contrato del token PLA tenía una vulnerabilidad de control de acceso que permitía a cualquier dirección con el rol de minter acuñar tokens sin límite. Los atacantes explotaron esto en dos fases: primero acuñaron 200M PLA (~$36,5M) y, al no responder el equipo de PlayDapp a sus exigencias, acuñaron otros 1.590 millones de PLA adicionales (~$253,9M). La dilución masiva del suministro de tokens causó el colapso del precio de PLA.

**Coste económico:** ~$290M

**Fuentes:**

- 🔗 [Halborn – PlayDapp Hack](https://www.halborn.com/blog/post/year-in-review-the-biggest-defi-hacks-of-2024)

---

### 21. WazirX

**Fecha:** Julio 2024 **Blockchain:** Ethereum **Tipo de ataque:** Social Engineering + Malware sobre multisig

**Descripción:** WazirX es uno de los principales exchanges de criptomonedas de la India. Los atacantes, presuntamente el grupo Lazarus de Corea del Norte, utilizaron malware para manipular la interfaz del proveedor de custodia multisig Liminal, mostrando a los firmantes una transacción aparentemente legítima mientras la transacción real transfería el control de la wallet multisig a un contrato inteligente controlado por los atacantes. Cuatro de los firmantes aprobaron la transacción sin notar la discrepancia entre la interfaz de usuario y los datos reales de la transacción.

**Coste económico:** ~$235M

**Fuentes:**

- 🔗 [Halborn – WazirX Hack](https://www.halborn.com/blog/post/year-in-review-the-biggest-defi-hacks-of-2024)
- 🔗 [Rekt.news – WazirX](https://rekt.news/wazirx-rekt/)

---

### 22. Radiant Capital

**Fecha:** Octubre 2024 (segunda vez en el año) **Blockchain:** Arbitrum / BNB Chain **Tipo de ataque:** Malware sobre firmantes multisig + Upgradeable Contract

**Descripción:** Radiant Capital sufrió dos ataques en 2024. El más grave ocurrió en octubre: los atacantes distribuyeron malware entre los ordenadores de al menos tres de los firmantes multisig del protocolo (esquema 3-de-11). El malware interceptó las solicitudes de firma legítimas y las reemplazó silenciosamente por transacciones maliciosas que transferían el control del contrato `Pool Provider` a los atacantes. Con dicho control, los atacantes realizaron upgrades maliciosos a los contratos del protocolo y usaron las aprobaciones previas de los usuarios para drenar sus wallets. Chainalysis atribuyó el ataque al Lazarus Group.

**Coste económico:** ~$53M (segundo ataque); ~$4,5M (primer ataque, flash loan)

**Fuentes:**

- 🔗 [Halborn – Radiant Capital Hack](https://www.halborn.com/blog/post/year-in-review-the-biggest-defi-hacks-of-2024)
- 🔗 [Rekt.news – Radiant Capital](https://rekt.news/radiant-capital-rekt2/)

---

### 23. Bybit

**Fecha:** 21 de febrero de 2025 **Blockchain:** Ethereum **Tipo de ataque:** Blind Signing + UI Spoofing sobre Safe Multisig

**Descripción:** Bybit es uno de los mayores exchanges de criptomonedas del mundo. Los atacantes —identificados como el Lazarus Group de Corea del Norte— comprometieron la infraestructura del proveedor de custodia multisig Safe (antes Gnosis Safe), manipulando la interfaz del frontend para mostrar transacciones legítimas mientras los firmantes en realidad aprobaban una transacción que actualizaba la implementación del proxy multisig a un contrato malicioso controlado por los atacantes. Mediante este contrato, drenaron la cold wallet de ETH del exchange.

Este ataque es el mayor robo de criptomonedas de la historia, superando por primera vez la barrera de los $1.000 millones en un único incidente. Demostró que incluso wallets frías con esquemas multisig robustos son vulnerables si la cadena de confianza del firmware o el frontend del firmador está comprometida (_blind signing_).

**Coste económico:** ~$1.400M (~$1,4 billones / 1,4 billion USD)

**Fuentes:**

- 🔗 [Concordium – Bybit Hack and Smart Contract Security](https://medium.com/@concordium/smart-contracts-arent-so-smart-bybit-s-1-5-billion-hack-and-concordium-s-secure-alternative-b132b3dd580b)
- 🔗 [Fintech Singapore – Biggest Crypto Hacks 2025](https://fintechnews.sg/108259/crypto/biggest-crypto-hacks-digital-security/)

---

## Tabla Resumen

|#|Protocolo / Exchange|Año|Tipo de Ataque|Pérdida Estimada|¿Fondos recuperados?|
|---|---|---|---|---|---|
|1|The DAO|2016|Reentrancy|~$60M|Sí (hard fork)|
|2|Parity Wallet (hack)|2017|Access Control|~$30M|No|
|3|Parity Wallet (freeze)|2017|Logic Error / Selfdestruct|~$150M|No (congelados)|
|4|Mt. Gox|2011–2014|Infra / Custodia|~$470M|Parcialmente|
|5|Coincheck|2018|Hot Wallet|~$532M|No (indemnizados)|
|6|bZx|2020|Flash Loan + Oracle|~$1.5M|No|
|7|Harvest Finance|2020|Flash Loan + Oracle|~$34M|No|
|8|Cream Finance|2021|Flash Loan + Reentrancy|~$130M|No|
|9|Poly Network|2021|Access Control|~$611M|Sí (devueltos)|
|10|Compound (bug)|2021|Logic Error|~$80M|Parcialmente|
|11|Wormhole Bridge|2022|Signature Bypass|~$320M|Sí (Jump Crypto)|
|12|Ronin Network|2022|Private Key / Social Eng.|~$625M|Parcialmente (~$30M)|
|13|Beanstalk Farms|2022|Flash Loan + Governance|~$182M|No|
|14|Nomad Bridge|2022|Input Validation|~$190M|Parcialmente|
|15|BNB Chain Bridge|2022|Proof Verifier Bug|~$100–110M|Parcialmente|
|16|FTX|2022|Hot Wallet / Insider|~$477M|En investigación|
|17|Euler Finance|2023|Flash Loan + Logic Error|~$197M|Sí (devueltos)|
|18|Curve Finance|2023|Reentrancy (bug Vyper)|~$62M|Parcialmente|
|19|Mixin Network|2023|Cloud Infrastructure|~$200M|No|
|20|PlayDapp|2024|Access Control / Mint|~$290M|No|
|21|WazirX|2024|Social Eng. + Malware|~$235M|En investigación|
|22|Radiant Capital|2024|Malware + Upgrade|~$53M|No|
|23|Bybit|2025|Blind Signing / UI Spoof|~$1.400M|En investigación|

---

## Referencias Generales

|Recurso|URL|
|---|---|
|Rekt.news – Base de datos de hacks DeFi|[rekt.news](https://rekt.news/)|
|Immunefi – Crypto Losses Reports|[immunefi.com/research](https://immunefi.com/research/)|
|Halborn – Top 100 DeFi Hacks Report|[halborn.com/reports](https://www.halborn.com/reports/top-100-defi-hacks-2025)|
|Chainalysis – Crypto Crime Report|[chainalysis.com/blog](https://www.chainalysis.com/blog/crypto-crime-midyear-update-2024/)|
|Elliptic – Blockchain analytics blog|[elliptic.co/blog](https://www.elliptic.co/blog)|
|DeFiHackLabs – Repositorio de PoCs|[github.com/SunWeb3Sec/DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs)|
|SWC Registry (Smart Contract Weaknesses)|[swcregistry.io](https://swcregistry.io/)|
|OWASP Smart Contract Top 10 (2025)|[owasp.org/www-project-smart-contract-top-10](https://owasp.org/www-project-smart-contract-top-10/)|
|Solodit – Base de datos de vulnerabilidades|[solodit.xyz](https://solodit.xyz/)|

