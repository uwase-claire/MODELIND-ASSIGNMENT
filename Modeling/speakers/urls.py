from django.urls import path
from . import views

app_name = 'speakers'

urlpatterns = [
    path('create/', views.create_speaker, name='create_speaker'),
    path('update/<int:speaker_id>/', views.update_speaker, name='update_speaker'),
    path('delete/<int:speaker_id>/', views.delete_speaker, name='delete_speaker'),
    path('details/<int:speaker_id>/', views.speaker_details, name='speaker_details'),
    path('list/', views.speaker_list, name='speaker_list'),
]
