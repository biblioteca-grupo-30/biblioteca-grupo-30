from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt import views as jwt_views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
    path("login/", jwt_views.TokenObtainPairView.as_view()),
    path("refresh/", jwt_views.TokenRefreshView.as_view()),
]
