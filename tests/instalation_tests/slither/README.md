# Slither2 - Herramienta de Análisis de Seguridad de Contratos Inteligentes

Una herramienta basada en Python para analizar contratos inteligentes Solidity utilizando el framework de análisis estático Slither.

## Características

- Analiza contratos Solidity para detectar vulnerabilidades de seguridad
- Detección automatizada de problemas comunes (reentrancia, overflow de enteros, etc.)
- Fácil integración con flujos de trabajo de desarrollo existentes
- Soporte para análisis en lote de múltiples contratos

## Instalación

1. Clone el repositorio:
```bash
git clone <url-del-repositorio>
cd slither2
```

2. Instale las dependencias usando UV:
```bash
uv sync
```

3. (Opcional) Instale el compilador de Solidity:
```bash
solc-select install 0.4.25
solc-select use 0.4.25
```

## Uso

### Análisis Básico

Analizar un solo contrato:
```bash
uv run slither not-so-smart-contracts/reentrancy/Reentrancy.sol
```

### Uso Programático

También puede utilizar el analizador mediante programación:

```python
from slither import Slither

# Inicializar Slither con un contrato
slither = Slither("ruta/al/contrato.sol")

# Obtener detectores
detectors = slither.detectors

# Imprimir resultados
for detector in detectors:
    print(detector)
```

## Estructura del Proyecto

```
slither2/
├── analyze_contract.py     # Script de análisis de contratos
├── main.py                # Punto de entrada
├── not-so-smart-contracts/ # Contratos vulnerables de muestra
├── test_contracts.py      # Pruebas para el analizador
├── pyproject.toml         # Configuración del proyecto
└── README.md              # Este archivo
```

## Contratos de Muestra

El directorio `not-so-smart-contracts/` contiene varios contratos inteligentes vulnerables para pruebas:

- Vulnerabilidades de reentrancia
- Overflow/underflow de enteros
- Aleatoriedad deficiente
- Honeypots
- Nombres incorrectos de constructores
- Vectores de denegación de servicio

## Ejecución de Pruebas

Ejecute la suite de pruebas:
```bash
uv run python test_contracts.py
```

## Requisitos

- Python 3.12+
- Analizador Slither
- Compilador de Solidity (solc)

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo LICENSE para más detalles.

## Agradecimientos

- [Slither](https://github.com/crytic/slither) - El framework de análisis estático utilizado
- [Solc-select](https://github.com/crytic/solc-select) - Gestión de versiones de Solidity