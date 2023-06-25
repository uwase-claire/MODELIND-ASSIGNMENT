from django.urls import path
from . import views

app_name = 'conferences'

urlpatterns = [
    path('', views.create_conference),
    path('', views.update_conference),
    path('', views.delete_conference),
    path('', views.conference_details),
    path('', views.conference_list),
]
