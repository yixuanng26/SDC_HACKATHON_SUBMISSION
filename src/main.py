import os
import requests

RUNPOD_API_KEY = os.getenv("RUNPOD_API_KEY", "")
RUNPOD_ENDPOINT_ID = os.getenv("RUNPOD_ENDPOINT_ID", "rg88ptje13dkwa")

def fetch_ai_career_insights(prompt_text: str) -> dict:
    if not RUNPOD_API_KEY:
        print("Warning: RUNPOD_API_KEY is not set. Using local fallback.")
        return {
            "status": "fallback",
            "message": "Local fallback: Default career path active."
        }

    url = f"https://api.runpod.ai/v2/{RUNPOD_ENDPOINT_ID}/runsync"
    headers = {
        "Authorization": f"Bearer {RUNPOD_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "input": {
            "prompt": prompt_text
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"RunPod API Request Failed: {e}")
        return {"status": "error", "error": str(e)}

def main() -> None:
    print("Starting MyFuture Career AI Service...")
    test_prompt = "I want to become a Data Analyst in Malaysia."
    result = fetch_ai_career_insights(test_prompt)
    
    print("\n--- AI Insights Result ---")
    print(result)

if __name__ == "__main__":
    main()
