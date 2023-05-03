from django.urls import path
from .views import BookView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:id>/", BookRetrieveUpdateDestroyView.as_view(), name="bookRetrieveUpdateDestroyView"),
]