from django.test import TestCase

from accounts.factories import AccountFactory

from .factories import BookCopyFactory


# Create your tests here.
class BookCopyTest(TestCase):
    def setUp(self):
        self.borrower = AccountFactory.create()

        self.book_copy = BookCopyFactory.build()
        self.book_copy.owner.save()
        self.book_copy.book.save()
        self.book_copy.save()

    def test_method_lend_to(self):
        self.book_copy.lend_to(self.borrower)

        self.assertEqual(self.borrower, self.book_copy.borrower)

    def test_method_return_to_owner(self):
        self.book_copy.lend_to(self.borrower)
        self.book_copy.return_to_owner()
        
        self.assertEqual(self.book_copy.borrower, None)

