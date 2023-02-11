import factory.fuzzy
from faker import Faker

from apps.order.models import Cart, Checkout, CheckoutItem
from apps.store.tests.factories import ProductFactory
from apps.account.tests.factories import UserFactory


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart

    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
    price = float(Faker().random_int(min=0, max=300))


class CheckoutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Checkout

    user = factory.SubFactory(UserFactory)

class CheckoutItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CheckoutItem

    checkout = factory.SubFactory(CheckoutFactory)
    product = factory.SubFactory(ProductFactory)
    price = float(Faker().random_int(min=0, max=300))
    shipping_fee = factory.Faker("random_element", elements=[0.0, 10.0])