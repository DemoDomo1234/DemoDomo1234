from django.db import models
from accounts.models import User
from django.urls import reverse


class List(models.Model):
    titel = models.CharField(max_length=50 , unique=True)
    user = models.ForeignKey(User, related_name='list_user', on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse("blog:BlogList")

class PlayList(models.Model):
    titel = models.CharField(max_length=50 , unique=True)
    user = models.ForeignKey(User, related_name='play_list_user', on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse("blog:BlogList")
