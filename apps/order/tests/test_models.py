from django.db.models import Sum

from apps.order.models import Cart, CheckoutItem
from apps.order.tests.factories import CheckoutFactory
from apps.store.tests.factories import ProductFactory
from apps.account.tests.factories import UserFactory


def test_shipping_fee_cart(db: None):
    """Teste na atualização do
    frete dos produtos ao inserir item no carrinho

    Args:
        db (None): _description_
    """
    def verify_object(c: Cart, to_compare):
        c.refresh_from_db()
        assert c.shipping_fee == to_compare
    p = ProductFactory(price=100.00)
    user = UserFactory()
    c1 = Cart.objects.create(
        user=user,
        product=p,
        price=p.price,
    )
    verify_object(c1, 10.0)
    c2 = Cart.objects.create(
        user=user,
        product=p,
        price=p.price,
    )
    verify_object(c1, 10.0)
    verify_object(c2, 10.0)
    c3 = Cart.objects.create(
        user=user,
        product=p,
        price=p.price,
    )   
    verify_object(c1, 0.0)
    verify_object(c2, 0.0)
    verify_object(c3, 0.0)
    c3.delete()
    verify_object(c1, 10.0)
    verify_object(c2, 10.0)


def test_shipping_fee_checkout_equal_0(db: None):
    """Teste no valor do checkout
    quando o valor total da venda 
    supera ou iguala R$250

    Args:
        db (None): _description_
    """
    p = ProductFactory(price=100.00)
    user = UserFactory()
    for _ in range(3):
        # 
        Cart.objects.create(
            user=user,
            product=p,
            price=p.price,
        )
    checkout = CheckoutFactory(user=user)
    checkout.checkout_items()
    items = CheckoutItem.objects.filter(checkout=checkout)
    assert sum(
        items
        .annotate(total=Sum("shipping_fee"))
        .values_list("total", flat=True)
    ) == 0.0


def test_shipping_fee_checkout_equal_20(db: None):
    """Teste no valor do checkout
    quando o valor total da venda 
    for menor que R$250

    Args:
        db (None): _description_
    """
    p = ProductFactory(price=100.00)
    user = UserFactory()
    for _ in range(2):
        # 
        Cart.objects.create(
            user=user,
            product=p,
            price=p.price,
        )
    checkout = CheckoutFactory(user=user)
    checkout.checkout_items()
    items = CheckoutItem.objects.filter(checkout=checkout)
    assert sum(
        items
        .annotate(total=Sum("shipping_fee"))
        .values_list("total", flat=True)
    ) == 20.0
    
    