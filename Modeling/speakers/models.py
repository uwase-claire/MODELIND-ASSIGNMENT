from django.db import models

# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    contact_info = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='speaker_images')
    expertise_areas = models.CharField(max_length=255)

    def __str__(self):
        return self.name
