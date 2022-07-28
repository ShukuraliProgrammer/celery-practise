from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm

from send_email_main.tasks import send_email
class ContactCreateView(CreateView):
    template_name = 'main/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = '/'

    def form_valid(self,form):
        form.save()
        #send(form.cleaned_data['email'],form.cleaned_data['message'])
        send_email.delay(form.instance.email,form.instance.message)
        return super().form_valid(form)

