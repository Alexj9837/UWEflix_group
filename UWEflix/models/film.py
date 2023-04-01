from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="pics", default="default.png")
    date = models.DateField()
    duration = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    cast = models.TextField(max_length=100)
    trailer = models.CharField(max_length=100)
    up = models.BooleanField(default=False)
    price = models.IntegerField(default=0)






