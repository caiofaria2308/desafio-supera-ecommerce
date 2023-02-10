from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins

from apps.account.models import User, UserAddress
from apps.account.serializers import UserSerializer, UserAddressSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ["is_active", "staff", "admin"]
    search_fields = ["email", "first_name", "last_name"]


class UserAddressViewSet(ModelViewSet):
    queryset = UserAddress.objects.select_related("user").all()
    serializer_class = UserAddressSerializer
    filterset_fields = ["user"]
    search_fields = ["address"]
