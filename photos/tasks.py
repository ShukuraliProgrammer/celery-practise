from celery.schedules import crontab
from celery import shared_task
from celery import shared_task

from photos.utils import save_latest_flickr_image



@shared_task(bind=True)
def task_save_latest_flickr_image(*args, **kwargs):
    save_latest_flickr_image()
   