from tabnanny import verbose
from django.db import models
from profiles.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Forum(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Thread(models.Model):
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
    forum = models.OneToOneField(Forum, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
    thread = models.OneToOneField(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}'