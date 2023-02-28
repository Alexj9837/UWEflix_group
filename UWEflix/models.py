from django.db import models
from django.contrib.auth.models import User 

class Contact(models.Model):
    landline = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, blank=False)

    def __str__(self):
        return str(self.email)

class Address(models.Model):
    street = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.street)


class Club(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    contact_details = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class ClubRepresentative(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_name)

class Film(models.Model):
    title = models.CharField(max_length=255)
    age_rating = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    trailer_description = models.TextField()

    def __str__(self):
        return str(self.title)

class Showing(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.film.title)

class Ticket(models.Model):
    showing = models.ForeignKey(Showing, on_delete=models.CASCADE)
    club_representative = models.ForeignKey(ClubRepresentative, on_delete=models.CASCADE)