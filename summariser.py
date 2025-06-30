import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Correct way to get the model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

def summarise_text(prompt):
    response = model.generate_content(f"Summarize this article:\n\n{prompt}")
    return response.text.strip()
