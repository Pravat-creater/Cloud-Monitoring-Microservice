#!/bin/bash

docker build -t cloud-monitor .

docker run \
-e AWS_REGION=ap-south-1 \
-e INSTANCE_ID=i-1234567890abcdef0 \
cloud-monitor
