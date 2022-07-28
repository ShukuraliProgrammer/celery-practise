from config.celery import app
from django.core.mail import send_mail
from .servise import send
from .models import Contact

@app.task
def send_email(email,message):
    send(email,message)

@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'This is beat task',
            contact.message,
            'rezamonovshukurali21@gmail.com',
            contact.email,
            fail_silently=False,
            )
