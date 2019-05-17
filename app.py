import os
from bottle import route, run, request


@route('/calculate/:variable_name')
def index(variable_name='World'):
    # json_request = request.json
    # request_id = json_request['re']
    return {
      "fulfillmentText": "one million dollars",
      "source": "https://ratesrebates.services.govt.nz"
    }

# Get required port, default to 5000.
port = os.environ.get('PORT', 5000)

# Run the app.
run(host='0.0.0.0', port=port, reloader=True)