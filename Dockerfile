# Utiliza una imagen base de Python 3.10.6
FROM python:3.10.6-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el contenido de la aplicación al contenedor
COPY . .

# Expone el puerto 8000 para acceder a la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación cuando se ejecute el contenedor
CMD ["python", "-m", "uvicorn", "app:app", "--reload"]
