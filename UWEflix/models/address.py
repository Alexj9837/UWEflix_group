from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.street)