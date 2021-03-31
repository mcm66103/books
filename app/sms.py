from twilio.rest import Client

from django.conf import settings


class SMS():
    def __init__(self):
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN

        self.client = Client(account_sid, auth_token)

    def send(self, to, body): 
        self.client.messages.create(
            to = to, 
            from_ = settings.TWILIO_PHONE_NUMBER,
            body = body
        )