from django.test import TestCase

from accounts.factories import AccountFactory

from .factories import BookFactory

# Create your tests here.
class BookTest(TestCase):
    def setUp(self):
        self.borrower = AccountFactory.create()

        self.book = BookFactory.build()
        self.book.owner.save()
        self.book.save()

    def test_method_lend_to(self):
        self.book.lend_to(self.borrower)

        self.assertEqual(self.borrower, self.book.borrower)

    def test_method_return_to_owner(self):
        self.book.lend_to(self.borrower)
        self.book.return_to_owner()
        
        self.assertEqual(self.book.borrower, None)
