from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Coments
from django.core.mail import send_mail

@receiver(post_save, sender=Coments)
def send_notifications(sender, instance, created, *args, **kwargs):
    if created:
        if instance.one_coments != None or instance.tow_coments != None:
            email = instance.author.email
            send_mail('noty', 'http://127.0.0.1:8000'+instance.get_absolute_url(),
            'demodomone@gmail.com', [email], fail_silently=False, auth_password='jjbkvvclqseeixhx')
