from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('photos/', include('photos.urls')),
    path('send_email/', include('send_email_main.urls')),
]
