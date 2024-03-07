from django.contrib import admin
from .models import Photo, Title

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'header')


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('header',)
