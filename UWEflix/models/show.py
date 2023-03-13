from django.db import models
from UWEflix.models.screen import Screen
from UWEflix.models.film import films

class Show(models.Model):
    # Fields for the show model
    show_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(films, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        pass

    def __str__(self):
        return f'{self.film} at {self.screen} on {self.date} at {self.time}'
