from books.permissions import IsAuthenticatedOrReadOnly, IsUserAdmin
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView)
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ListBookView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class BookUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"
