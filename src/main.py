import os
import requests

# Retrieve credentials securely from Replit Secrets
RUNPOD_API_KEY = os.environ.get("RUNPOD_API_KEY")
RUNPOD_ENDPOINT_ID = os.environ.get("RUNPOD_ENDPOINT_ID")

# Construct the RunPod synchronous API endpoint URL
url = f"https://api.runpod.ai/v2/{RUNPOD_ENDPOINT_ID}/runsync"

headers = {
    "Authorization": f"Bearer {RUNPOD_API_KEY}",
    "Content-Type": "application/json"
}

# Payload required for Wan2.2 Image-to-Video (I2V)
# Replace the image URL with a direct public link to your avatar image
payload = {
    "input": {
        "prompt": "Data Engineering Career Path, talking avatar, smooth motion",
        "image": "https://example.com/your-avatar-image.jpg" 
    }
}

print("Sending request to RunPod WAN 2.2 I2V model... Please wait (this can take a moment).")

response = requests.post(url, json=payload, headers=headers)
result = response.json()

print("RunPod Response:", result)

# Check execution status and extract video URL if successful
if result.get("status") == "COMPLETED":
    output = result.get("output", {})
    # Depending on the exact template wrapper, the video link might be under video_url or delay_url
    video_url = output.get("video_url") or output.get("delay_url")
    
    if video_url:
        print(f"\nVideo generated successfully! Download link: {video_url}")
    else:
        print("\nTask completed, but could not find the video URL in the output structure.")
else:
    print(f"\nTask status: {result.get('status')}")
