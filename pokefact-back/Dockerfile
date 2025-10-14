# Usa una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del backend al contenedor
COPY . /app

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expón el puerto donde correrá FastAPI
EXPOSE 8000

# Comando para iniciar la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
