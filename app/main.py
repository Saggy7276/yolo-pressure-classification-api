import os
import io
import numpy as np
import cv2
from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO

app = FastAPI(title="PoPu YOLO-CLS API")

MODEL_PATH = os.getenv("MODEL_PATH", "best.pt")
IMGSZ = int(os.getenv("IMGSZ", "512"))

model = YOLO(MODEL_PATH, task="classify")


def bytes_to_bgr_image(file_bytes: bytes):
    arr = np.frombuffer(file_bytes, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)  # BGR
    if img is None:
        raise ValueError("Could not decode image")
    return img

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    b = await file.read()
    img = bytes_to_bgr_image(b)

    # Ultralytics classify accepts numpy image directly
    results = model.predict(img, imgsz=IMGSZ, verbose=False)

    r = results[0]
    # r.probs contains probabilities; r.names maps index->class name
    top1_idx = int(r.probs.top1)
    top1_conf = float(r.probs.top1conf)
    top1_name = r.names[top1_idx]

    # Top-5
    top5_idx = list(map(int, r.probs.top5))
    top5_conf = list(map(float, r.probs.top5conf))
    top5 = [{"class_id": i, "class_name": r.names[i], "conf": c} for i, c in zip(top5_idx, top5_conf)]

    return {
        "top1": {"class_id": top1_idx, "class_name": top1_name, "conf": top1_conf},
        "top5": top5,
    }
