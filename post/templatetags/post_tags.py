from django import template
from post.models import Post
from django.db.models import Count 

register = template.Library()


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
