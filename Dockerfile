FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# OpenCV runtime deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 libsm6 libxext6 libxrender1 libgl1 libgomp1 \
  && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
# Copy your model into image (or mount it at runtime)
COPY best.onnx /app/best.onnx

EXPOSE 8080
ENV MODEL_PATH=/app/best.onnx
ENV IMGSZ=512

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
