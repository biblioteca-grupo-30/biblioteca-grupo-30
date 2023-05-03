from django.urls import path
from .views import ExemplaryView, ExemplaryDetailView

urlpatterns = [
    path("exemplaries/<int:pk>/", ExemplaryView.as_view()),
    path("exemplaries-detail/<int:pk>/", ExemplaryDetailView.as_view()),
]
