from django.db.models import Avg
from rest_framework.viewsets import GenericViewSet, mixins

from apps.order.models import Cart, Checkout, CheckoutItem
from apps.order.serializers import (
    CartListSerializer, CheckoutSerializer, CheckoutItemSerializer, CheckoutViewSerializer, CartCreateUpdateSerializer,
)


class CartCreateUpdateViewSet(
    GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Cart.objects.select_related("user", "product").all()
    serializer_class = CartCreateUpdateSerializer

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(user=self.request.user)
        )

    def destroy(self, request, *args, **kwargs):
        destroy = super().destroy(request, *args, **kwargs)
        items = self.get_queryset()
        self.get_serializer().update_shipping_fee(items)
        return destroy

class CartListViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = Cart.objects.select_related("user", "product")
    serializer_class = CartListSerializer

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(user=self.request.user)
            .distinct("user")
        )


class CheckoutViewSet(
    GenericViewSet,
    mixins.CreateModelMixin
):
    queryset = Checkout.objects.select_related("user").all()
    serializer_class = CheckoutSerializer
    filterset_fields = ["number"]

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(user=self.request.user)
        )


class CheckoutViewViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Checkout.objects.select_related("user").all()
    serializer_class = CheckoutViewSerializer
    filterset_fields = ["number"]
    lookup_field = "number"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(user=self.request.user)
        )


class CheckoutItemViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = CheckoutItem.objects.select_related("checkout").all()
    serializer_class = CheckoutItemSerializer
    filterset_fields = ["checkout__number"]

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(checkout__user=self.request.user)
        )