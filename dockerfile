# Usa una imagen de Python
FROM python:3.10-slim

# Define el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt y luego instala las dependencias
COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
RUN python -m venv --symlinks /opt/venv && /opt/venv/bin/pip install -r requirements.txt


# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Ejecuta las migraciones y el servidor en el puerto especificado por Railway
# CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:$PORT"]
CMD ["python", "manage.py", "migrate", "&&", "python", "manage.py", "collectstatic", "--noinput", "&&", "python", "manage.py", "runserver", "0.0.0.0:${PORT}"]

