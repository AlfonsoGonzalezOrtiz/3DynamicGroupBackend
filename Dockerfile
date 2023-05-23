# Utiliza una imagen base de Python
FROM python:3.10.-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el contenido de la aplicación al contenedor
COPY . .


# Expone el puerto 1234 para acceder a la aplicación desde el exterior del contenedor
EXPOSE 8000

# Define el comando de inicio de la aplicación
CMD ["python.exe","-m","uvicorn","app:app","--reload"]
