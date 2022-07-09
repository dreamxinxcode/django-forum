from django.db import models
from django.conf import settings


class Profile(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=25, unique=True)
    avatar = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.username