from datetime import timedelta
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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        exemplary = get_object_or_404(Exemplary, pk=serializer.validated_data["exemplary"].id)
        user = self.request.user
        duration = serializer.validated_data.get("duration", exemplary.default_loan_duration)

        # Cria um objeto datetime com a data atual e adiciona a duração em dias
        return_date = timezone.now() + timedelta(days=duration)

        # Verifica se a data de retorno cai em um
        # fim de semana e, se sim, define para o próximo dia útil
        if return_date.weekday() >= 5:
            return_date += timedelta(days=2)

        loan = serializer.save(user=user, return_date=return_date)

        exemplary.quantity -= 1
        exemplary.save()

        return loan


class LoanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
