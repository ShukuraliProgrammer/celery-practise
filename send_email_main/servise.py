from django.core.mail import send_mail

def send(email,message):
    send_mail(
        'Subject here',
        message,
        'shukurdev2002@gmail.com',
        [email],
        fail_silently=False,
    )
