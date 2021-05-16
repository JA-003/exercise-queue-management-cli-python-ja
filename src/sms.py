# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
TEST_PHONE_NUMBER = os.getenv('TEST_PHONE_NUMBER')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

def send(body='Some body', to=TEST_PHONE_NUMBER):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_=TWILIO_PHONE_NUMBER,
                        to='+'+to
                    )

    # print(message.sid)