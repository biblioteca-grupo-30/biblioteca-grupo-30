from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data["password"])

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_blocked",
            "is_blocked",
            "is_superuser",
            "books_followed",
            "blocked_until"
            "books_followed",
            "blocked_until"
        ]
        extra_kwargs = {

            "password": {"write_only": True},
            "books_followed": {"read_only": True},
            "is_blocked": {"default": False},
            "is_superuser": {"default": False},
            "books_followed": {"read_only": True},
            "is_blocked": {"default": False},
            "is_superuser": {"default": False},
        }
