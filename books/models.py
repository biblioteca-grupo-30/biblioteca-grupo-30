from django.db import models

class Book(models.Model):
    title = models.CharField(unique=True, max_length=200)
    author = models.CharField(max_length=155)
    synopsis = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.title
