from django.db import models
from accounts.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comments(models.Model):
    reply = models.ForeignKey('self', related_name="comment_reply",
        on_delete=models.CASCADE, null=True, blank=True,
        default=None)
    reply_to_reply = models.ForeignKey('self', related_name="comment_reply_to_reply",
        on_delete=models.CASCADE, null=True, blank=True,
        default=None)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='author_comments',
                            on_delete=models.CASCADE, default=True)
    likes = models.ManyToManyField(User, related_name='likes_comments', blank=True)
    un_likes = models.ManyToManyField(User, related_name='un_likes_comments', blank=True)
    content_type = models.ForeignKey(ContentType, related_name="content_type_comments",
                                    on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.body[:10]

    def get_absolute_url(self):
        return reverse("chat:VideoList")
