from django.shortcuts import render, get_object_or_404
from .models import What_We_Do
from main.models import lists


def what_we_do(request):
    projects = What_We_Do.objects.all()
    list_items = lists.objects.all()
    return render(request, 'what_we_do/what_we_do.html', {'projects': projects, 'lists': list_items})

def what_we_do_details(request, project_id):
    list_items = lists.objects.all()
    project = get_object_or_404(What_We_Do, pk=project_id)  # Use singular variable name
    return render(request, 'what_we_do/what_we_do_detail.html', {'project': project, 'lists': list_items})
