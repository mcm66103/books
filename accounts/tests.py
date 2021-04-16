from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse

from app.decorators import require_test_sms

from book_copies.models import BookCopy
from book_requests.models import BookRequest

from .factories import AccountFactory


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

class AccountViewTest(TestCase):
    def setUp(self):
        self.password = "123456!"
        self.client = Client()

        self.account = AccountFactory.build()
        self.account.password = self.password
        self.account.save()

        
    def test_profile_view_as_logged_in_account(self):
        self.client.login(username=self.account.username, password=self.password)

        res = self.client.get(reverse('profile'))

        self.assertEqual(res.context['books_on_shelf'].model, BookCopy)
        self.assertEqual(res.context['borrowed_books'].model, BookCopy)
        self.assertEqual(type(res.context['books_on_shelf_count']), int)
        self.assertEqual(res.context['lifetime_shares'].model, BookRequest)
        self.assertEqual(type(res.context['lifetime_shares_count']), int)

    def test_profile_view_as_not_logged_in_account(self):
        res = self.client.get(reverse('profile'))

        self. assertEqual(res.status_code, 302)
