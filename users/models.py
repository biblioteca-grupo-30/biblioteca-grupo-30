from django.db import models
from django.contrib.auth.models import AbstractUser


class StatusOptions(models.TextChoices):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    BLOCKED = "Blocked"


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    password = models.CharField(max_length=127)
    status = models.CharField(
        max_length=20,
        choices=StatusOptions.choices,
        default=StatusOptions.ACTIVE
    )
    is_superuser = models.BooleanField(default=False)
