from django.test import TestCase

from book_copies.factories import BookCopyFactory

from .models import Log


# Create your tests here.
class LogTest(TestCase):
    def setUp(self):
        self.book_copy = BookCopyFactory.build()
        self.book_copy.owner.save()
        self.book_copy.book.save()
        self.book_copy.save()

    def test_new_book_creates_associated_log(self):
        self.assertEqual(1, Log.objects.all().count())
