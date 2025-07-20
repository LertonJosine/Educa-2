#!/bin/sh

# Faz as migrações
python manage.py makemigrations
python manage.py migrate

# Depois inicia o servidor
gunicorn --bind 0.0.0.0:8000 educa.wsgi:application
