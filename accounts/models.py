from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(
        max_length=255,
        null=False,
        unique=True)
    password=models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    
    # to give name to profile object representation
    def __str__(self):
        return self.first_name