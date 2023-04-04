from django.db import models
from UWEflix.models.show import Show

class Ticket(models.Model):
    showing = models.ForeignKey(Show, on_delete=models.CASCADE)