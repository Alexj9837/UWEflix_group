from django.db import models

class Screen(models.Model):
    # Fields for the screen model
    screen_number = models.IntegerField()
    capacity = models.IntegerField()  # number of seats in the screen


    def __str__(self):
        return f'Screen {self.screen_number} (Capacity: {self.capacity})'
