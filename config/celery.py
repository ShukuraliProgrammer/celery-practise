from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Tashkent')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'send-email-every-day-at-8': {
        'task': 'photos.tasks.task_save_latest_flickr_image',
        'task': 'send_email_main.tasks.send_beat_email',
        'schedule': crontab(minute='*/2'),
        # 'args': ()
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')