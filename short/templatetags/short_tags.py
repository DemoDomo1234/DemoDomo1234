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
