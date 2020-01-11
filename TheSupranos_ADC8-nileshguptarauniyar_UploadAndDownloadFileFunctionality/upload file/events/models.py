from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField('Event Name',max_length=100)
    venue = models.CharField('Venue',max_length=100)
    event_date = models.DateTimeField('Event Date')
    manager = models.CharField('Manager Name', max_length=100)
    event_description=models.CharField('Event Description',max_length=200)    
