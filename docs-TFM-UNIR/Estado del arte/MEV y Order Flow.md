# MEV (Maximal Extractable Value) y Manipulación de Order Flow

## 1. Introducción al MEV
1.1. Definición: valor extraíble de reordenación
1.2. Historia: De "Miner" a "Maximal"
1.3. Magnitud del problema (datos 2020-2025)
1.4. Impacto en usuarios

## 2. Mempool y orden de transacciones
2.1. ¿Qué es la mempool?
2.2. Proceso de inclusión en bloque
2.3. Gas price y prioridad
2.4. Visible vs dark order flow

## 3. Tipos de MEV
3.1. Front-running (sandwich attacks)
3.2. Back-running (arbitrage)
3.3. Liquidation MEV
3.4. DEX arbitrage
3.5. NFT sniping
3.6. Time-bandit attacks

## 4. Anatomía de un sandwich attack
4.1. Detección de transacción víctima
4.2. Construcción del bundle
4.3. Cálculo de profitabilidad
4.4. Ejemplo técnico paso a paso

## 5. Infraestructura de MEV
5.1. Flashbots: MEV-Boost
5.2. Proposer-Builder Separation (PBS)
5.3. Private order flow (RPC privado)
5.4. MEV relays

## 6. MEV en Ethereum post-Merge
6.1. Cambios con Proof of Stake
6.2. Validators vs Builders
6.3. Censura de transacciones
6.4. Riesgos de centralización

## 7. Vulnerabilidades relacionadas con MEV
7.1. Slippage insuficiente
7.2. Deadline muy largo
7.3. Funciones sin protección anti-MEV
7.4. Oráculos manipulables

## 8. Protecciones contra MEV
8.1. Slippage protection
8.2. Commit-reveal schemes
8.3. Batch auctions
8.4. Private transactions
8.5. Mejores prácticas en contratos

## 9. Futuro del MEV
9.1. MEV minimization
9.2. MEV redistribution
9.3. Encrypted mempools
9.4. Threshold encryption

## Referencias
[1] Daian, P. et al. "Flash Boys 2.0: Frontrunning in Decentralized 
    Exchanges", IEEE S&P 2020.
    https://doi.org/10.1109/SP40000.2020.00040

[2] Qin, K. et al. "Quantifying Blockchain Extractable Value", 
    IEEE S&P 2022.
    https://doi.org/10.1109/SP46214.2022.9833734

[3] Flashbots. "MEV-Boost: Merge ready Flashbots architecture", 2022.
    https://writings.flashbots.net/

[4] Eskandari, S. et al. "SoK: Transparent Dishonesty: Front-running 
    Attacks on Blockchain", Financial Cryptography Workshops 2019.
    https://doi.org/10.1007/978-3-030-43725-1_13

[5] Zhou, L. et al. "High-Frequency Trading on Decentralized Exchanges", 
    IEEE S&P 2021.