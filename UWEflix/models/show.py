from django.db import models
from UWEflix.models.screen import screen
from UWEflix.models.film import film

class show(models.Model):
    # Fields for the show model
    show_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(film, on_delete=models.CASCADE)
    screen = models.ForeignKey(screen, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.film} at {self.screen} on {self.date} at {self.time}'
