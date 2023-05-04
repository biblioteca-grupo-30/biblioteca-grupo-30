from rest_framework import serializers
from exemplaries.models import Exemplary
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "title", "author", "pages", "synopsis", "category", "is_available"]

    def get_is_available(self, obj):
        available_count = Exemplary.objects.filter(book=obj, quantity__gt=0).count()
        return available_count > 0

# class BookSerializer(serializers.ModelSerializer):
#     is_available = serializers.SerializerMethodField()

#     class Meta:
#         model = Book
#         fields = ["id", "title", "author", "pages", "synopsis", "category", "is_available"]

#     def get_is_available(self, obj):
#         examples = Exemplary.objects.filter(book=obj)
#         available_count = obj.examples_set.filter(quantity__gt=0).count()
#         return available_count > 0
