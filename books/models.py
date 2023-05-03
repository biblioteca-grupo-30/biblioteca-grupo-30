from django.db import models


class Books(models.Model):
    title = models.CharField(unique=True, max_length=200)
    status = models.BooleanField(default=True)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.title

