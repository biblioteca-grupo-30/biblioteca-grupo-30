from .models import Exemplary
from .serializers import ExemplarySerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from books.models import Book
from rest_framework.views import Response, status


class ExemplaryView(CreateAPIView):
    queryset = Exemplary.objects.all()
    serializer_class = ExemplarySerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        serializer.save(book=book)

    def post(self, request, *args, **kwargs):
        try:
            exemplary = Exemplary.objects.get(pk=self.kwargs.get("pk"))
            return Response({"message": "Exemplary already exists."}, status.HTTP_409_CONFLICT)
        except Exemplary.DoesNotExist:
            return super().post(request, *args, **kwargs)


class ExamplaryRetriveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Exemplary.objects.all()
    serializer_class = ExemplarySerializer
