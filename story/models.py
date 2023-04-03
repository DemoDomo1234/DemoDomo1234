from django.db import models
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from accounts.models import User
from django.urls import reverse
from coments.models import Coments



class Story(models.Model):
    body = models.TextField()
    files = models.FileField(upload_to='story')
    likes = models.ManyToManyField(User, related_name = 'likes_story', blank= True)
    time = models.DateTimeField(auto_now_add=True )
    user = models.ForeignKey(User, related_name= 'user_story', on_delete=models.CASCADE , default=True)
    actived = models.BooleanField(default=True)
    tag = TaggableManager()
    comments = GenericRelation(Coments)
    views = models.ManyToManyField(User, related_name = 'views_story', blank= True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("blog:BlogDetail",args=[self.id] )

