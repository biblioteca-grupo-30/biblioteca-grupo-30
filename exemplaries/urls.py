from django.urls import path
from .views import ExemplaryView, ExemplaryDetailView

urlpatterns = [
    path("<int:pk>/exemplaries/", ExemplaryView.as_view()),
    path("exemplaries/<int:pk>/", ExemplaryDetailView.as_view()),
]
