from rest_framework.generics import ListCreateAPIView
# from rest_framework import generics
from .models import Books
from .serializers import BookSerializer


class BookView(ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

# class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
