
from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo, Title
from main.models import lists

def gallery(request):
    titles = Title.objects.all()
    photos = Photo.objects.all()
    list_items = lists.objects.all()
    return render(request, 'Gallery/gallery.html', {'title': titles, 'photos': photos, 'lists': list_items})
