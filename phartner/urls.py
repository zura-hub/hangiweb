from django.urls import path
from .views import partner

urlpatterns = [
    path('phartner/', partner, name='Phartner'),
]
