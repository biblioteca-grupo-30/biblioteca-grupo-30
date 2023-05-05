from rest_framework.generics import ListCreateAPIView
from .models import Follower
from books.models import Book
from .serializers import FollowerSerializer
from django.shortcuts import get_object_or_404


class FollowerListCreateView(ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))

        serializer.save(book=book)
        return super().perform_create(serializer)
