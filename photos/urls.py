from django.urls import path
from .views import photoView


urlpatterns = [
    path('', photoView, name='home'),
]