from django.db import models
from django.utils import timezone

class Club(models.Model):
    # Fields for the club model
    clubID = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    post_code = models.CharField(max_length=10)
    landline_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()

    def __str__(self):
        return self.club_name