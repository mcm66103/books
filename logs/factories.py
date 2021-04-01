import factory

from accounts.factories import AccountFactory
from books.factories import BookFactory

class LogFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = Log

    book = SubFactory(BookFactory)


class LogEntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LogEntry

    log = factory.SubFactory(LogFactory)
    account = factory.SubFactory(AccountFactory)
    entry = factory.Faker('sentence', nb_words=120)

    