🚀 YOLO Pressure Classification API (Docker + AWS Deployment)
📌 Project Overview

This project implements a complete end-to-end machine learning pipeline for pressure-based body position classification using YOLO (Ultralytics) and ONNX.

The system:

Converts 12x6 pressure sensor grid data (72 values) into heatmap images

Trains a YOLO classification model

Exports the model to ONNX

Wraps inference inside a FastAPI REST API

Containerizes the service using Docker

Deploys it on AWS EC2 (Free Tier)

Serves predictions publicly via HTTP

🧠 Problem Statement

Given 72 pressure readings from a Sensomatt grid (12 rows × 6 columns), classify body posture into:

left

right

prone

supine

📊 Data Processing Pipeline
1️⃣ Pressure Grid → Heatmap

Input: 72 pressure values

Reshaped into 12x6 grid

Normalized (0–255)

Converted to heatmap using OpenCV colormap

Resized to 512×512 for YOLO

🤖 Model

Model: YOLO Classification (Ultralytics)

Exported to: ONNX

Task: classify

Deployment: CPU inference

🏗️ API Architecture

Built using:

FastAPI

Uvicorn

ONNX Runtime

Docker

Endpoints
Health Check
GET /health


Response:

{"status":"ok"}

Predict
POST /predict


Upload image file:

Example:

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

Build locally:

docker build -t popu-yolo-api .
docker run -p 8080:8080 popu-yolo-api

☁️ AWS Deployment (Free Tier)

Deployed using:

EC2 (t2.micro)

Ubuntu 24.04

Docker

AWS ECR

Architecture:

Internet
   ↓
EC2 Instance (Free Tier)
   ↓
Docker Container
   ↓
YOLO API


Public API Example:

http://<PUBLIC_IP>/health

💰 Cost Optimization

Uses EC2 Free Tier (750 hrs/month)

No Load Balancer

No Fargate

No GPU

30GB EBS (within free limits)

🔒 Security Notes

AWS credentials are NOT included

PEM keys are NOT stored in repository

.gitignore prevents sensitive files

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

ONNX

FastAPI

Docker

AWS EC2

AWS ECR

Linux (Ubuntu)

📈 What This Demonstrates

This project demonstrates:

ML model training

Data preprocessing

Model export

API development

Docker containerization

Cloud deployment

AWS networking & security

Cost-aware cloud architecture

🚀 Future Improvements

Add HTTPS (SSL)

Add authentication

Add batch inference endpoint

Use CI/CD pipeline

Add monitoring

Optimize Docker image size

Switch to serverless deployment

👨‍💻 Author

Sagar
Machine Learning & Cloud Deployment Practice Project

⭐ If you found this interesting, feel free to fork or contribute.
🔥 Optional Upgrade

If you want, I can also:

Make this README look more research-oriented

Make it resume-ready

Add architecture diagrams

Add badges (Docker, AWS, Python, YOLO)

Add screenshots section

Make it enterprise-grade documentation

Just tell me 👍
