import json
import gzip
import glob
import os
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(
    "http://localhost:9200",
    request_timeout=30
)

try:
    print("Connected!")
    print(es.info()["version"]["number"])
except Exception as e:
    print("Connection failed:", e)
    exit()

# Find latest CloudTrail log
files = glob.glob("*.json.gz")

if not files:
    print("No CloudTrail logs found.")
    exit()

latest = max(files, key=os.path.getmtime)

print(f"Uploading {latest}")

with gzip.open(latest, "rt") as f:
    data = json.load(f)

count = 0

for event in data["Records"]:
    doc = {
        "eventTime": event.get("eventTime"),
        "eventName": event.get("eventName"),
        "eventSource": event.get("eventSource"),
        "userName": event.get("userIdentity", {}).get("userName"),
        "identityType": event.get("userIdentity", {}).get("type"),
        "sourceIPAddress": event.get("sourceIPAddress"),
        "awsRegion": event.get("awsRegion")
    }

    es.index(
        index="cloudtrail-events",
        document=doc
    )

    count += 1

print(f"\nUploaded {count} events successfully.")
