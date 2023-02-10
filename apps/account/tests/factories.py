import factory.fuzzy
from faker import Faker
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from apps.account.models import UserAddress


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = Faker().name


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("phone",)

    first_name = Faker().first_name
    last_name = Faker().last_name
    email = factory.LazyAttribute(
        lambda a: f"{a.first_name}.{a.last_name}@supera.com".lower()
    )
    phone = Faker("pt_BR").msisdn()
    cpf = Faker("pt_BR").cpf()
    password = factory.PostGenerationMethodCall("set_password", "aPasSWoRd")
    staff = factory.fuzzy.FuzzyChoice([True, False])
    is_active = factory.fuzzy.FuzzyChoice([True, False])


class UserAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserAddress
    user = factory.SubFactory(UserFactory)
    country = Faker("pt_BR").country()
    state = Faker("pt_BR").state_abbr()
    zip_code = Faker("pt_BR").postcode()
    neighborhood = Faker("pt_BR").neighborhood()
    address = Faker("pt_BR").street_suffix() + \
        " " + Faker("pt_BR").street_name()
    number = Faker("pt_BR").building_number()
