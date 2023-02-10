import factory.fuzzy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from apps.account.models import UserAddress


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Faker("name")


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("phone",)

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(
        lambda a: f"{a.first_name}.{a.last_name}@supera.com".lower()
    )
    phone = factory.Faker("phone", locale="pt_BR")
    cpf = factory.Faker(locale="pt_BR").cpf()
    password = factory.PostGenerationMethodCall("set_password", "aPasSWoRd")
    is_staff = factory.fuzzy.FuzzyChoice([True, False])
    is_active = factory.fuzzy.FuzzyChoice([True, False])


class UserAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserAddress
    user = UserFactory()
    country = factory.Faker(locale="pt_BR").country
    state = factory.Faker(locale="pt_BR").state_abbr
    zip_code = factory.Faker(locale="pt_BR").postcode
    neighborhood = factory.Faker(locale="pt_BR").neighborhood
    address = factory.Faker(locale="pt_BR").street_sufix + \
        " " + factory.Faker(locale="pt_BR").street_name
    number = factory.Faker(locale="pt_BR").building_number
