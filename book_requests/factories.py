import factory
import datetime

from accounts.factories import AccountFactory
from books.factories import BookFactory
from book_copies.factories import BookCopyFactory

from .models import BookRequest

class BookRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BookRequest

    status = 'n' # New
    book_copy = factory.SubFactory(BookCopyFactory)
    borrower = factory.SubFactory(AccountFactory)
    original_due_date = datetime.date.today() + datetime.timedelta(days=3)
    due_date = datetime.date.today() + datetime.timedelta(days=3)
