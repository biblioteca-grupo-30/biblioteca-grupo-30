from django.urls import path
from exemplaries.views import ExamplaryRetriveUpdate, ExemplaryView
from .views import (
    BookView,
    BookRetrieveView,
    BookUpdateDestroyView,
    ListBookView
)


urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/list/", ListBookView.as_view()),
    path("books/delete-update/<int:pk>/",
         BookUpdateDestroyView.as_view(), name="bookUpdateDestroyView"),
    path("books/<int:pk>/", BookRetrieveView.as_view(),
         name="bookRetrieveView"),
    path("books/exemplaries/<int:pk>/", ExemplaryView.as_view()),
    path("books/exemplaries-detail/<int:pk>/",
         ExamplaryRetriveUpdate.as_view())
]
