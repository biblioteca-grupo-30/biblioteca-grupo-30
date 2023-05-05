from datetime import timedelta
from django.forms import ValidationError
from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from exemplaries.models import Exemplary
from .models import Loan
from .serializers import LoanSerializer
from django.shortcuts import get_object_or_404


class LoanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        exemplary = get_object_or_404(Exemplary, pk=serializer.
                                      validated_data["exemplary"].id)
        user = self.request.user

        if Loan.objects.filter(user=user,
                               exemplary__book=exemplary.book).exists():
            raise ValidationError("Usuário já tem um exemplar \
emprestado para este livro")

        duration = serializer.validated_data.get("duration", exemplary
                                                 .default_loan_duration)

        return_date = timezone.now() + timedelta(days=duration)

        if return_date.weekday() >= 5:
            return_date += timedelta(days=2)

        loan = serializer.save(user=user, return_date=return_date)

        exemplary.quantity -= 1
        exemplary.save()

        return loan


class LoanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
