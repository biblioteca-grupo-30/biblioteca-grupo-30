from rest_framework import serializers
from .models import Loan
from followers.utils import send_mail_on_change
from books.models import Book
from exemplaries.models import Exemplary
from django.shortcuts import get_object_or_404


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = ["id", "exemplary", "user", "return_date",
                  "returned_date", "loan_date"]

        extra_kwargs = {"return_date": {"read_only": True},
                        "loan_date": {"read_only": True},
                        "user": {"read_only": True},
                        "id": {"read_only": True}}

    def create(self, validated_data):
        exemplary = get_object_or_404(
            Exemplary,
            pk=validated_data["exemplary"].id
        )
        book = get_object_or_404(
            Book,
            pk=exemplary.id
        )

        instance_updated = super().update(exemplary, validated_data)
        quantity = instance_updated.quantity

        if quantity == 0:
            send_mail_on_change(instance_updated, book.title, "indisponível")

        if quantity > 0:
            send_mail_on_change(instance_updated, book.title, "disponível")

        return instance_updated


class ListLoanOwnerSerializer(serializers.Serializer):
    class Meta:
        model: Loan
        fields = [
            "id",
            "exemplary",
            "user",
            "return_date",
            "returned_date",
            "loan_date",
        ]

        extra_kwargs = {
            "return_date": {"read_only": True},
            "loan_date": {"read_only": True},
            "user": {"read_only": True},
            "id": {"read_only": True},
        }


class ListLoanOwnerSerializer(serializers.Serializer):
    class Meta:
        model: Loan
        fields = [
            "id",
            "exemplary",
            "user",
            "return_date",
            "returned_date",
            "loan_date",
        ]

        extra_kwargs = {
            "return_date": {"read_only": True},
            "loan_date": {"read_only": True},
            "user": {"read_only": True},
            "id": {"read_only": True},
        }
