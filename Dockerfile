# Usamos una base de Python oficial estable
FROM ubuntu:22.04

# Evitar que Python escriba archivos .pyc y forzar salida en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Evitar diálogos interactivos durante la instalación de paquetes
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    curl \
    git \
    tar \
    software-properties-common \
    build-essential \
    pkg-config \
    libcairo2-dev \
    python3 \
    python3-dev \
    python3-pip \
    && add-apt-repository -y ppa:ethereum/ethereum \
    && apt-get update && apt-get install -y solc \
    && rm -rf /var/lib/apt/lists/*


# Instalar solc (compilador de Solidity) mediante solc-select (usado por Slither)
RUN pip install --no-cache-dir solc-select && \
    solc-select install 0.8.20 && \
    solc-select use 0.8.20

# Instalar Echidna (Descarga directa del binario estático sin comprimir)
# Descargar e instalar Echidna con el nombre de archivo correcto
RUN curl -L https://github.com/crytic/echidna/releases/download/v2.3.2/echidna-2.3.2-x86_64-linux.tar.gz -o echidna.tar.gz \
    && tar -xvf echidna.tar.gz \
    && mv echidna /usr/local/bin/ \
    && rm echidna.tar.gz


# Instalar 'uv' para la gestión de dependencias de Python
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el resto del código de la aplicación
COPY . .

# Volver a sincronizar para registrar el paquete local (evmaudit)
RUN uv sync --frozen --no-cache

# Exponer el puerto en el que corre Uvicorn
EXPOSE 8080

# Arrancar la aplicación usando el entorno virtual creado por uv
CMD ["uv", "run", "python3", "-m", "uvicorn", "webapp.app:app", "--host", "0.0.0.0", "--port", "8080"]