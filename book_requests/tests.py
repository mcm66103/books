from django.test import TestCase

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

