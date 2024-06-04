from django.db import models
from accounts.models import User
from django.urls import reverse


class List(models.Model):
    title = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, related_name='list_user',
                            on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video:VideoList")


class PlayList(models.Model):
    title = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, related_name='play_list_user',
                            on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video:VideoList")
