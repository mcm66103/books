import factory
from .models import Account

class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    email = factory.Faker('email')