# Ataques Reales en Blockchain

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
