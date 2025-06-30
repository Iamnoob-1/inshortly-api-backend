import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-pro")

def summarise_text(prompt):
    response = model.generate_content(f"Summarize this article:\n\n{prompt}")
    return response.text.strip()
