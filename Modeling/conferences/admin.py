from django.contrib import admin
from .models import Conference
# Register your models here.
#@admin.register(Conference)
admin.site.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'date', 'venue', 'theme']
    search_fields = ['name', 'category']
