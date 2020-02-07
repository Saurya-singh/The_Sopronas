from django.db import models
from django.utils import timezone as tz

# Create your models here.



class Status(models.Model):
    fullname = models.CharField(max_length=40)
    yourpost = models.TextField()
    posteddate = models.DateTimeField(auto_now_add=False, default=tz.now)
   
    
def __str__(self):
    return str(self.id) + " " + self.fullname + " " + self.yourpost


