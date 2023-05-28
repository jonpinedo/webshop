#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput

python manage.py loaddata initial.json
gunicorn -b unix:/run/socket.sock webshop.wsgi:application --access-logfile - --error-logfile -