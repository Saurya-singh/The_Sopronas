
from django.db import models
from django.utils import timezone as tz

# Create your models here.

class User (models.Model):
    user_name=models.TextField()
    user_email=models.TextField()
    user_address=models.TextField()
    user_gender=models.TextField()
    user_age=models.IntegerField(max_length=50)
    

    def __str__(self):
        return self.user_name

    
    def valid_name(self):
        return self.user_name != None

         
    def valid_gender(self):
        return self.user_gender=='male' or self.user_gender=='female' 

    def valid_age(self):
        return self.user_age>=18       




class Status (models.Model):
    fullname = models.CharField(max_length=40)
    yourpost = models.TextField()
    posteddate = models.DateTimeField(auto_now_add=False, default=tz.now)
    
    def __str__(self):
        return str(self.id) + " " + self.fullname + " " + self.yourpost


    def valid(self):
        return self.fullname != None 


    def length(self):
        return len(self.yourpost)<20






