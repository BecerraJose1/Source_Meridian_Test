# Usa la imagen de Python 3.12.3
FROM python:3.12.3

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos al contenedor
COPY . .

# Actualizar pip y instalar dependencias
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
