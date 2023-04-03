from django.db import models
from accounts.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from coments.models import Coments
from list.models import List, PlayList



class BlogPoblish(models.Manager):
    def poblished(self):
        return self.filter(poblished=True)


class Blog(models.Model):
    titel = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='mdia')
    film = models.FileField(upload_to='film')
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    poblished = models.BooleanField()
    likes = models.ManyToManyField(User, related_name='likes_blog', blank=True)
    author = models.ForeignKey(User, related_name='author_blog', on_delete=models.CASCADE, default=True)
    unlikes = models.ManyToManyField(User, related_name='unlikes_blog', blank=True)
    saved = models.ManyToManyField(User, related_name='saved_blog', default=True)
    tag = TaggableManager()
    views = models.ManyToManyField(User, related_name = 'views_blog', blank= True)
    lists = models.ManyToManyField(List , related_name='list' , blank= True)
    playlists = models.ManyToManyField(PlayList , related_name='play_list' , blank= True)
    comments = GenericRelation(Coments)
    objects = BlogPoblish()

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse("blog:BlogDetail",args=[self.id] )

