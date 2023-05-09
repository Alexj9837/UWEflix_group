from django.db import models
from UWEflix.models.clubs import Club
from UWEflix.models.user import Custom_user 

class ClubRepresentative(models.Model):
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_name)