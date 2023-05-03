from datetime import timedelta
from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Loan
from .serializers import LoanSerializer
from django.shortcuts import get_object_or_404


class LoanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        exemplare = get_object_or_404(Exemplare, pk=serializer.
                                      validated_data["exemplare"].id)
        user = self.request.user
        duration = serializer.validated_data.get("duration", exemplare
                                                 .default_loan_duration)

        # Cria um objeto datetime com a data atual e adiciona a duração em dias
        return_date = timezone.now() + timedelta(days=duration)

        # Verifica se a data de retorno cai em um
        # fim de semana e, se sim, define para o próximo dia útil
        if return_date.weekday() >= 5:
            return_date += timedelta(days=2)

        loan = serializer.save(user=user, return_date=return_date)


class LoanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
