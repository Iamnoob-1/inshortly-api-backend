import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env contents

API_KEY = os.getenv("GEMINI_API_KEY")

def summarise_text(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
    
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [{"text": f"Summarise this text:\n{text}"}]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Failed to summarise: {str(e)}"
