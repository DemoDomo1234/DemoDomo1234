from django.db import models
from accounts.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comments
from list.models import List, PlayList



class VideoPublish(models.Manager):
    def published(self):
        return self.filter(published=True)


class Video(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='media')
    film = models.FileField(upload_to='film')
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    published = models.BooleanField()
    likes = models.ManyToManyField(User, related_name='likes_video', blank=True)
    author = models.ForeignKey(User, related_name='author_video',
                            on_delete=models.CASCADE, default=True)
    un_likes = models.ManyToManyField(User, related_name='un_likes_video', blank=True)
    saved = models.ManyToManyField(User, related_name='saved_video', default=True)
    tag = TaggableManager()
    views = models.ManyToManyField(User, related_name='views_video', blank=True)
    lists = models.ManyToManyField(List , related_name='list', blank=True)
    playlists = models.ManyToManyField(PlayList, related_name='play_list', blank=True)
    comments = GenericRelation(Comments)
    objects = VideoPublish()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video:VideoDetail", args=[self.id])

