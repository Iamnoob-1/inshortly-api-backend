import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash")

def summarize_text(input_text):
    prompt = f"Summarize the following article:\n\n{input_text}"
    response = model.generate_content(prompt)
    return response.text.strip()
