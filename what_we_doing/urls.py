# urls.py
from django.urls import path
from . import views

app_name = 'what_we_doing'

urlpatterns = [
    path('what_we_doing/', views.what_we_doing, name='what_we_doing'),
    path('what_we_doing/<int:project_id>/', views.what_we_doing_details, name='what_we_doing_details')
]
