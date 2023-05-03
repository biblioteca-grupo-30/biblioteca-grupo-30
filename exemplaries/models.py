from django.db import models


class Exemplary(models.Model):
    quantity = models.IntegerField()

    book = models.ForeignKey(
        "books.Books", related_name="exemplaries", on_delete=models.CASCADE
    )
