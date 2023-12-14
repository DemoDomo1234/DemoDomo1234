from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comments
from accounts.tasks import send_mail_task


@receiver(post_save, sender=Comments)
def send_notifications(sender, instance, created, *args, **kwargs):
    if created:
        if instance.reply != None or instance.reply_to_reply != None:
            email = instance.author.email
            massages = 'http://127.0.0.1:8000'+instance.get_absolute_url()
            send_mail_task(massages, email)