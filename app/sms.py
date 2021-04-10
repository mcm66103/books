from twilio.rest import Client

from django.conf import settings


class SMS():
    def get_sms_client():
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        return Client(account_sid, auth_token)
    
    client = get_sms_client()

    @classmethod
    def send(cls, to, body):
        # Phone number may be string or PhoneNumber object.
        try: 
            to = to.raw_phone
        except:
            pass

        cls.client.messages.create(
            to = to, 
            from_ = settings.TWILIO_PHONE_NUMBER,
            body = body
        )



