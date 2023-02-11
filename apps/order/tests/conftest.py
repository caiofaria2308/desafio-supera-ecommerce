
import pytest
from django.contrib.auth import get_user_model

from main.utils import get_permissions


@pytest.fixture
def user():
    """
    Create a user with all permissions for core app.
    """
    permission_required = get_permissions(
        [
            "view_cart",
            "add_cart",
            "change_cart",
            "remove_cart",
            "view_checkout",
            "add_checkout",
            "change_checkout",
            "remove_checkout",
            "view_checkoutitem",
            "add_checkoutitem",
            "change_checkoutitem",
            "remove_checkoutitem",
        ]
    )
    klass = get_user_model()
    user = klass.objects.create(email="testuser@root.com")
    user.user_permissions.set(permission_required)
    return user


@pytest.fixture
def client_permission(user, client):
    """
    user logged with all permissions of core app.
    """
    client.force_login(user)
    return client
