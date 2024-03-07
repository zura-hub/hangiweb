from django.shortcuts import render
from .models import Blogs, Stories,Title
from main.models import lists

def social(request):
    title = Title.objects.all()
    stories = Stories.objects.all()
    blogs = Blogs.objects.all()
    list_items = lists.objects.all()
    return render(request, 'social/social.html', { 'title': title, 'blogs': blogs, 'stories': stories, 'lists': list_items})

