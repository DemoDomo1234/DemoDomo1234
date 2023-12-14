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
    un_likes = Post.objects.filter(id=post.id).aggregate(Count('un_likes'))
    return un_likes['un_likes__count']

@register.simple_tag()
def post_comment_count(post):
    comments = Post.objects.filter(id=post.id).aggregate(Count('comments'))
    return comments['comments__count']

@register.simple_tag()
def post_view_count(post):
    views = Post.objects.filter(id=post.id).aggregate(Count('views'))
    return views['views__count']
