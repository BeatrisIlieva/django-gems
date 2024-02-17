FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
#COPY . /app/

COPY manage.py /app/manage.py
COPY staticfiles /app/staticfiles
COPY templates /app/templates
COPY django_gems /app/django_gems
