from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=50)#input = text
    image = models.ImageField(upload_to="pics", default="default.png")#input = image
    date = models.DateField()#input = date
    duration = models.CharField(max_length=50)#input = number
    type = models.CharField(max_length=50)#input = text
    language = models.CharField(max_length=50)#input = text
    rating = models.CharField(max_length=50)#input = number
    cast = models.TextField(max_length=100)#input = text
    trailer = models.CharField(max_length=100)#input = text
    up = models.BooleanField(default=False)#input = checkbox
    price = models.IntegerField(default=0)#input = nuber






