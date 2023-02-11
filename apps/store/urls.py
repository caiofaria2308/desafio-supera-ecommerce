from rest_framework import routers

from apps.store.views import ProductViewSet

router = routers.SimpleRouter()

router.register(r"products", ProductViewSet, basename="products")

urlpatterns = router.urls
