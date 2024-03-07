from django.contrib import admin
from .models import What_We_Do

@admin.register(What_We_Do)
class What_We_DoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )
    search_fields = ('title', 'description', )
