FROM --platform=$BUILDPLATFORM python:3.9-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM --platform=$TARGETPLATFORM python:3.9-slim
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY app.py .

EXPOSE 8080
CMD ["python", "app.py"]