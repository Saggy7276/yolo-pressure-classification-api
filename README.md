# 🚀 YOLO Pressure Classification API
### Dockerized ML Inference + AWS EC2 Deployment

---

## 📌 Project Overview

This project implements a complete end-to-end machine learning pipeline for **pressure-based body position classification** using **Ultralytics YOLO (classification)** and **ONNX Runtime**.

The system:

- Converts 12×6 pressure sensor grid data (72 values) into heatmap images
- Trains a YOLO classification model
- Exports the model to ONNX
- Wraps inference inside a FastAPI REST API
- Containerizes the service using Docker
- Deploys the service on AWS EC2 (Free Tier)
- Serves real-time predictions via HTTP

---

## 🧠 Problem Statement

Given 72 pressure readings from a Sensomatt grid (12 rows × 6 columns), classify body posture into:

- left
- right
- prone
- supine
