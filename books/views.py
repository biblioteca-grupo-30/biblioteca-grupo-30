from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"