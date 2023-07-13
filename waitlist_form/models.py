from django.db import models

# Create your models here.

class WaitlistForm(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)