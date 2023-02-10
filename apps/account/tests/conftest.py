import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


@pytest.fixture
def user():
    """
    Create a user with all permissions for core app.
    """
    password = "testPassword"
    klass = get_user_model()
    user = klass.objects.create(
        email="testuser@vert-capital.com",
        password=make_password(password),
        is_active=True,
    )
    user._old_password = password
    return user


@pytest.fixture
def client_permission(user, client):
    """
    user logged with all permissions of core app.
    """
    client.force_login(user)
    return client
