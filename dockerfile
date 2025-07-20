FROM python:3.10-slim

WORKDIR /educa2

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

CMD [ "sh" "-c" "gunicorn --bind 0.0.0.0:8000 educa:wsgi:application && python manage.py makemigrations && python manage.py migrate" ]
