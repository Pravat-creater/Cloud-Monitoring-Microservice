import boto3
from datetime import datetime, timedelta
from config import AWS_REGION, INSTANCE_ID


def get_cloudwatch_client():
    """
    Creates a CloudWatch client using IAM role or configured AWS credentials.
    """
    return boto3.client("cloudwatch", region_name=AWS_REGION)


def fetch_cpu_utilization():
    """
    Fetch CPU utilization metrics for the given EC2 instance.
    """
    cloudwatch = get_cloudwatch_client()

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=10)

    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[
            {"Name": "InstanceId", "Value": INSTANCE_ID}
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=["Average"],
    )

    return response


def main():
    try:
        print("Fetching CPU utilization metrics...")
        data = fetch_cpu_utilization()
        print("CloudWatch Response:")
        print(data)

    except Exception as e:
        print("Error occurred:", str(e))


if name == "main":
    main()
