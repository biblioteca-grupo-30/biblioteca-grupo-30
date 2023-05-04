from django.db import models
from datetime import timedelta


class Loan(models.Model):
    exemplary = models.ForeignKey("exemplare.Exemplary",
                                  on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    return_date = models.DateTimeField()
    returned_date = models.DateTimeField(blank=True, null=True)
    blocked_until = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.return_date.weekday() >= 5:
            self.return_date = self.return_date + timedelta(
                days=(7 - self.return_date.weekday()))
        super().save(*args, **kwargs)
