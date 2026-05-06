# Slither Usage Guide

## Analizar un contrato inteligente

Cada contrato requiere una versión específica de Solidity. Si la versión instalada no coincide, slither fallará.

### Opción A: Análisis directo con Slither

#### 1. Verificar la versión requerida

Revisa la primera línea del contrato:
```bash
head -1 contrato.sol
```

Busca la línea `pragma solidity ^X.Y.Z;`

#### 2. Instalar y seleccionar la versión correcta

```bash
pip install solc-select
solc-select install X.Y.Z
solc-select use X.Y.Z
```

#### 3. Ejecutar slither

```bash
source .venv/bin/activate
slither ruta/al/contrato.sol
```

### Opción B: Usar script de Python (cuenta vulnerabilidades)

El script `analyze_contract.py` detecta automáticamente la versión de Solidity, la instala y cuenta las vulnerabilidades por severidad.

#### 1. Instalar dependencias

```bash
source .venv/bin/activate
pip install slither-analyzer solc-select
```

#### 2. Ejecutar el script (automático)

```bash
python analyze_contract.py ruta/al/contrato.sol
```

El script detecta automáticamente la versión del pragma y configura solc-select.

Salida esperada (formato de test):
```
Setting up Solidity version 0.4.15...
Using Solidity 0.4.15
Contract: Reentrancy.sol
Solidity Version: 0.4.15
Execution: Success
Vulnerabilities:
  High: 1
  Informational: 9
```

## Ejemplo completo (Opción B)

```bash
# Activar entorno virtual
source .venv/bin/activate

# Instalar herramientas
pip install slither-analyzer solc-select

# Configurar versión (ejemplo: 0.4.15)
solc-select install 0.4.15
solc-select use 0.4.15

# Ejecutar análisis con script
python analyze_contract.py not-so-smart-contracts/reentrancy/Reentrancy.sol
```
