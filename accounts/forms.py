from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

from phone_field.forms import PhoneWidget


from .models import Account
from .sms import AccountSMS

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

class InviteForm(forms.Form):
    phone_number = forms.CharField(widget=PhoneWidget())

class SMSPasswordResetForm(PasswordResetForm):
    username = forms.CharField(max_length=48)
    email = None
      
    def save(self, *args, **kwargs):
        """
        Generate a one-use only link for resetting password and SMS it to the
        user.
        """
        username = self.cleaned_data["username"]

        try: 
            user = Account.objects.get(username=username)
            AccountSMS.password_reset_sms(user)

        except Account.DoesNotExist:
            pass            