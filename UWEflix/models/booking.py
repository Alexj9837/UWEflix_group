from django.db import models
from UWEflix.models.film import Film
from UWEflix.models.show import Show

class Booking(models.Model):
    # Fields for the booking model
    booking_id = models.AutoField(primary_key=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    ticket_type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    card_number = models.CharField(max_length=20)

    class Meta:
        pass
    
    def __str__(self):
        return f'Booking {self.booking_id} for {self.show} ({self.quantity} {self.ticket_type} tickets)'