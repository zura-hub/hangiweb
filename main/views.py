from django.shortcuts import render

from .models import About, Mission, Activities, Photo, lists, Contact


def index(request):
    abouts = About.objects.all()
    missions = Mission.objects.all()
    activities = Activities.objects.all()
    photos = Photo.objects.all()
    list = lists.objects.all()
    return render(request, 'main/index.html', {'lists' : list, 'abouts': abouts, 'photos': photos, 'missions': missions, 'activities': activities})




def contact(request):
    contacts = Contact.objects.all()
    list_items = lists.objects.all()
    return render(request, 'main/info.html', {'contacts': contacts, 'lists': list_items})
