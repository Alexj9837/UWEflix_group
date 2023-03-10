from django.db import models
from UWEflix.models.show import Show
from UWEflix.models.clubrep import ClubRepresentative

class Ticket(models.Model):
    showing = models.ForeignKey(Show, on_delete=models.CASCADE)
    club_representative = models.ForeignKey(ClubRepresentative, on_delete=models.CASCADE)