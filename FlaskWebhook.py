import os
from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello from Python!"

@app.route("/", methods=['GET'])
def helloUser(name):
    return "Hello " + name + " to dialogflow-rest demo webhook!!!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
