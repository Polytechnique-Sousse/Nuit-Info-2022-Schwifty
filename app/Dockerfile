FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /app
WORKDIR /app
RUN apk add --no-cache python3-dev build-base linux-headers pcre-dev
RUN pip install --upgrade pip
RUN pip install "uWSGI>=2.0,<2.1"
RUN pip install -r /app/requirements.txt --no-cache-dir
RUN rm -rf /etc/apk && rm -rf /lib/apk && rm -rf /usr/share/apk && rm -rf /var/lib/apk
RUN chmod -R 755 /app/static
RUN chmod -R 755 /app/media
RUN chmod +x /app/scripts/*
RUN mkdir -p /tmp/uwsgi/