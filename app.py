import os
from bottle import route, run, request



def make_response(project_id, session_id):
  return {
    "fulfillmentText": "This is a text response",
    "fulfillmentMessages": [
      {
        "card": {
          "title": "card title",
          "subtitle": "card text",
          "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
          "buttons": [
            {
              "text": "button text",
              "postback": "https://assistant.google.com/"
            }
          ]
        }
      }
    ],
    "source": "example.com",
    "payload": {
      "google": {
        "expectUserResponse": True,
        "richResponse": {
          "items": [
            {
              "simpleResponse": {
                "textToSpeech": "this is a simple response"
              }
            }
          ]
        }
      }
    },
    "outputContexts": [
      {
        "name": "projects/{PROJECT_ID}/agent/sessions/{SESSION_ID}/contexts/context name".format(PROJECT_ID=project_id, SESSION_ID=session_id),
        "lifespanCount": 5,
        "parameters": {
          "param": "param value"
        }
      }
    ],
    "followupEventInput": {
      "name": "event name",
      "languageCode": "en-US",
      "parameters": {
        "param": "param value"
      }
    }
  }


@route('/calculate/:variable_name')
def index(variable_name='World'):
    print(request.json)
    return make_response("1", "1")

# Get required port, default to 5000.
port = os.environ.get('PORT', 5000)

# Run the app.
run(host='0.0.0.0', port=port, reloader=True)