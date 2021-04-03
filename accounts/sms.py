from twilio.rest import Client

from django.conf import settings

from app.sms import SMS
from app.helpers.url_helper import URLHelper


class AccountSMS(SMS):
    def confirm_account_phone_sms(self, account):
        self.send(
            to = account.phone,
            body =  f"Please visit the link below to confirm your phone number.\n\n"\
                    f"{URLHelper().phone_confirmation_url(account)}"
        )
    
    def invite_friend(self, account, to):
        self.send(
            to = to,
            body =  f"You've been invited to join the book club\n\n"\
                    f"{URLHelper().invite_friend_url(account)}"
        )