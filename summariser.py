import requests

def summarise_text(prompt):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Content-Type": "application/json"}

    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        result = response.json()
        return result[0]["summary_text"]
    except Exception as e:
        return f"Error in response: {str(e)}"
