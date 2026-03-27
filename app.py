from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hi this ahmed running a flask app hello. now i chaneg the code for trigeering teh automtion  gaindhdjaj</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 