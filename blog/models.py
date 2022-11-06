from django.db import models
from accounts.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from coments.models import Coments

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

class BlogPoblish(models.Manager):
    def poblished(self):
        return self.filter(poblished = True)

class Blog(models.Model):
    titel = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='mdia')
    film = models.FileField(upload_to='film')
    date = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    poblished = models.BooleanField()
    likes = models.ManyToManyField(User, related_name = 'likes_blog', blank= True)
    author = models.ForeignKey(User, related_name= 'author_blog', on_delete=models.CASCADE , default=True)
    unlikes = models.ManyToManyField(User, related_name = 'unlikes_blog', blank= True)
    saved = models.ManyToManyField(User, related_name= 'saved_blog', default=True)
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

class Post(models.Model):
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name = 'likes_post', blank= True)
    unlikes = models.ManyToManyField(User, related_name = 'unlikess_post', blank= True)
    time = models.DateTimeField(auto_now_add=True )
    user = models.ForeignKey(User, related_name= 'users_post', on_delete=models.CASCADE , default=True)
    comments = GenericRelation(Coments)
    views = models.ManyToManyField(User, related_name = 'views_post', blank= True)

    def __str__(self):
        return self.body
        
    def get_absolute_url(self):
        return reverse("blog:BlogDetail",args=[self.id] )

class Image(models.Model):
    post = models.ForeignKey(Post , related_name="post_images" , on_delete = models.CASCADE , null =  True , blank = True)
    image = models.ImageField( upload_to='media' , null =  True , blank = True)
    time = models.DateTimeField(auto_now_add=True )

    def get_absolute_url(self):
        return reverse("blog:BlogList")
        