from django import template
from short.models import Short
from django.db.models import Count 

register = template.Library()

@register.simple_tag()
def short_like_count(short):
    likes = Short.objects.filter(id=short.id).aggregate(Count('likes'))
    return likes['likes__count']

@register.simple_tag()
def short_unlike_count(short):
    un_likes = Short.objects.filter(id=short.id).aggregate(Count('un_likes'))
    return un_likes['un_likes__count']

@register.simple_tag()
def short_comment_count(short):
    comments = Short.objects.filter(id=short.id).aggregate(Count('comments'))
    return comments['comments__count']

@register.simple_tag()
def short_view_count(short):
    views = Short.objects.filter(id=short.id).aggregate(Count('views'))
    return views['views__count']
