from django import template
from blog.models import User
from django.db.models import Count

register = template.Library()

@register.simple_tag()
def folower_count(user):
    folower = User.objects.filter(id=user.id).aggregate(Count('folower'))
    return folower['folower__count']
