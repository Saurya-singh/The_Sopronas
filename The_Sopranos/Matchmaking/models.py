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


class Status (models.Model):
    fullname = models.CharField(max_length=40)
    yourpost = models.TextField()
    posteddate = models.DateTimeField(auto_now_add=False, default=tz.now)
    statuses=models.ForeignKey(User, on_delete=models.CASCADE)
    
def __str__(self):
    return str(self.id) + " " + self.fullname + " " + self.yourpost


class profile(models.Model):
    user_profile= models.ForeignKey(User, on_delete-models.CASCADE)

    
class Match (models.Model):
    match_name=models.TextField()
    match_email=models.TextField()
    matches=models.ManyToManyField(User)

class Messages (models.Model):
    sender_name = models.TextField()
    reciever_name= models.TextField()
    message = models.TextField()
    msg= models.ForeignKey(Match, on_delete-models.CASCADE)







