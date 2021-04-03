from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Account

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)