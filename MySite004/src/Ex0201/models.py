from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name  = models.CharField(max_length=50)
    Email      = models.EmailField()
    Birth_Day  = models.DateField()
    def __str__ (self):
        return self.First_Name,self.Last_Name
class info(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    job  = models.CharField(max_length=50)
    lang = models.CharField(max_length=50)
    num  = models.IntegerField()
