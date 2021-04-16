from django.test import TestCase

from accounts.factories import AccountFactory

from .factories import BookCopyFactory, UnavailableBookCopyFactory
from .models import BookCopy


# Create your tests here.
class BookCopyTest(TestCase):
    def setUp(self):
        self.borrower = AccountFactory.create()

        self.book_copy = BookCopyFactory.build()
        self.book_copy.owner.save()
        self.book_copy.book.save()
        self.book_copy.save()

        self.unavailable_book_copy = UnavailableBookCopyFactory.build()
        self.unavailable_book_copy.owner = self.book_copy.owner
        self.unavailable_book_copy.book.save()
        self.unavailable_book_copy.save()

    def test_method_lend_to(self):
        self.book_copy.lend_to(self.borrower)

        self.assertEqual(self.borrower, self.book_copy.borrower)

    def test_method_return_to_owner(self):
        self.book_copy.lend_to(self.borrower)
        self.book_copy.return_to_owner()
        
        self.assertEqual(self.book_copy.borrower, None)

    def test_on_shelf_method(self):
        books_on_shelf = BookCopy.objects.on_shelf(self.book_copy.owner)
        
        for book in books_on_shelf: 
            self.assertTrue(book.available)
            self.assertEqual(self.book_copy.owner, book.owner)

    def test_borrowed_by_method(self):
        self.book_copy.lend_to(self.borrower)

        borrowed_books = BookCopy.objects.borrowed_by(self.borrower)
