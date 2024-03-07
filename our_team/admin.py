from django.contrib import admin
from .models import Employee, Team, GroupPhoto
from django.contrib.admin import ModelAdmin



@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ('name',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(GroupPhoto)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('description', 'image_preview')

    def image_preview(self, obj):
        return obj.image.url if obj.image else None

    image_preview.short_description = 'Image Preview'