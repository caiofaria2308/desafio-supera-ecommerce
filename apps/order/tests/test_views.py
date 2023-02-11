from django.urls import reverse

from apps.order.models import Cart
from apps.store.tests.factories import ProductFactory
from apps.account.tests.factories import UserFactory


def test_valid_total_cart_with_shipping_fee(db, client_permission, headers):
    """ Test checkout values if have shipping fee"""
    API_LIST_CART = "cart-view-list"
    API_NEW_CART = "cart-add-list"
    p = ProductFactory(price=100.00)
    url = reverse(API_NEW_CART)
    
    for _ in range(2):
        payload = {
            "product": p.pk
        }
        assert client_permission.post(url, payload, **headers).status_code == 201
        
    url = reverse(API_LIST_CART)
    response = client_permission.get(url, **headers)
    data = response.json()
    assert response.status_code == 200
    assert len(data.get("results")) > 0
    result = data.get("results")[0]
    assert len(result.get("items")) == 2
    assert result.get("total_products") == 200.0
    assert result.get("total_shipping_fee") == 20.0
    assert result.get("total") == 220.00


def test_valid_total_cart_without_shipping_fee(db, client_permission, headers):
    """ Test checkout values if have no shipping fee"""
    API_LIST_CART = "cart-view-list"
    API_NEW_CART = "cart-add-list"
    p = ProductFactory(price=100.00)
    url = reverse(API_NEW_CART)
    
    for _ in range(3):
        payload = {
            "product": p.pk
        }
        assert client_permission.post(url, payload, **headers).status_code == 201
        
    url = reverse(API_LIST_CART)
    response = client_permission.get(url, **headers)
    data = response.json()
    assert response.status_code == 200
    assert len(data.get("results")) > 0
    result = data.get("results")[0]
    assert len(result.get("items")) == 3
    assert result.get("total_products") == 300.0
    assert result.get("total_shipping_fee") == 0.0
    assert result.get("total") == 300.00
    