from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id_card = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.username
