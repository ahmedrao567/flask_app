from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():


    return "<h1>hello this is ahmed deploying the app on rocky server going to push it.=..= 31 MARCH 2026 kubernetes checking </h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050) 