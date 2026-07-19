import boto3

ct = boto3.client("cloudtrail")

response = ct.describe_trails()

print("CloudTrail Trails:\n")

for trail in response["trailList"]:
    print(trail["Name"])
