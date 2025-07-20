FROM python:3.10-slim

WORKDIR /educa2

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERED=1

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

COPY . .

#CMD [ "sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 educa:wsgi:application" ]
