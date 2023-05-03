from .models import Exemplary
from .serializers import ExemplarySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ExemplaryView(ListCreateAPIView):
    queryset = Exemplary.objects.all()
    serializer_class = ExemplarySerializer


class ExemplaryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Exemplary.objects.all()
    serializer_class = ExemplarySerializer
