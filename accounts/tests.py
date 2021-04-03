from django.conf import settings
from django.test import TestCase

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

    def test_confirm_phone_text(self):
        if settings.TEST_SMS:      
            self.confirm_phone_account = AccountFactory.build()
            self.confirm_phone_account.save(send_sms=True)

            print(
                "\n"\
                "\n"\
                f"A text message has been sent to {self.confirm_phone_account.phone}...\n"\
                f"Please confirm that text arrived...\n"\
                "\n"
            )

    def test_account_has_phone_confirmation_number(self):
        has_phone_confirmation_number = bool(self.account.phone_confirmation_number)
        self.assertTrue(has_phone_confirmation_number)
