import os
from bottle import route, run

@route('/calculate/:variable_name')
def index(variable_name='World'):
    return 'calculation for {variable_name} goes here'.format(variable_name=variable_name)

# Get required port, default to 5000.
port = os.environ.get('PORT', 5000)

# Run the app.
run(host='0.0.0.0', port=port)