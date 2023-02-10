from rest_framework import routers

from apps.order.views import (
    CartListViewSet, CheckoutViewSet, CheckoutItemViewSet, CheckoutViewViewSet, CartCreateUpdateViewSet,
)

router = routers.SimpleRouter()

router.register(r"cart-add", CartCreateUpdateViewSet, basename="cart-add")
router.register(r"cart", CartListViewSet, basename="cart-view")
router.register(r"checkout", CheckoutViewSet, basename="checkout")
router.register(r"checkout-list", CheckoutViewViewSet, basename="checkout-list")
router.register(r"checkout-items", CheckoutItemViewSet, basename="checkout-items")


urlpatterns = router.urls
