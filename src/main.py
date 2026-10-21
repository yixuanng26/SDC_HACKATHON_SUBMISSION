import os
import requests

# Retrieve credentials securely from Replit Secrets
RUNPOD_API_KEY = os.environ.get("RUNPOD_API_KEY")
RUNPOD_ENDPOINT_ID = os.environ.get("RUNPOD_ENDPOINT_ID")

url = f"https://api.runpod.ai/v2/{RUNPOD_ENDPOINT_ID}/runsync"

headers = {
    "Authorization": f"Bearer {RUNPOD_API_KEY}",
    "Content-Type": "application/json"
}

# Pass the prompt to your handler
payload = {
    "input": {
        "prompt": "Data Engineering Career Path"
    }
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
