from datetime import timedelta
from django.forms import ValidationError
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from exemplaries.models import Exemplary
from .models import Loan
from books.permissions import IsUserAdmin, IsAuthenticatedOrReadOnly
from .serializers import LoanSerializer
from django.shortcuts import get_object_or_404
from books.models import Book
from followers.utils import send_mail_on_change


class LoanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin | IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        exemplary = get_object_or_404(
            Exemplary, pk=serializer.validated_data["exemplary"].id
        )
        user = self.request.user
        book = exemplary.book

        if Loan.objects.filter(
            user=user, exemplary__book=book, returned_date__isnull=True
        ).exists():
            raise ValidationError(
                "Usuário já tem um exemplar emprestado para este livro."
            )

        duration = serializer.validated_data.get(
            "duration", exemplary.default_loan_duration
        )

        return_date = timezone.now() + timedelta(days=duration)
        if return_date.weekday() >= 5:
            return_date += timedelta(days=2)

        serializer.save(user=user, exemplary=exemplary, return_date=return_date, returned_date=None)
        exemplary.quantity -= 1
        exemplary.save()


class LoanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_url_kwarg = "pk"


class LoanReturnAPIView(generics.UpdateAPIView):
    serializer_class = LoanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def update(self, request, *args, **kwargs):
        loan = self.get_object()

        if loan.returned_date is not None:
            return Response(
                {"detail": "Este exemplar já foi devolvido."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        loan.returned_date = timezone.now()
        loan.save()
        exemplary = loan.exemplary
        exemplary.quantity += 1
        exemplary.save()

        exemplary = get_object_or_404(
            Exemplary,
            pk=exemplary.id
        )

        book = get_object_or_404(
            Book,
            pk=exemplary.book_id
        )

        if exemplary.quantity > 0:
            send_mail_on_change(loan, book.title, "disponível")

        serializer = self.get_serializer(loan)

        return Response(serializer.data)


class ListLoanOwner(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user)
