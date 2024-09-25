# Imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios a la imagen
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instala las dependencias
RUN pip install -r requirements.txt

# Exponemos el puerto en el que Flask correrá
EXPOSE 5001

# Ejecutamos la aplicación
CMD ["python", "app.py"]
