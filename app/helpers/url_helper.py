from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode




class URLHelper():
    def __init__(self): 
        self.base_url = settings.BASE_URL

    def phone_confirmation_url(self, account):
        path = reverse_lazy('confirm_phone', kwargs={"confirmation_number": account.phone_confirmation_number})
        return self.prepend_base_url(path)

    def invite_friend_url(self, account):
        """
            Generate invite link based on the account 
            the invite is coming from.
        """
        path = reverse_lazy('create_account_from_invite', kwargs={"invite_number": account.invite_number})
        return self.prepend_base_url(path)

    def sms_password_reset_url(self, account):
        kwargs = {
            "uidb64"    : urlsafe_base64_encode(force_bytes(account.pk)), 
            "token"     : default_token_generator.make_token(account)
        }
        
        path = reverse_lazy('password_reset_confirm', kwargs = kwargs)
        return self.prepend_base_url(path)

    def prepend_base_url(self, path): 
        return self.base_url + str(path)