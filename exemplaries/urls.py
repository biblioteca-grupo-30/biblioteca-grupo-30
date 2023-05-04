from django.urls import path
from .views import ExemplaryView, ExamplaryRetriveUpdate

urlpatterns = [
    path("exemplaries/<int:pk>/", ExemplaryView.as_view()),
    path("exemplaries-detail/<int:pk>/", ExamplaryRetriveUpdate.as_view()),
]
