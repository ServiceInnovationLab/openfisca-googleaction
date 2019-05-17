import os
from bottle import post, run, request
import requests
OPENFISCA_URL = "https://openfisca-aotearoa.herokuapp.com/calculate"


def get_rebate_amount(dependents, rates, income):
    OF_QUERY = {
        'persons': {
            'person_one': {
                'rates_rebates__combined_income': {
                  '2019': income
                },
                'rates_rebates__dependants': {
                  '2019': dependents
                }
            }
        },
        'titled_properties': {
            'home': {
              'rates_rebates__rates_total': {
                '2019': rates
              },
              'rates_rebates__rebate': {
                '2019': None
              },
              'owners': ['person_one']
            }
        },
    }
    of_response = requests.post(OPENFISCA_URL, json=OF_QUERY).json()
    rebate = of_response['titled_properties']['home']['rates_rebates__rebate']['2019']
    return rebate


@post('/calculate/rebate')
def rebate():
    json_request = request.json
    parameters = json_request['queryResult']['parameters']
    dependents = parameters['dependents']
    income = parameters['income']
    rates = parameters['rates']

    rebate = get_rebate_amount(dependents, rates, income)

    reply = "kay teh-pie. You are eligible for {rebate} dollars".format(rebate=rebate)
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

port = os.environ.get('PORT', 5000)
run(host='0.0.0.0', port=port)
