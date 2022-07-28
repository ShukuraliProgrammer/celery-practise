
from django.shortcuts import render
from photos.models import Photo

from .tasks import task_save_latest_flickr_image
def photoView(request, *args, **kwargs):
    model = Photo.objects.all()
    template_name = 'photos/photo_list.html'
    context = {
        'photos': model
    }
    task_save_latest_flickr_image.delay(*args, **kwargs)
    return render(request, template_name, context = context)
