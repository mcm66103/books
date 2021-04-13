import factory

from accounts.factories import AccountFactory
from books.factories import BookFactory

from .models import BookCopy

class BookCopyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BookCopy

    owner = factory.SubFactory(AccountFactory)
    book = factory.SubFactory(BookFactory)

class UnavailableBookCopyFactory(BookCopyFactory):
    class Meta:
        model = BookCopy

    available = False