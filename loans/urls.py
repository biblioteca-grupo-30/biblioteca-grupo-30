from django.urls import path
from .views import LoanListCreateAPIView, LoanRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("loan/", LoanListCreateAPIView.as_view()),
    path("loans/<int:pk>/", LoanRetrieveUpdateDestroyAPIView.as_view()),
]
