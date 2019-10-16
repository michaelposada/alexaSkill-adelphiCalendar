# import flask
## pip install cryptography==2.1.0
## ngrok http 5000
## we had to downgrade pip to a different version
##
# import the following
from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import ast
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/adelphi_calendar")

def get_event_date(event, semester):
    # default value for date if event is not found
    date = 0

    #JSON files stored as the semester name
    with open(semester + ".json") as json_file:
        data = json.load(json_file)

        # convert to dictionary
        data = ast.literal_eval(data)

        for keys, values in data.items():
            if event.lower() in values.lower():
                date = keys
                break
    return date

#event = get_event_date()
#print(event)

# default
@app.route('/')
def homepage():
    return "hello"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, what would you like to know?'
    return question(welcome_message)

# return date to the user, takes in both the event and the semester
@ask.intent("AnswerIntent")
def share_event_date(event, semester):

    requestedEvent = event
    requestedSemester = semester

    event_date = get_event_date(requestedEvent, requestedSemester) #just gonna string together
    if(event_date != 0): # if 0 is returned then the event was not found
        event_date_msg = requestedEvent + ' for '+ requestedSemester +' is on ' + event_date
    else:
        event_date_msg = "The event does not exist for this semester"
    return statement(event_date_msg)

# return date to user, only takes the event input
@ask.intent("SimpleAnswerIntent")
def share_event_date(event):

    requestedEvent = event
    requestedSemester = "Fall 2019"

    event_date = get_event_date(requestedEvent, requestedSemester) #just gonna string together
    if (event_date != 0):
        event_date_msg = requestedEvent + ' is on ' + event_date
    else:
        event_date_msg = "The event does not exist"
    return statement(event_date_msg)

# not being used right now
@ask.intent("NoIntent")
def no_intent():
    bye_text = 'okay... bye'
    return statement(bye_text)

if __name__== '__main__':
    app.run(debug=True)