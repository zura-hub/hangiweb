
from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('photo-list/', views.gallery, name='photo-list'),
]