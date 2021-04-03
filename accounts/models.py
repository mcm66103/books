from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from phone_field import PhoneField

from accounts.managers import AccountManager
from accounts.sms import AccountSMS

from .helpers import generate_confirmation_number

from app.helpers.env_helper import EnvHelper
# from .mailers import AccountMailer


# Phone number field 
# https://pypi.org/project/django-phone-field/


class Account(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    phone_confirmation_number = models.CharField(max_length=32, default=generate_confirmation_number)
    phone_confirmed_at = models.DateTimeField(blank=True, null=True)

    confirmation_number = models.CharField(max_length=32, default=generate_confirmation_number)
    confirmed_at = models.DateTimeField(blank=True, null=True)

    invite_number = models.CharField(max_length=32, default=generate_confirmation_number)

    phone = PhoneField(blank=True) #  optional kwarg: help_text=''

    friends = models.ManyToManyField("accounts.Account")

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        send_sms = (settings.TEST_SMS and kwargs.pop('send_sms', False)) or settings.SMS_VERIFICATION

        if not self.pk:
            self.set_password(self.password)

            if send_sms:
                '''
                    In this case,
                    We rely on a user to verify their phone number.
                    - Production
                ''' 
                self.send_phone_confirmation_sms()
            
            else:           
                '''
                    In this case,
                    We confirm the phone number.
                    - Testing
                    - Development
                ''' 
                self.confirm_phone_number(save=False)

        super(Account, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('profile')
    
    def is_confirmed(self):
        return self.confirmed_at == None
    
    def send_account_confirmation_email(self):
        AccountMailer().account_confirmation_email(self)

    def set_phone_confirmation_number(self, save=False):
        self.phone_confirmation_number = generate_confirmation_number()

        if save: 
            self.save()

    def send_phone_confirmation_sms(self):
        AccountSMS().confirm_account_phone_sms(self)

    def confirm_phone_number(self, save=True):
        
        self.phone_confirmed_at = datetime.now()

        if save: 
            self.save()

    def invite_friend(self, to):
        AccountSMS().invite_friend(self, to) 

    def add_friend(self, new_friend):
        self.friends.add(new_friend)
        self.save()