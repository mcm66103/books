import datetime
from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from app.decorators import require_test_sms

from .factories import BookRequestFactory


class BookRequestTest(TestCase):

    def setUp(self): 
        self.book_request = BookRequestFactory.build()

        self.book_request.book_copy.owner.save()
        self.book_request.book_copy.book.save()
        self.book_request.book_copy.save()

        self.book_request.borrower.save()

        self.book_request.save()

    def test_accept_book_request(self):
        self.book_request.accept_request(self.book_request.book_copy.owner)

        self.assertEqual(self.book_request.status, 'a')
        self.assertFalse(self.book_request.book_copy.available)

    def test_reject_book_request(self):
        self.book_request.reject_request(self.book_request.book_copy.owner)

        self.assertEqual(self.book_request.status, 'r')
        self.assertTrue(self.book_request.book_copy.available)

    def test_begin_book_checkout(self):
        self.book_request.accept_request(self.book_request.book_copy.owner)
        self.book_request.begin_checkout()

        self.assertEqual(self.book_request.status, 'i')

    def test_return_book(self):
        self.book_request.accept_request(self.book_request.book_copy.owner)
        self.book_request.begin_checkout()

        self.assertEqual(self.book_request.status, 'i')

    def test_days_until_due(self):
        '''
        BookRequest.due_date is set as follows in ./factories.py

        due_date = datetime.date.today() + datetime.timedelta(days=3)
        '''

        days_remaining = self.book_request.days_until_due()
        self.assertEqual(days_remaining, 3)

class BookRequestCommandTest(TestCase):
    '''
    This command test is a great example of how you can test other console commands.
    We can use console commands for scheduled tasks or internal tools / utilities.
    '''
    def setUp(self):
        self.book_request = BookRequestFactory.build(
                                due_date = datetime.date.today() + datetime.timedelta(days=1)
                            )

        self.book_request.book_copy.owner.save()
        self.book_request.book_copy.book.save()
        self.book_request.book_copy.save()

        self.book_request.borrower.save()

        self.book_request.save()

        self.lengthy_book_request = BookRequestFactory.build(
                                        due_date = datetime.date.today() + datetime.timedelta(days=24)
                                    )
                                    
    @require_test_sms
    def test_command_send_2_day_book_return_reminder(self):
        out = StringIO()
        call_command('send_2_day_book_return_reminder', stdout=out)
        out_string = out.getvalue()

        '''
        self.book_request is nearly due. This output is expected in stdout given
        then input conditions
        '''
        self.assertTrue(f"borrower {self.book_request.borrower.id}" in out_string)
        self.assertTrue(f"book copy {self.book_request.book_copy.id}" in out_string)

        '''
        self.lengthy_book_request is not due for a long time. There should be no
        output about it in stdout.
        '''
        self.assertTrue(f"borrower {self.lengthy_book_request.borrower.id}" not in out_string)
        self.assertTrue(f"book copy {self.lengthy_book_request.book_copy.id}" not in out_string)
