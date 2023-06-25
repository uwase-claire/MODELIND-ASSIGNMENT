"""
URL configuration for conference_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from conferences import views
from speakers import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('conferences/', include('conferences.urls')),
    path('speakers/', include('speakers.urls')),
    #conference paths
    path('create_conference/', views.create_conference),
    path('update_conference/', views.update_conference),
    path('delete_conference/', views.delete_conference),
    path('conference_details/', views.conference_details),
    path('conference_list/', views.conference_list),
    #speaker paths
    path('create_speaker/', views.create_speaker),
    path('delete_speaker/', views.delete_speaker),
    path('speaker_details/', views.speaker_details),
    path('speaker_list/', views.speaker_list),
    path('update_speaker/', views.update_speaker),
   

]

