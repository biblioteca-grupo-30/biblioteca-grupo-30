from rest_framework import serializers
from .models import Exemplary
from books.models import Book
from followers.utils import send_mail_on_change
from django.shortcuts import get_object_or_404


class ExemplarySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Exemplary.objects.create(**validated_data)

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Quantidade de exemplares precisa ser maior que 0"
            )
        return value

    class Meta:
        model = Exemplary
        fields = ["id", "quantity", "book_id"]
        extra_kwargs = {"book_id": {"read_only": True}}

    def update(self, instance, validated_data):
        book = get_object_or_404(Book, pk=instance.book_id)

        instance_updated = super().update(instance, validated_data)
        quantity = instance_updated.quantity
        if quantity == 0:
            send_mail_on_change(instance_updated, book.title, "indisponível")

        if validated_data["quantity"] > 0:
            send_mail_on_change(instance_updated, book.title, "disponível")

        return instance_updated
