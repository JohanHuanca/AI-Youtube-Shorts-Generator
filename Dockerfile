# Usa una imagen base oficial de Python 3.10 slim
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala TODAS las dependencias del sistema, incluyendo los paquetes -dev de FFMPEG
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    libsm6 \
    libxext6 \
    pkg-config \
    build-essential \
    libavformat-dev \
    libswscale-dev \
    libswresample-dev \
    libavdevice-dev \
    libavfilter-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Define el comando para ejecutar la aplicación
CMD ["python", "-u", "main.py"]