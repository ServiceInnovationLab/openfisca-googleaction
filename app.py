import os
from bottle import route, run, request


@route('/calculate/rebate')
def rebate():
    json_request = request.json
    parameters = json_request['queryResult'['parameters']]
    dependents = parameters['dependents']
    income = parameters['income']
    rates = parameters['rates']
    # request_id = json_request['re']
    return {
      "fulfillmentText": "one million dollars",
      "payload": {
        "google": {
          "expectUserResponse": false,
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

# Get required port, default to 5000.
port = os.environ.get('PORT', 5000)

# Run the app.
run(host='0.0.0.0', port=port)