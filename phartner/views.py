from django.shortcuts import render
from .models import Phartner, MainTitle
from main.models import  lists, Mission

def partner(request):
    main_titles = MainTitle.objects.all()
    phartner_photos = Phartner.objects.all()
    list_items = lists.objects.all()
    missions = Mission.objects.all()
    return render(request, 'phartner/phartner.html', {'main_titles': main_titles, 'phartner_photos': phartner_photos, 'lists': list_items, 'missions': missions})
