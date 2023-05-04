from django.urls import path

from exemplaries.views import ExamplaryRetriveUpdate, ExemplaryView
from .views import BookView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:id>/", BookRetrieveUpdateDestroyView.as_view(), name="bookRetrieveUpdateDestroyView"),
    path("books/exemplaries/<int:pk>/", ExemplaryView.as_view()),
    path("books/exemplaries-detail/<int:pk>/", ExamplaryRetriveUpdate.as_view()),
]
