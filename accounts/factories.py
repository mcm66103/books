from django.conf import settings

import factory

from .models import Account

class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    username = factory.Faker('user_name')
    phone = settings.TEST_PHONE