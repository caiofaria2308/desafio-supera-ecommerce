import pytest
from pytest_factoryboy import register

from apps.account.tests.factories import UserFactory, GroupFactory, UserAddressFactory
from apps.store.tests.factories import ProductFactory

# accounts
register(UserFactory)
register(UserAddressFactory)
register(GroupFactory)
register(ProductFactory)


@pytest.fixture
def user_credentials(user):
    password = "test_password"
    user.set_password(password)
    user.save()
    return user, password


@pytest.fixture
def get_permissions():
    from main.utils import get_permissions

    return get_permissions


@pytest.fixture
def get_view(all_views):
    from main.utils import get_view

    return get_view


@pytest.fixture
def all_views():
    from main.utils import get_views

    return get_views()


@pytest.fixture
def responsible():
    responsible = UserFactory()
    return responsible


@pytest.fixture
def headers():
    """default headers on make request"""
    return {"content_type": "application/json"}


@pytest.fixture
def authenticated_client(client, user):
    client.force_login(user)
    return client
