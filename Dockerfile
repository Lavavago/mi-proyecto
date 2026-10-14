FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
CMD ["python", "-c", "from src.calculadora import sumar; print('App lista:', sumar(2, 3))"]
