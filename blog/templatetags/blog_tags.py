from django import template
from blog.models import (Blog, Story, Short, Post)
from django.db.models import Count 

register = template.Library()

@register.simple_tag()
def blog_like_count(blog):
    likes = Blog.objects.filter(id=blog.id).aggregate(Count('likes'))
    return likes['likes__count']

@register.simple_tag()
def blog_unlike_count(blog):
    unlikes = Blog.objects.filter(id=blog.id).aggregate(Count('unlikes'))
    return unlikes['unlikes__count']

@register.simple_tag()
def blog_coment_count(blog):
    coments = Blog.objects.filter(id = blog.id).aggregate(Count('coments'))
    return coments['coments__count']

@register.simple_tag()
def blog_view_count(blog):
    views = Blog.objects.filter(id = blog.id).aggregate(Count('views'))
    return views['views__count']

@register.simple_tag()
def story_like_count(story):
    likes = Story.objects.filter(id=story.id).aggregate(Count('likes'))
    return likes['likes__count']

@register.simple_tag()
def story_coment_count(story):
    coments = Story.objects.filter(id = story.id).aggregate(Count('coments'))
    return coments['coments__count']

@register.simple_tag()
def story_view_count(story):
    views = Story.objects.filter(id = story.id).aggregate(Count('views'))
    return views['views__count']

@register.simple_tag()
def post_like_count(post):
    likes = Post.objects.filter(id=post.id).aggregate(Count('likes'))
    return likes['likes__count']

@register.simple_tag()
def post_unlike_count(post):
    unlikes = Post.objects.filter(id=post.id).aggregate(Count('unlikes'))
    return unlikes['unlikes__count']

@register.simple_tag()
def post_coment_count(post):
    coments = Post.objects.filter(id = post.id).aggregate(Count('coments'))
    return coments['coments__count']

@register.simple_tag()
def post_view_count(post):
    views = Post.objects.filter(id = post.id).aggregate(Count('views'))
    return views['views__count']

@register.simple_tag()
def short_like_count(short):
    likes = Short.objects.filter(id=short.id).aggregate(Count('likes'))
    return likes['likes__count']

@register.simple_tag()
def short_unlike_count(short):
    unlikes = Short.objects.filter(id=short.id).aggregate(Count('unlikes'))
    return unlikes['unlikes__count']

@register.simple_tag()
def short_coment_count(short):
    coments = Short.objects.filter(id = short.id).aggregate(Count('coments'))
    return coments['coments__count']

@register.simple_tag()
def short_view_count(short):
    views = Short.objects.filter(id = short.id).aggregate(Count('views'))
    return views['views__count']
