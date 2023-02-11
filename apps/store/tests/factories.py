import factory.fuzzy
from faker import Faker

from apps.store.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = Faker().color_name
    price = float(Faker().random_int(min=0, max=300))
    score = Faker().random_int(min=0, max=300)
