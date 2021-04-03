from django.conf import settings

import factory

from .models import Account

class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    email = factory.Faker('email')
    phone = settings.TEST_PHONE