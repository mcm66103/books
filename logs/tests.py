from django.test import TestCase

from books.factories import BookFactory

from .models import Log


# Create your tests here.
class LogTest(TestCase):
    def setUp(self):
        self.book = BookFactory.build()
        self.book.owner.save()
        self.book.save()

    def test_new_book_creates_associated_log(self):
        self.assertEqual(1, Log.objects.all().count())