FROM python:3.12-slim

WORKDIR /app

# Instala dependencias primero para aprovechar la caché de capas de Docker.
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del backend y el frontend.
COPY backend/ ./backend/
COPY frontend/ ./frontend/

WORKDIR /app/backend

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
