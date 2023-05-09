from django.urls import path
from .views import (
    LoanListCreateAPIView,
    LoanRetrieveUpdateDestroyAPIView,
    LoanReturnAPIView,
    ListLoanOwner
)

urlpatterns = [
    path("loan/", LoanListCreateAPIView.as_view()),
    path("loans/<int:pk>/", LoanRetrieveUpdateDestroyAPIView.as_view()),
    path("loans/returning/<int:pk>/", LoanReturnAPIView.as_view()),
    path("loans/owner/", ListLoanOwner.as_view()),
]
