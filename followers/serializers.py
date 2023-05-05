from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.Serializer):
    def create(self, validated_data: dict) -> Follower:
        return Follower.objects.create(**validated_data)

    class Meta:
        model = Follower
        fields = [
            "id",
            "user_id",
            "book_id",
        ]
        extra_kwargs = {
            "user_id": {"read_only": True},
            "book_id": {"read_only": True},
        }
