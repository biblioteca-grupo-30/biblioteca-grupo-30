from rest_framework import serializers
from .models import Exemplary


class ExemplarySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Exemplary.objects.create(**validated_data)

    class Meta:
        model = Exemplary
        fields = ["id", "quantity", "book_id"]
        extra_kwargs = {"book_id": {"read_only": True}}
