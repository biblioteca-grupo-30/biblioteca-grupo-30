from .models import Exemplary
from .serializers import ExemplarySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from books.models import Books


class ExemplaryView(ListCreateAPIView, PageNumberPagination):
    queryset = Exemplary.objects.all()
    serializer_class = ExemplarySerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Books, pk=self.kwargs.get("pk"))

        serializer.save(book=book)


class ExemplaryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Exemplary.objects.all()
    serializer_class = ExemplarySerializer

