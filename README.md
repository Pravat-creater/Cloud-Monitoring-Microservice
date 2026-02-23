# Cloud-Monitoring-Microservice
# Containerized Cloud Monitoring Microservice

## Project Overview
This project is a Dockerized Python microservice that securely fetches AWS CloudWatch CPU utilization metrics using IAM role-based access.

## Technologies Used
- Python
- boto3 (AWS SDK for Python)
- AWS CLI
- Docker
- Kubernetes (conceptual deployment)
- IAM Role-based access control

## Architecture
1. AWS CLI used for credential configuration.
2. IAM role provides secure access to CloudWatch.
3. Python (boto3) fetches EC2 CPU utilization metrics.
4. Docker ensures portability and consistent runtime.
5. Kubernetes deployment file demonstrates scaling capability.

## How to Run Locally

### Step 1: Configure AWS CLI
aws configure

### Step 2: Build Docker Image
docker build -t cloud-monitor .

### Step 3: Run Container
docker run \
-e AWS_REGION=ap-south-1 \
-e INSTANCE_ID=your-instance-id \
cloud-monitor

## Production Setup
- Attach IAM role with CloudWatchReadOnlyAccess to EC2.
- Deploy using Kubernetes deployment.yaml.
