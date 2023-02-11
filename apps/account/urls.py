from rest_framework import routers

from apps.account.views import UserViewSet, UserAddressViewSet

router = routers.SimpleRouter()

router.register(r'users', UserViewSet, basename="users")
router.register(r'users-address', UserAddressViewSet, basename="users-address")

urlpatterns = router.urls
