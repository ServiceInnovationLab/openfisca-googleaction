import os
from bottle import route, run, request


@route('/calculate/rebate')
def rebate():
    json_request = request.json
    dependents = json_request['parameters']['dependents']
    income = json_request['parameters']['income']
    rates = json_request['parameters']['rates']
    # request_id = json_request['re']
    return {
      "fulfillmentText": "one million dollars"
    }

# Get required port, default to 5000.
port = os.environ.get('PORT', 5000)

# Run the app.
run(host='0.0.0.0', port=port)