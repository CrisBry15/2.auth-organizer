FROM python:3.11-slim

# Variables de entorno para evitar errores en contenedor
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias necesarias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    libpq-dev \
    build-essential \
    libssl-dev \
    pkg-config \
    curl \
    && apt-get clean

# Crear y entrar al directorio de la app
WORKDIR /app

# Copiar todo el contenido del proyecto al contenedor
COPY . .

# Instalar dependencias Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Flask
EXPOSE 5000

# Comando de inicio (modo QA/desarrollo)
CMD ["python", "run.py"]
