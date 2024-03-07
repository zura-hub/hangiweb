
from django.urls import path
from . import views

urlpatterns = [
    path('our_team/', views.team, name='team'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
]
