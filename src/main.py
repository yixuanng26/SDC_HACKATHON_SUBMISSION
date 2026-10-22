import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load credentials from Replit Secrets
RUNPOD_API_KEY = os.environ.get("RUNPOD_API_KEY")
DEEPSEEK_ENDPOINT_ID = os.environ.get("DEEPSEEK_ENDPOINT_ID")
RUNPOD_ENDPOINT_ID = os.environ.get("RUNPOD_ENDPOINT_ID")

def call_deepseek_chat(user_message):
    url = f"https://api.runpod.ai/v2/{DEEPSEEK_ENDPOINT_ID}/runsync"
    headers = {
        "Authorization": f"Bearer {RUNPOD_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "input": {
            "prompt": user_message
        }
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        res_data = response.json()
        if "output" in res_data:
            output = res_data["output"]
            if isinstance(output, list) and len(output) > 0:
                return output[0].get("text", str(output[0]))
            return str(output)
        return "Thinking... (No text output received)"
    except Exception as e:
        print("❌ DeepSeek API call error:", e)
        return "Sorry, I am having trouble reaching DeepSeek right now."

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "Empty message"}), 400
    reply = call_deepseek_chat(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
