from django.contrib import admin

from apps.store.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "slug",
        "name",
        "price",
        "score",
        "updated_at"
    ]
    list_display_links = [
        "id", "slug"
    ]
    search_fields = ["slug", "name"]
    list_editable = ["price", "score"]
