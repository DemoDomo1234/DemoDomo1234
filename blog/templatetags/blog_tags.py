from django import template
from blog.models import Blog
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
