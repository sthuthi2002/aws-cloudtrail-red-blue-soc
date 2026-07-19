import boto3
import os

BUCKET_NAME = "cloud-red-blue-logs-6f5e9c29"
PREFIX = "AWSLogs/256148542278/CloudTrail/"

s3 = boto3.client("s3")

response = s3.list_objects_v2(
    Bucket=BUCKET_NAME,
    Prefix=PREFIX
)

files = response.get("Contents", [])

if not files:
    print("No CloudTrail logs found.")
    exit()

latest = max(files, key=lambda x: x["LastModified"])

key = latest["Key"]
filename = os.path.basename(key)

print(f"Downloading: {filename}")

s3.download_file(
    BUCKET_NAME,
    key,
    filename
)

print("Download complete.")
