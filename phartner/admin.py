from django.contrib import admin
from .models import Phartner, MainTitle
from django.contrib.admin import ModelAdmin


@admin.register(Phartner)
class PhartnerAdmin(ModelAdmin):
    list_display = ('title', 'content')



@admin.register(MainTitle)
class MainTitleAdmin(ModelAdmin):
    list_display = ('title',)

