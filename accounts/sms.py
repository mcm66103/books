from twilio.rest import Client

from django.conf import settings

from app.sms import SMS
from app.helpers.url_helper import URLHelper


class AccountSMS(SMS):
    def confirm_account_phone_sms(self, account):
        self.send(
            to = account.phone,
            body =  f"lease visit the link below to confirm your phone number."\
                    f"{URLHelper().phone_confirmation_url(account)}"
        )
    
