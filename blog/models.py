from django.db import models
from accounts.models import account
from django.urls import reverse

class Tag(models.Model):
    tag = models.CharField(max_length=20)

class BlogPoblish(models.Manager):
    def poblished(self):
        return self.filter(poblish = True)

class Blog(models.Model):
    titel = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='mdia')
    film = models.FileField(upload_to='film')
    date = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    date_poblish = models.DateField(auto_now=True)
    poblish = models.BooleanField()
    likes = models.ManyToManyField(account, related_name = 'likes_blog', blank= True)
    author = models.ForeignKey(account, related_name= 'author_blog', on_delete=models.CASCADE , default=True)
    unlikes = models.ManyToManyField(account, related_name = 'unlikes_blog', blank= True)
    saved = models.ForeignKey(account, related_name= 'saved_blog', on_delete=models.CASCADE , default=True)
    tag = models.ManyToManyField(Tag , related_name = 'tag_blog', blank= True)
    views = models.ManyToManyField(account, related_name = 'views_blog', blank= True)

    objects = BlogPoblish()

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse("blog:BlogList")

class Story(models.Model):
    body = models.TextField()
    files = models.FileField(upload_to='story')
    likes = models.ManyToManyField(account, related_name = 'likes_stoy', blank= True)
    time = models.DateTimeField(auto_now_add=True )