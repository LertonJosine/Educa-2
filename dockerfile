FROM python:3.10-slim

WORKDIR /educa2

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .