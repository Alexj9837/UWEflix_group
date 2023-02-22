from django.db import models
""" 
class Film(models.Model):
    # Fields for the film model
    film_title = models.CharField(max_length=100)
    age_rating = models.CharField(max_length=10)
    duration = models.IntegerField()  # in minutes
    description = models.TextField()

    def __str__(self):
        return self.film_title

class Screen(models.Model):
    # Fields for the screen model
    screen_number = models.IntegerField()
    capacity = models.IntegerField()  # number of seats in the screen

    def __str__(self):
        return f'Screen {self.screen_number} (Capacity: {self.capacity})'

class Show(models.Model):
    # Fields for the show model
    show_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.film} at {self.screen} on {self.date} at {self.time}'

class Booking(models.Model):
    # Fields for the booking model
    booking_id = models.AutoField(primary_key=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    ticket_type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    card_number = models.CharField(max_length=20)

    def __str__(self):
        return f'Booking {self.booking_id} for {self.show} ({self.quantity} {self.ticket_type} tickets)' """