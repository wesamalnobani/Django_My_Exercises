from django.db import models

# Create your models here.
class Person_User(models.Model):
    Full_Name = models.CharField(max_length=100)
    Email     = models.EmailField()
    Age       = models.IntegerField()
    Birth_Day = models.DateField()
class pic(models.Model):
    Name_Pic = models.CharField(max_length=50)
    Image    = models.ImageField(upload_to="Ex0101/static/Ex0101/img/")
