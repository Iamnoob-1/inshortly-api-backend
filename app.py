from flask import Flask, request, jsonify
from flask_cors import CORS
from summariser import summarise_text

app = Flask(__name__)
CORS(app)

@app.route("/summarise", methods=["POST"])
def summarise():
    data = request.get_json()
    input_text = data.get("text")

    if not input_text:
        return jsonify({"error": "Missing 'text' field"}), 400

    summary = summarise_text(input_text)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
