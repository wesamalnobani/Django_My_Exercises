from django.db import models

# Create your models here.
class users (models.Model):
    fullname = models.CharField(max_length=100)
    email    = models.EmailField()
    age      = models.IntegerField()
    birthday = models.DateField()
    
