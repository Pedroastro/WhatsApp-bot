from flask import Flask, request
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
MY_PHONE_NUMBER = os.environ.get('MY_PHONE_NUMBER')
BUSINESS_PHONE_NUMBER = os.environ.get('BUSINESS_PHONE_NUMBER')

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/", methods=["POST"])

def bot():

	# user input
    user_msg = request.values.get('Body')
    print(user_msg)
    user_number = request.values.get('From')
    print(user_number)

	# response
    message = client.messages.create(
                                body=f'{user_msg}',
                                from_=f'whatsapp:{BUSINESS_PHONE_NUMBER}',
                                to=f'{user_number}'
                            )

    return "ok"


if __name__ == "__main__":
	app.run()

