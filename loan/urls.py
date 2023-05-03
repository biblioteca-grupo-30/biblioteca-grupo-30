from django.urls import path
from .views import LoanListCreateAPIView, LoanRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("loan/", LoanListCreateAPIView.as_view()),
    path("books/<int:id>/", LoanRetrieveUpdateDestroyAPIView.as_view()),
]
