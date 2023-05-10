from rest_framework.generics import ListCreateAPIView
from .models import Follower
from books.models import Book
from .serializers import FollowerSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class FollowerListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def post(self, request, *args, **kwargs):
        try:
            book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
            user = self.request.user
            user_following = Follower.objects.get(pk=user.id)
            if user_following.user_id == user.id and user_following.book_id == book.id:
                raise ValueError("Você já está seguindo este livro.")

        except Follower.DoesNotExist:
            return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        user = self.request.user

        serializer.save(user=user, book=book)
