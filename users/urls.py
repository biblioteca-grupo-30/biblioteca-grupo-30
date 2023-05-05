from django.urls import path
from .views import UserView, UserDetailView
from followers.views import FollowerListCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/books/<int:pk>/follow/", FollowerListCreateView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/refresh/", TokenRefreshView.as_view()),
]
