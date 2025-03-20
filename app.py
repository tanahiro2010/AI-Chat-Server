from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text-generation", model="rinna/japanese-gpt-1b")

@app.route("/")
def home():
    return "Hello World!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    result = generator(data["prompt"], max_length=1000)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
