from django.contrib import admin

from apps.account.forms import UserForm
from apps.account.models import User, UserAddress


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "email",
        "first_name",
        "phone",
        "is_active"
    ]
    list_display_links = ["id", "email"]
    search_fields = ["email", "phone", "first_name", "last_name"]
    list_filter = ["is_active", "staff", "admin"]
    add_form = UserForm
    form = UserForm


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "country",
        "zip_code",
        "address",
        "number",
        "state"
    ]
    list_display_links = ["id", "user"]
    search_fields = ["address"]
    list_filter = ["state", "country"]
    raw_id_fields = ["user"]
