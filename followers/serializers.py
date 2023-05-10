from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
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
