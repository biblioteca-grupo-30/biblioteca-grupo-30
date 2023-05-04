from .models import Exemplary
from .serializers import ExemplarySerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from books.models import Book


class ExemplaryView(CreateAPIView):
    queryset = Exemplary.objects.all()
    serializer_class = ExemplarySerializer

    def perform_create(self, serializer):

        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        serializer.save(book=book)


class ExamplaryRetriveUpdate(RetrieveUpdateDestroyAPIView,
                             PageNumberPagination):
    queryset = Exemplary.objects.all()
    serializer_class = ExemplarySerializer
