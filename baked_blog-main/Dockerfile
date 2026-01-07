FROM python:3.11.2-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libjpeg-dev \
    gcc \
    libpq-dev \
    default-mysql-client \
    python3-cryptography
RUN pip wheel --wheel-dir /app/wheels -r requirements.txt

FROM python:3.11.2-slim 
WORKDIR /app
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*
COPY . .

CMD ["python","manage.py","runserver","0.0.0.0:8080"]

