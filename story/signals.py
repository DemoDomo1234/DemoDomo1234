from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Story
from accounts.tasks import send_mail_task


@receiver(post_save, sender=Story)
def story_send_notifications(sender, instance, created, *args, **kwargs):
    if created:
        for user in instance.user.folower.all():
            massages = 'http://127.0.0.1:8000'+instance.get_absolute_url()
            email = user.email
            send_mail_task(massages, email)