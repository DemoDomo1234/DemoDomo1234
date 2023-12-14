from django import template
from django.db.models import Count 
from comments.models import Comments


register = template.Library()


@register.simple_tag()
def comment_like_count(comment):
    likes = Comments.objects.filter(id=comment.id).aggregate(Count('likes'))
    return likes['likes__count']


@register.simple_tag()
def comment_un_like_count(comment):
    un_likes = Comments.objects.filter(id=comment.id).aggregate(Count('un_likes'))
    return un_likes['un_likes__count']


@register.simple_tag()
def reply_comment_count(comment):
    reply = Comments.objects.filter(reply=comment.id).aggregate(Count('reply'))
    return reply['reply__count']


@register.simple_tag()
def reply_to_reply_comment_count(comment):
    reply_to_reply = Comments.objects.filter(reply_to_reply=comment.id).aggregate(Count('reply_to_reply'))
    return reply_to_reply['reply_to_reply__count']
