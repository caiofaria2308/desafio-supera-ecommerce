from rest_framework.viewsets import ModelViewSet

from apps.store.models import Product
from apps.store.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["name"]
    lookup_field = "slug"
    ordering_fields = [
        "price",
        "score",
        "name"
    ]