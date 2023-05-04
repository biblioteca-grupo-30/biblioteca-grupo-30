from rest_framework import serializers
from .models import Exemplary
from django.shortcuts import get_object_or_404


class ExemplarySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Exemplary.objects.create(**validated_data)

    class Meta:
        model = Exemplary
        fields = ["id", "quantity", "book_id"]
        extra_kwargs = {"book_id": {"read_only": True}}
