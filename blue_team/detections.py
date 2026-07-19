import gzip
import json
import glob
import os

files = glob.glob("*.json.gz")

if not files:
    print("No CloudTrail logs found.")
    exit()

latest = max(files, key=os.path.getmtime)

with gzip.open(latest, "rt") as f:
    data = json.load(f)

print("=" * 45)
print("      CLOUD SECURITY ALERT REPORT")
print("=" * 45)

alerts = 0

for event in data["Records"]:

    event_name = event.get("eventName")
    identity = event.get("userIdentity", {}).get("type")
    username = event.get("userIdentity", {}).get("userName", "N/A")

    if identity == "Root":
        print(f"[HIGH] Root account activity")
        print(f"       Event : {event_name}")
        alerts += 1

    elif event_name == "ListUsers":
        print(f"[MEDIUM] IAM enumeration")
        print(f"         User : {username}")
        alerts += 1

    elif event_name == "DescribeTrails":
        print(f"[MEDIUM] CloudTrail reconnaissance")
        alerts += 1

    elif event_name == "ListBuckets":
        print(f"[LOW] S3 bucket enumeration")
        alerts += 1

    elif event_name == "DescribeInstances":
        print(f"[LOW] EC2 discovery")
        alerts += 1

print("\n--------------------------------")
print(f"Total Alerts: {alerts}")
print("--------------------------------")
