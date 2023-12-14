from celery import shared_task
from story.models import Story
from datetime import datetime, timedelta
import pytz


@shared_task
def remove_expired_story():
	expired_time = datetime.now(tz=pytz.timezone('UTC')) - timedelta(day=7)
	Story.objects.filter(created__lt=expired_time).delete()

