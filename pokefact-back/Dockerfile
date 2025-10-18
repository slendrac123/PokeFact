# Imagen base
FROM python:3.12-slim

# Crear y movernos al directorio de trabajo
WORKDIR /app

# Copiar archivos de requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto del backend
EXPOSE 8000

# Comando para iniciar la app
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Comando inicializador - Espera que la BD esté lista antes de iniciar
CMD ["sh", "-c", "sleep 10 && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]