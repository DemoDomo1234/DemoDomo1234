from django.db import models
from accounts.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from coments.models import Coments



class Short(models.Model):
    body = models.TextField()
    files = models.FileField(upload_to='short')
    likes = models.ManyToManyField(User, related_name = 'likes_short', blank= True)
    unlikes = models.ManyToManyField(User, related_name = 'unlikes_short', blank= True)
    time = models.DateTimeField(auto_now_add=True )
    user = models.ForeignKey(User, related_name= 'user_short', on_delete=models.CASCADE , default=True)
    tag = TaggableManager()
    comments = GenericRelation(Coments)
    views = models.ManyToManyField(User, related_name = 'views_short', blank= True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("blog:BlogDetail",args=[self.id] )

