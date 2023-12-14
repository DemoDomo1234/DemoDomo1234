from django import template
from video.models import Video
from django.db.models import Count 

register = template.Library()

@register.simple_tag()
def video_like_count(video):
    likes = Video.objects.filter(id=video.id).aggregate(Count('likes'))
    return likes['likes__count']

@register.simple_tag()
def video_unlike_count(blog):
    un_likes = Video.objects.filter(id=blog.id).aggregate(Count('un_likes'))
    return un_likes['un_likes__count']

@register.simple_tag()
def video_comment_count(blog):
    comments = Video.objects.filter(id=blog.id).aggregate(Count('comments'))
    return comments['comments__count']

@register.simple_tag()
def video_view_count(blog):
    views = Video.objects.filter(id=blog.id).aggregate(Count('views'))
    return views['views__count']


@register.simple_tag()
def video_saved_count(video):
    saved = Video.objects.filter(id=video.id).aggregate(Count('saved'))
    return saved['saved__count']
