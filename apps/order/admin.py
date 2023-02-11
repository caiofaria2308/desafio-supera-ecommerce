from django.contrib import admin

from apps.order.models import Cart, Checkout, CheckoutItem


class CheckoutItemInLine(admin.TabularInline):
    model = CheckoutItem
    extra = 0
    fields = ["product", "price", "shipping_fee"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "price", "shipping_fee"]
    list_display_links = ["id", "user", "product"]
    search_fields = ["product__name", "user__phone", "user__first_name"]
    raw_id_fields = ["user", "product"]

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "number", "date"]
    list_display_links = ["id", "user"]
    search_fields = ["number", "user__phone", "user__first_name"]
    raw_id_fields = ["user"]
    inlines = [CheckoutItemInLine]


@admin.register(CheckoutItem)
class CheckoutItemAdmin(admin.ModelAdmin):
    list_display = ["id", "checkout", "product", "price", "shipping_fee"]
    list_display_links = ["id", "checkout", "product"]
    list_editable = ["price", "shipping_fee"]
    search_fields = [
        "product__name",
        "checkout__number"
    ]
    raw_id_fields = ["checkout", "product"]
    
    
