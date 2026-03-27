from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello! This is Ahmed deploying the app on Rocky server...</h1>"

# Add this webhook route
@app.route("/github_webhook", methods=["POST"])
def github_webhook():
    data = request.json
    print("Webhook payload received:", data)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)