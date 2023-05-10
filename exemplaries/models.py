from django.db import models


class Exemplary(models.Model):
    quantity = models.IntegerField()
    default_loan_duration = models.IntegerField(default=7)

    book = models.ForeignKey(
        "books.Book", related_name="exemplaries", on_delete=models.CASCADE
    )
