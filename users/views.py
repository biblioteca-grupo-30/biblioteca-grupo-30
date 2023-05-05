from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination
from books.permissions import IsUserAdmin


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUserView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = "pk"

    # def get(self, request: Request, user_id: int) -> Response:
    #     user = get_object_or_404(User, pk=user_id)
    #     serializer = UserSerializer(user)
    #     self.check_object_permissions(request, user)
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def patch(self, request: Request, user_id: int) -> Response:
    #     user = get_object_or_404(User, pk=user_id)

    #     self.check_object_permissions(request, user)

    #     serializer = UserSerializer(user, request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)

    #     serializer.save()

    #     return Response(serializer.data, status.HTTP_200_OK)
