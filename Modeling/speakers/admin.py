from django.contrib import admin
from .models import Speaker
# Register your models here.
#@admin.register(Speaker)
admin.site.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_info']
    search_fields = ['name']
