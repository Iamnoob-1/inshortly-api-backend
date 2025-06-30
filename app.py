from flask import Flask, request, jsonify
from flask_cors import CORS
from summariser import summarize_text

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Gemini Summarizer Backend Running"

@app.route("/generate", methods=["POST"])
def generate_summary():
    try:
        data = request.get_json()
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400

        summary = summarize_text(text)
        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
