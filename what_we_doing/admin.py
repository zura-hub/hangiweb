from django.contrib import admin
from .models import What_We_Doing

@admin.register(What_We_Doing)
class What_We_DoingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )
    search_fields = ('title', 'description', )
