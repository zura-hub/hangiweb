from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import About, Mission, Activities, Photo, lists, Contact


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    fields = ('title', 'content')


@admin.register(Mission)
class MissionAdmin(TranslationAdmin):
    fields = ('headers', 'content')


@admin.register(Activities)
class ActivitiesAdmin(TranslationAdmin):
    fields = ('header', 'content')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(lists)
class ListsAdmin(admin.ModelAdmin):
    list_display = ('home', 'social', 'gallery', 'team', 'project', 'done', 'doing', 'partnership', 'apps', 'contact', 'meniu' )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('image', 'city', 'address', 'phone', 'email', )