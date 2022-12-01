FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /app
WORKDIR /app
RUN apk add --no-cache python3-dev build-base linux-headers pcre-dev \
 && pip install --upgrade pip \
 && pip install "uWSGI>=2.0,<2.1" \
 && pip install -r /app/requirements.txt --no-cache-dir \
 && rm -rf /etc/apk && rm -rf /lib/apk && rm -rf /usr/share/apk && rm -rf /var/lib/apk \
 && chmod -R 755 /app/static \
 && chmod -R 755 /app/media \
 && addgroup -S app && adduser -S app -G app \
 && chown -R app:app /app \
 && chmod +x /app/scripts/* \
 && mkdir -p /tmp/uwsgi/

