import factory.fuzzy
from apps.store.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker().color_name
    price = float(factory.Faker().random_int(min=0, max=300))
    score = factory.Faker().random_int(min=0, max=300)
