# Usa la imagen base de alpine
FROM alpine:latest

# Actualiza e instala los paquetes necesarios
RUN apk update && \
    apk add python3 py3-pip py3-virtualenv postgresql-dev gcc python3-dev musl-dev supervisor && \
    apk upgrade --no-cache

# Copia el proyecto a la carpeta /app
COPY . /app

# Establece directorio actual
WORKDIR /app

# Reemplaza supervidord.conf
RUN mv supervisord.conf /etc/supervisord.conf

# Crea entorno virtual e instala dependencias
RUN python3 -m venv env && \
    source env/bin/activate && \
    pip install gunicorn && \
    pip install -r requirements.txt && \
    deactivate

RUN mkdir /var/log/gunicorn 

# Corre Gunicorn
CMD ["sh", "-c", "source env/bin/activate && python3 manage.py migrate && supervisord -c /etc/supervisord.conf && supervisorctl update && supervisorctl status && tail -f /dev/null"]