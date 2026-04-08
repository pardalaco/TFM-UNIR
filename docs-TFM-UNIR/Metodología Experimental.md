# Metodología Experimental y Desarrollo del Analizador

## 1. Objetivos del analizador
- Detectar vulnerabilidades automáticamente
- Integrar herramientas existentes (Slither, Mythril)
- Generar informes estructurados
- Reducir falsos positivos vs herramientas individuales

## 2. Arquitectura del sistema
- Diseño modular
- Pipeline de análisis
- Integración de herramientas
- Sistema de reportes

## 3. Tecnologías utilizadas
- Python 3.x
- Slither API
- Mythril CLI
- Flask (si haces web)
- Librerías: web3.py, solc, etc.

## 4. Datasets de evaluación
4.1. SmartBugs Wild
4.2. Contratos de ataques reales
4.3. Contratos de producción verificados
4.4. Contratos sintéticos de prueba

## 5. Métricas de evaluación
- Precisión, Recall, F1-Score
- Tasa de falsos positivos
- Tiempo de ejecución
- Cobertura de vulnerabilidades

## 6. Protocolo experimental
6.1. Configuración del entorno
6.2. Proceso de análisis
6.3. Validación de resultados
6.4. Comparación con baseline (Slither solo, Mythril solo)

## 7. Implementación práctica
7.1. Código fuente del analizador
7.2. Integración de herramientas
7.3. Sistema de reportes
7.4. Interfaz de usuario (CLI/Web)

## 8. Casos de prueba
8.1. Contratos vulnerables conocidos
8.2. Contratos seguros (validación de falsos positivos)
8.3. Contratos de complejidad variable

## Referencias
[1] Durieux, T. et al. "Empirical Review of Automated Analysis Tools on 
    47,587 Ethereum Smart Contracts", ASE 2020.
    https://arxiv.org/abs/1910.10601

[2] Ferreira, J. et al. "SmartBugs: A Framework to Analyze Solidity 
    Smart Contracts", ASE 2020.
    https://doi.org/10.1145/3324884.3416939

[3] Torres, C.F. et al. "The Art of The Scam: Demystifying Honeypots 
    in Ethereum Smart Contracts", USENIX Security 2019.
    https://www.usenix.org/conference/usenixsecurity19/presentation/torres

[4] Parizi, R.M. et al. "Empirical Vulnerability Analysis of Automated 
    Smart Contracts Security Testing on Blockchains", CASCON 2018.
    https://doi.org/10.5555/3291291.3291297