from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ["id", "exemplare", "user", "return_date",
                  "returned_date", "blocked_until"]
