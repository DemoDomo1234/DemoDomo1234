from django import template
from django.db.models import Count 
from coments.models import Coments

register = template.Library()

@register.simple_tag()
def likes_count(coment):
    likes = Cuments.objects.filter(id-coment.id).aggregate(Count('likes'))
    return likes['likes__count']

@register.simple_tag()
def unlikes_count(coment):
    unlikes = Cuments.objects.filter(id-coment.id).aggregate(Count('unlikes'))
    return unlikes['unlikes__count']

@register.simple_tag()
def one_coments_count(coment):
    one_coments = Coments.objects.filter(one_coments = coment).aggregate(Count('one_coments'))
    return one_coments['one_coments__count']

@register.simple_tag()
def tow_coments_count(coment):
    tow_coments = Coments.objects.filter(tow_coments = coment).aggregate(Count('tow_coments'))
    return tow_coments['tow_coments__count']
