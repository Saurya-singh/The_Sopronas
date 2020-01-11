from django.db import models

# Create your models here.
class Status (models.Model):
    fullname = models.CharField(max_length=40)
    status = models.CharField(max_length=200)
    