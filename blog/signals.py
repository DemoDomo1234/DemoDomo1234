from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (Blog, Story, Short, Post)
from django.core.mail import send_mail

@receiver(post_save, sender=Blog)
def blog_send_notifications(sender, instance, created, *args, **kwargs):
    if created:
        for user in instance.author.folower.all():
            email = user
            send_mail(instance.titel, 'http://127.0.0.1:8000'+instance.get_absolute_url(),
            'demodomone@gmail.com', [email], fail_silently=False, auth_password='jjbkvvclqseeixhx')

@receiver(post_save, sender=Story)
def story_send_notifications(sender, instance, created, *args, **kwargs):
    if created:
        for user in instance.user.folower.all():
            email = user.email
            send_mail('noty',  'http://127.0.0.1:8000'+instance.get_absolute_url(),
            'demodomone@gmail.com', [email], fail_silently=False, auth_password='jjbkvvclqseeixhx')

@receiver(post_save, sender=Short)
def short_send_notifications(sender, instance, created, *args, **kwargs):
    if created:
        for user in instance.user.folower.all():
            email = user.email
            send_mail('noty', 'http://127.0.0.1:8000'+instance.get_absolute_url(),
            'demodomone@gmail.com', [email], fail_silently=False, auth_password='jjbkvvclqseeixhx')

@receiver(post_save, sender=Post)
def post_send_notifications(sender, instance, created, *args, **kwargs):
    if created:
        for user in instance.user.folower.all():
            email = user.email
            send_mail('noty', 'http://127.0.0.1:8000'+instance.get_absolute_url(),
            'demodomone@gmail.com', [email], fail_silently=False, auth_password='jjbkvvclqseeixhx')
