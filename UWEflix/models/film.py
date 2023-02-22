from django.db import models

class film(models.Model):
    # Fields for the film model
    film_title = models.CharField(max_length=100)
    age_rating = models.CharField(max_length=10)
    duration = models.IntegerField()  # in minutes
    description = models.TextField()

    def __str__(self):
        return self.film_title