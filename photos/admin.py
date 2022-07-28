from django.contrib import admin

from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'url')
    list_per_page = 20

admin.site.register(Photo, PhotoAdmin)
