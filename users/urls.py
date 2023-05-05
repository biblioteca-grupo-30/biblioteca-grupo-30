from django.urls import path
from .views import UserView, UserDetailView, FollowView
# from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("users/", UserView.as_view()),
<<<<<<< HEAD
    path("users/<int:user_id>/", UserDetailView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/refresh/", TokenRefreshView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
=======
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/books/<int:pk>/follow/", FollowView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/refresh/", TokenRefreshView.as_view()),
>>>>>>> 3e6da546ca7038d6cab6003a9b6f19f7f321706f
]
