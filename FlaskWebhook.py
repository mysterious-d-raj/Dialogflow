import os
from flask import Flask
from flask import request, jsonify
import json 

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello from Python!"

@app.route("/name", methods=['GET'])
def helloUser():
    return "Hello " + request.args.get('username') + " to dialogflow-rest demo webhook!!!"


@app.route("/handleWebhookRequest", methods=['POST'])
def handleWebhookRequest():
    jsonRequestBody = request.get_json()
    jsonResponse = {"fulfillmentText": jsonRequestBody}
    return jsonify(jsonResponse)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
