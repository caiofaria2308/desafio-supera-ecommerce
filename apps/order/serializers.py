from rest_framework import serializers
from django.db.models import Sum

from apps.order.models import Cart, Checkout, CheckoutItem
from apps.store.serializers import ProductMinimalSerializer


class CartCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "user",
            "product",
            "price",
            "created_at",
            "updated_at"
        ]
        read_only_fields = [
            "user",
            "price",
        ]

    

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        validated_data["price"] = validated_data.get("product").price
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["price"] = validated_data.get("product").price
        return super().update(instance, validated_data)

class CartListSerializer(serializers.ModelSerializer):
    total_products = serializers.SerializerMethodField()
    total_shipping_fee = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            "user",
            "items",
            "total_products",
            "total_shipping_fee",
            "total",
        ]

    def get_total_products(self, obj):
        user = self.context["request"].user
        items = Cart.objects.filter(user=user)
        return sum(
            items
            .annotate(total=Sum("price"))
            .values_list("total", flat=True)
        )

    def get_total_shipping_fee(self, obj):
        user = self.context["request"].user
        items = Cart.objects.filter(user=user)
        return sum(
            items
            .annotate(total=Sum("shipping_fee"))
            .values_list("total", flat=True)
        )

    def get_total(self, obj):
        return self.get_total_products(obj) + self.get_total_shipping_fee(obj)

    def get_items(self, obj):
        user = self.context["request"].user
        items = Cart.objects.filter(user=user)
        return CartCreateUpdateSerializer(items, many=True).data


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = [
            "id",
            "user",
            "number",
            "date"
        ]
        read_only_fields = fields

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        create = super().create(validated_data)
        cart = Cart.objects.filter(user=user)
        if cart.exists():
            cart.first().update_shipping_fee(cart)
        else:
            create.delete()
        for item in cart:
            CheckoutItem.objects.create(
                checkout=create,
                product=item.product,
                price=item.price,
                shipping_fee=item.shipping_fee
            )
        cart.delete()
        return create


class CheckoutItemSerializer(serializers.ModelSerializer):
    product = ProductMinimalSerializer()

    class Meta:
        model = CheckoutItem
        fields = [
            "id",
            "product",
            "price",
            "shipping_fee",
            "checkout"
        ]


class CheckoutViewSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    total_shipping_fee = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Checkout
        fields = [
            "id",
            "number",
            "date",
            "products",
            "total_price",
            "total_shipping_fee",
            "total"
        ]
        read_only_fields = ["id", "number", "date"]

    def get_products(self, obj: Checkout):
        items = CheckoutItem.objects.filter(checkout=obj)
        return CheckoutItemSerializer(items, many=True).data

    def get_total_price(self, obj):
        user = self.context["request"].user
        items = CheckoutItem.objects.filter(checkout=obj, checkout__user=user)
        return sum(
            items
            .annotate(total=Sum("price"))
            .values_list("total", flat=True)
        )

    def get_total_shipping_fee(self, obj):
        user = self.context["request"].user
        items = CheckoutItem.objects.filter(checkout=obj, checkout__user=user)
        return sum(
            items
            .annotate(total=Sum("shipping_fee"))
            .values_list("total", flat=True)
        )

    def get_total(self, obj):
        return self.get_total_price(obj) + self.get_total_shipping_fee(obj)
