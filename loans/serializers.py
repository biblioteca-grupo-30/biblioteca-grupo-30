from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = ["id", "exemplary", "user", "return_date",
                  "returned_date", "loan_date"]

        extra_kwargs = {"return_date": {"read_only": True},
                        "loan_date": {"read_only": True},
                        "user": {"read_only": True},
                        "id": {"read_only": True}}
