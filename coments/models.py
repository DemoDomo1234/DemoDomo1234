from django.db import models
from accounts.models import account
from blog.models import Blog
from django.urls import reverse

class Coments(models.Model):
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(account, related_name= 'author_coments', on_delete=models.CASCADE , default=True)
    likes = models.ManyToManyField(account, related_name= 'likes_coments', blank= True)
    unlikes = models.ManyToManyField(account, related_name= 'unlikes_coments', blank= True)

    def get_absolute_url(self):
        return reverse("blog:BlogList")

class StoryComents(models.Model):
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(account, related_name= 'author_coments_story', on_delete=models.CASCADE , default=True)
    likes = models.ManyToManyField(account, related_name= 'likes_coments_story', blank= True)
    unlikes = models.ManyToManyField(account, related_name= 'unlikes_coments_story', blank= True)

    def get_absolute_url(self):
        return reverse("blog:storylist")