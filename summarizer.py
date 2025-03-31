import requests
import os

API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-V3-0324"
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def summarize(text):
    payload = {
        "inputs": f"Summarize this: {text}",
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()

    if isinstance(result, list):
        return result[0].get("generated_text", "[No summary returned]")
    elif isinstance(result, dict) and "error" in result:
        return f"Error from HF API: {result['error']}"
    return str(result)