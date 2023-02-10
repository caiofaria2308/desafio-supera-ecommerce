from django.db import models
from django.db.models import Sum
from author.decorators import with_author

from main.utils import BaseModel, get_order_number


@with_author
class Cart(BaseModel):
    user = models.ForeignKey(
        "account.User",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "store.Product",
        on_delete=models.PROTECT
    )
    price = models.FloatField(
        verbose_name="Preço"
    )
    shipping_fee = models.FloatField(
        verbose_name="Frete",
        default=10
    )

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"

    def __str__(self) -> str:
        return f"Carrinho de {self.user}"

    def update_shipping_fee(self, items):
        # Update shipping fee in the cart
        total = sum(
            items
            .annotate(total=Sum("price"))
            .values_list("total", flat=True)
        )
        if total >= 250.00:
            items.update(shipping_fee=0)
            return
        items.update(shipping_fee=10)
        return

    def save(self, *args, **kwargs) -> None:
        save = super().save(*args, **kwargs)
        items = self.__class__.objects.filter(user=self.user)
        self.update_shipping_fee(items)
        return save

@with_author
class Checkout(BaseModel):
    user = models.ForeignKey(
        "account.User",
        on_delete=models.CASCADE
    )
    number = models.CharField(
        verbose_name="Número do pedido",
        max_length=32,
        default=get_order_number,
        unique=True,
    )
    date = models.DateField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self) -> str:
        return f"Pedido {self.number} do {self.user}"


@with_author
class CheckoutItem(BaseModel):
    checkout = models.ForeignKey(
        Checkout,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "store.Product",
        on_delete=models.PROTECT
    )
    price = models.FloatField(
        verbose_name="Preço"
    )
    shipping_fee = models.FloatField(
        verbose_name="Frete"
    )

    class Meta:
        verbose_name = "Item do pedido"
        verbose_name_plural = "Itens dos pedidos"

    def __str__(self) -> str:
        return f"Pedido: {self.checkout.number} Produto: {self.product.name}"