# Finanzas Descentralizadas (DeFi) y Vulnerabilidades Económicas

## 1. Introducción a DeFi
1.1. Definición y alcance
1.2. Diferencias con finanzas tradicionales
1.3. Componentes principales del ecosistema DeFi
1.4. Total Value Locked (TVL) y crecimiento 2020-2025

## 2. Protocolos fundamentales de DeFi
2.1. Exchanges Descentralizados (DEXs)
    - Automated Market Makers (AMMs)
    - Uniswap: modelo x*y=k
    - Curve: stableswap
    - Balancer: weighted pools
    
2.2. Lending & Borrowing
    - Compound: modelo de interés
    - Aave: flash loans, liquidaciones
    - MakerDAO: CDP y DAI

2.3. Derivados y Sintéticos
    - Synthetix
    - dYdX
    - Perpetual protocols

2.4. Yield Aggregators
    - Yearn Finance
    - Harvest Finance
    - Beefy Finance

## 3. Oráculos de precio
3.1. Problema del oráculo
3.2. Chainlink: descentralizado
3.3. TWAP (Time-Weighted Average Price)
3.4. Uniswap V3 oracles
3.5. Riesgos de manipulación

## 4. Flash Loans
4.1. ¿Qué son los flash loans?
4.2. Casos de uso legítimos
4.3. Anatomía de un ataque con flash loan
4.4. Ejemplos reales:
    - bZx (2020)
    - Harvest Finance (2020)
    - Cream Finance (2021)
    - Euler Finance (2023)

## 5. Vulnerabilidades económicas específicas de DeFi
5.1. Oracle manipulation
5.2. Flash loan attacks
5.3. Sandwich attacks
5.4. Liquidation cascades
5.5. MEV (Maximal Extractable Value)
5.6. Rug pulls y exit scams
5.7. Governance attacks
5.8. Bridge exploits

## 6. Composabilidad y riesgos sistémicos
6.1. "Money legos": composición de protocolos
6.2. Riesgos de dependencias
6.3. Efectos de contagio
6.4. Casos de estudio: Terra/Luna, FTX contagion

## 7. Detección de vulnerabilidades económicas
7.1. ¿Por qué las herramientas actuales fallan?
7.2. Necesidad de modelado económico
7.3. Análisis de invariantes financieros
7.4. Simulación de ataques económicos

## 8. Mejores prácticas en DeFi
8.1. Uso seguro de oráculos
8.2. Protección contra flash loans
8.3. Diseño de mecanismos de liquidación
8.4. Auditorías económicas vs técnicas

## Referencias
[1] Qin, K. et al. "SoK: Decentralized Finance (DeFi)", IEEE S&P 2021.
    https://arxiv.org/abs/2101.08778

[2] Qin, K. et al. "Attacking the DeFi Ecosystem with Flash Loans for 
    Fun and Profit", Financial Cryptography 2021.
    https://doi.org/10.1007/978-3-662-64331-0_1

[3] Perez, D. et al. "Liquidations: DeFi on a Knife-edge", 
    Financial Cryptography 2021.
    https://doi.org/10.1007/978-3-662-64331-0_5

[4] Zhou, L. et al. "High-Frequency Trading on Decentralized On-Chain 
    Exchanges", IEEE S&P 2021.
    https://doi.org/10.1109/SP40001.2021.00027

[5] Daian, P. et al. "Flash Boys 2.0: Frontrunning, Transaction 
    Reordering, and Consensus Instability in Decentralized Exchanges", 
    IEEE S&P 2020.
    https://doi.org/10.1109/SP40000.2020.00040

[6] Gudgeon, L. et al. "DeFi Protocols for Loanable Funds: Interest 
    Rates, Liquidity and Market Efficiency", AFT 2020.
    https://doi.org/10.1145/3419614.3423254

[7] Xu, J. et al. "SoK: Decentralized Finance (DeFi) Attacks", 
    IEEE S&P 2023.
    https://arxiv.org/abs/2208.13035