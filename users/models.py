from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    password = models.CharField(max_length=127)
    is_blocked = models.BooleanField(default=False)
    blocked_until = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)

    books_followed = models.ManyToManyField(
        "books.Book",
        related_name="users_following"
    )
