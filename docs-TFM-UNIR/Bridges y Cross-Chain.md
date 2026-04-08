# Puentes Cross-Chain (Bridges) y Vulnerabilidades

## 1. Introducción a la interoperabilidad blockchain
1.1. Problema de las blockchains aisladas
1.2. Necesidad de transferir activos cross-chain
1.3. Casos de uso de bridges

## 2. Tipos de bridges
2.1. Lock-and-Mint (Wrapped assets)
2.2. Burn-and-Mint
2.3. Atomic Swaps
2.4. Liquidity Networks
2.5. Comparativa de modelos

## 3. Arquitecturas de bridges
3.1. Centralizados (custodial)
3.2. Semi-descentralizados (multisig)
3.3. Descentralizados (light clients)
3.4. Optimistic bridges
3.5. Zero-knowledge bridges

## 4. Componentes técnicos de un bridge
4.1. Validadores/Relayers
4.2. Verificación de pruebas cross-chain
4.3. Smart contracts de bloqueo/acuñación
4.4. Sistemas de consenso
4.5. Mecanismos de seguridad

## 5. Vulnerabilidades específicas de bridges
5.1. Compromiso de claves de validadores
5.2. Bypass de verificación de pruebas
5.3. Manipulación de mensajes cross-chain
5.4. Input validation failures
5.5. Ataques de replay
5.6. Race conditions

## 6. Análisis de ataques reales a bridges
6.1. Wormhole (2022): Signature bypass
    - Código vulnerable
    - Explotación técnica
    - Lecciones aprendidas
    
6.2. Ronin Network (2022): Private key compromise
    - Modelo de validadores
    - Vector de ataque
    - Implicaciones de seguridad
    
6.3. Nomad Bridge (2022): Trusted root = 0x00
    - Bug de inicialización
    - Exploit masivo ("free-for-all")
    - Post-mortem técnico
    
6.4. Poly Network (2021): Access control cross-chain
    - Función vulnerable
    - Takeover del sistema
    - Devolución de fondos
    
6.5. BNB Chain Bridge (2022): Proof verifier bug
    - Falsificación de mensajes
    - Respuesta de emergencia

## 7. Detección de vulnerabilidades en bridges
7.1. Desafíos únicos vs contratos normales
7.2. Necesidad de análisis cross-chain
7.3. Verificación de pruebas criptográficas
7.4. Modelado de consenso multi-firma

## 8. Mejores prácticas en diseño de bridges
8.1. Diseño de sistemas de validación
8.2. Verificación formal de pruebas
8.3. Límites de transferencia
8.4. Timelock y pausas de emergencia
8.5. Auditorías especializadas

## 9. Futuro de bridges
9.1. ZK-bridges
9.2. Restaking y shared security
9.3. Interoperabilidad nativa (Cosmos IBC, Polkadot)

## Referencias
[1] Zamyatin, A. et al. "SoK: Communication Across Distributed Ledgers", 
    Financial Cryptography 2021.
    https://eprint.iacr.org/2019/1128.pdf

[2] Belchior, R. et al. "A Survey on Blockchain Interoperability: 
    Past, Present, and Future Trends", ACM Computing Surveys 2021.
    https://doi.org/10.1145/3471140

[3] Qin, K. et al. "Attacking the DeFi Ecosystem with Flash Loans", 
    Financial Cryptography 2021.

[4] Certik. "Wormhole Bridge Exploit Analysis", 2022.
    https://certik.medium.com/wormhole-bridge-exploit-analysis-5068d79cbb71

[5] Kudelski Security. "The Poly Network Hack Explained", 2021.
    https://research.kudelskisecurity.com/2021/08/12/the-poly-network-hack-explained/

[6] Elliptic. "Analysis: Nomad loses $156 million in seventh major 
    crypto bridge exploit of 2022", 2022.
    https://www.elliptic.co/blog/analysis-nomad-loses-156-million