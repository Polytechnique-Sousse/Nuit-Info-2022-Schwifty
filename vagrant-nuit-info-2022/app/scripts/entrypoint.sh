#!/bin/sh

python /app/manage.py makemigrations
python /app/manage.py migrate
python /app/manage.py loaddata /app/init_admin.json
python /app/manage.py collectstatic --noinput
uwsgi --ini app.uwsgi.ini