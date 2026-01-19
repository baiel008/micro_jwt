FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY req.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r req.txt

COPY . /app/

RUN chmod +x /app/manage.py

EXPOSE 8002

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8002", "mysite.wsgi:application"]