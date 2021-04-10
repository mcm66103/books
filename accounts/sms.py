from twilio.rest import Client

from django.conf import settings

from app.sms import SMS
from app.helpers.url_helper import URLHelper


class AccountSMS(SMS):
    @classmethod
    def confirm_account_phone_sms(self, to):
        self.send(
            to = to.phone,
            body =  f"Please visit the link below to confirm your phone number.\n\n"\
                    f"{URLHelper().phone_confirmation_url(to)}"
        )
    
    @classmethod
    def password_reset_sms(self, account):
        self.send(
            to = account.phone,
            body =  f"You requested a password reset. \n\n"\
                    f"{URLHelper().sms_password_reset_url(account)}"
        )
    
    @classmethod
    def invite_friend_sms(self, account, to):
        """
        Invitation goes 
        from: `account` (Account) 
        to: `to` (string: phone number)
        """
        self.send(
            to = to,
            body =  f"You've been invited to join the book club\n\n"\
                    f"{URLHelper().invite_friend_url(account)}"
        )
