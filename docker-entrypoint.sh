#!/bin/bash

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000

echo "Django docker is fully configured successfully."

exec "$@"