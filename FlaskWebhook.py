import os
from flask import Flask
from flask import request, jsonify
import json 

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "Welcome to Requirement to Developenet solutions !!! \n We are in process to build our website." 

def helloUser(personName):
    return "Hello " + personName + " from dialogflow-rest demo webhook!!!"


@app.route("/handleWebhookRequest", methods=['POST'])
def handleWebhookRequest():
    jsonRequestBody = request.get_json()
    #actionMethod = jsonRequestBody["queryResult"]["action"]

    jsonResponse = {"fulfillmentText": helloUser(jsonRequestBody["queryResult"]["parameters"]["person"]["name"])}
    return jsonify(jsonResponse)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
