from django.db import models

class Contact(models.Model):
    landline = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, blank=False)

    def __str__(self):
        return str(self.email)