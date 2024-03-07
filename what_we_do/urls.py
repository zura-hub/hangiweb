from django.urls import path
from . import views

urlpatterns = [
    path('what_we_do/', views.what_we_do, name='what_we_do'),
    path('what_we_do/<int:project_id>/', views.what_we_do_details, name='what_we_do_details')
]