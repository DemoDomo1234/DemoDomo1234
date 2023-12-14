from django import template
from video.models import User
from django.db.models import Count

register = template.Library()

@register.simple_tag()
def follower_count(user):
    follower = User.objects.filter(id=user.id).aggregate(Count('follower'))
    return follower['follower__count']
