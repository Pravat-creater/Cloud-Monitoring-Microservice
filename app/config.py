import os

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
INSTANCE_ID = os.getenv("INSTANCE_ID")

if not INSTANCE_ID:
    raise ValueError("INSTANCE_ID environment variable not set")
