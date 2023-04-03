from celery import shared_task
from accounts.models import OTPCode
from django.core.mail import send_mail
from datetime import datetime, timedelta
import pytz


@shared_task
def remove_expired_otp_codes():
	expired_time = datetime.now(tz=pytz.timezone('UTC')) - timedelta(minutes=2)
	OTPCode.objects.filter(created__lt=expired_time).delete()


@shared_task
def send_mail_task(massages, email):
	send_mail('massages', massages, 'demodomone@gmail.com', [email],
    fail_silently=False, auth_password='moxczeohuhgyowqm')  
	
