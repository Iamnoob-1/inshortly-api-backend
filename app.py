from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from summariser import summarise_text

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Inshortly Gemini Summarizer is running!"

@app.route("/generate", methods=["POST"])
def generate_summary():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    summary = summarise_text(text)
    return jsonify({"summary": summary})

# 🔧 This must be outside any function
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
