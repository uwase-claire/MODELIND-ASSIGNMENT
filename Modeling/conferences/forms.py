from django import forms
from .models import Conference

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'category', 'date', 'venue', 'theme']
