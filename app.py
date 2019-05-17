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


    OF_QUERY = {
        'persons': {
            'person_one': {
                'rates_rebates__combined_income': {
                  '2018-01': income
                },
                'rates_rebates__dependants': {
                  '2018-01': dependents
                }
            }
        },
        'titled_properties': {
            'home': {
              'rates_rebates__rates_total': {
                '2018-01': rates
              },
              'owner': 'person_one'
            }
        },
    }

    # request_id = json_request['re']
    reply = "kay tea pie. if you have an income of {income} dollars and rates of {rates} dollars and {dependents} dependants, then you are eligible for one million dollars".format(
        income=income, dependents=dependents, rates=rates)
    return {
              "fulfillmentText": reply,
              "payload": {
                "google": {
                  "expectUserResponse": False,
                  "richResponse": {
                    "items": [
                      {
                        "simpleResponse": {
                          "textToSpeech": reply
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