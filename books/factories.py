import factory

from accounts.factories import AccountFactory

from .models import Book

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    author = factory.Faker('name')