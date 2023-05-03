from django.urls import path
from .views import ExemplaryView, ExemplaryDetailView

urlpatterns = [
    path("exemplaries/", ExemplaryView.as_view()),
    path("exemplaries/<int:pk>/", ExemplaryDetailView.as_view()),
]
