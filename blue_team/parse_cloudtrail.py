import gzip
import json
import glob
import os

# Find the latest downloaded .json.gz file
files = glob.glob("*.json.gz")

if not files:
    print("No CloudTrail .json.gz files found.")
    exit()

latest_file = max(files, key=os.path.getmtime)

print(f"Parsing: {latest_file}")

with gzip.open(latest_file, "rt") as f:
    data = json.load(f)

records = data.get("Records", [])

print(f"\nTotal Events: {len(records)}\n")

for event in records:
    print("-------------------------------")
    print("Time       :", event.get("eventTime"))
    print("Event      :", event.get("eventName"))
    print("Service    :", event.get("eventSource"))
    print("User       :", event.get("userIdentity", {}).get("type"))

    username = event.get("userIdentity", {}).get("userName")
    if username:
        print("Username   :", username)

    print("Source IP  :", event.get("sourceIPAddress"))
    print("Region     :", event.get("awsRegion"))
