from rest_framework import serializers

from apps.account.models import User, UserAddress


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "password",
            "is_staff",
            "is_superuser"
        ]
        read_only_fields = ["is_staff", "is_superuser"]

    def create(self, validated_data):
        create = super().create(validated_data)
        obj: User = User.objects.get(pk=create.pk)
        obj.set_password(validated_data.get('password'))
        return create

    def update(self, instance, validated_data):
        update = super().update(instance, validated_data)
        instance.set_password(validated_data.get('password'))
        return update


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"
