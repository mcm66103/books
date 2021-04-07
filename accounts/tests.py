from django.conf import settings
from django.test import TestCase

from app.decorators import require_test_sms

from .factories import AccountFactory


# Create your tests here.
class AccountTest(TestCase):
    def setUp(self):
        
        assert settings.SMS_VERIFICATION != True
        """
            We do not want to rack up large bills for Twilio.
            We do not generally want to use sms verification during development. 

            We make this assertion to avoid sending SMS messages during development.
        """

        self.account = AccountFactory.build()
        self.account.save()

    @require_test_sms
    def test_confirm_phone_text(self):
        self.confirm_phone_account = AccountFactory.build()
        self.confirm_phone_account.save(send_sms=True)

    def test_account_has_phone_confirmation_number(self):
        has_phone_confirmation_number = bool(self.account.phone_confirmation_number)
        self.assertTrue(has_phone_confirmation_number)
