from django.db import models

# Create your models here.

class Conference(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)

    def __str__(self):
        return self.name
