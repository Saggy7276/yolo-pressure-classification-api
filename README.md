🚀 YOLO Pressure Classification API
Dockerized ML Inference + AWS EC2 Deployment
📌 Project Overview

This project implements a complete end-to-end machine learning pipeline for pressure-based body position classification using Ultralytics YOLO (classification) and ONNX Runtime.

The system:

Converts 12×6 pressure sensor grid data (72 values) into heatmap images

Trains a YOLO classification model

Exports the model to ONNX

Wraps inference inside a FastAPI REST API

Containerizes the service using Docker

Deploys the service on AWS EC2 (Free Tier)

Serves real-time predictions via HTTP

🧠 Problem Statement

Given 72 pressure readings from a Sensomatt grid (12 rows × 6 columns), classify body posture into:

left

right

prone

supine

📊 Data Processing Pipeline
🔄 Pressure Grid → Heatmap

Input: 72 pressure values

Reshape into 12×6 grid

Normalize values to range 0–255

Convert to heatmap using OpenCV colormap

Resize to 512×512 for YOLO

This allows sensor data to be interpreted visually by a CNN-based classifier.

🤖 Model

Model Type: YOLO Classification (Ultralytics)

Export Format: ONNX

Task: classify

Inference: CPU-based

Deployment Runtime: ONNX Runtime

🏗️ System Architecture
Pressure Sensor Data
        ↓
Heatmap Conversion
        ↓
YOLO Classification Model (ONNX)
        ↓
FastAPI REST API
        ↓
Docker Container
        ↓
AWS EC2 (Free Tier)
        ↓
Public HTTP Endpoint

🔌 API Endpoints
✅ Health Check
GET /health


Response:

{
  "status": "ok"
}

🔮 Predict
POST /predict


Upload image file:

curl -F "file=@test.jpg" http://<SERVER_IP>/predict


Response:

{
  "top1": {
    "class_id": 0,
    "class_name": "left",
    "conf": 0.99999
  },
  "top5": [...]
}

🐳 Docker Deployment
Build Locally
docker build -t popu-yolo-api .

Run Locally
docker run -p 8080:8080 popu-yolo-api


Access locally:

http://localhost:8080/health

☁️ AWS Deployment (Free Tier)

Deployed using:

EC2 (t2.micro – Free Tier)

Ubuntu 24.04

Docker

AWS ECR

Architecture
Internet
   ↓
EC2 Instance (Free Tier)
   ↓
Docker Container
   ↓
YOLO API


Public API Example:

http://<PUBLIC_IP>/health

💰 Cost Optimization Strategy

Uses EC2 Free Tier (750 hours/month)

No Load Balancer

No ECS/Fargate

No GPU

30GB EBS (within Free Tier limits)

Container runs directly on EC2

🔒 Security Notes

AWS credentials are NOT included

PEM key files are excluded via .gitignore

Model weights are excluded

IAM user with programmatic access used for deployment

Security group restricts SSH to personal IP

📂 Project Structure
yolo-popu-api/
│
├── app/
│   └── main.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore

🛠️ Technologies Used

Python

Ultralytics YOLO

ONNX Runtime

FastAPI

Docker

AWS EC2

AWS ECR

Linux (Ubuntu)

📈 What This Project Demonstrates

ML model training & export

Data preprocessing & visualization

REST API development

Docker containerization

Cloud deployment (AWS)

DevOps fundamentals

Cost-aware cloud architecture

Public ML inference serving

🚀 Future Improvements

HTTPS with SSL (Let's Encrypt)

Authentication layer (API key)

Batch inference endpoint

CI/CD pipeline (GitHub Actions)

Monitoring & logging

Docker image size optimization

Move to serverless architecture

Domain name integration

👨‍💻 Author

Sagar
Machine Learning & Cloud Deployment Practice Project

⭐ If you found this project interesting, feel free to fork or contribute.

🚀 If You Want Next-Level Polish

I can help you:

Add professional badges (Docker, AWS, Python, YOLO)

Add architecture diagram image

Make it recruiter-ready

Optimize README for ML engineer roles

Write a LinkedIn post about this deployment

Turn this into a resume bullet

Tell me what you want next 👌
