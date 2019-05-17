import os
from bottle import post, run, request
import requests
OPENFISCA_URL = "https://openfisca-aotearoa.herokuapp.com/"

@post('/calculate/rebate')
def rebate():
    json_request = request.json
    parameters = json_request['queryResult']['parameters']
    dependents = parameters['dependents']
    income = parameters['income']
    rates = parameters['rates']
    # request_id = json_request['re']
    return {
              "fulfillmentText": "one million dollars",
              "payload": {
                "google": {
                  "expectUserResponse": False,
                  "richResponse": {
                    "items": [
                      {
                        "simpleResponse": {
                          "textToSpeech": "you are eligible for one million dollars"
                        }
                      }
                    ]
                  }
                }
              }
            }

# Get required port, default to 5000.
port = os.environ.get('PORT', 5000)

# Run the app.
run(host='0.0.0.0', port=port)