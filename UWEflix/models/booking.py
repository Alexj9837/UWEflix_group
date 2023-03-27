from django.db import models
#from UWEflix.models.film import films
from UWEflix.models.show import Show

class Booking(models.Model):
    # Fields for the booking model
    booking_id = models.AutoField(primary_key=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    
    # ticket_adult = models.CharField(max_length=7)
    # ticket_children = models.CharField(max_length=7)
    # ticket_student = models.CharField(max_length=7)

    quantity_adult = models.IntegerField()
    quantity_children = models.IntegerField()
    quantity_student = models.IntegerField()

    card_number = models.IntegerField(null=True)
    card_holder = models.CharField(max_length=30,null=True)
    card_expire_year  = models.IntegerField(null=True)
    card_expire_month  = models.IntegerField(null=True)
    card_cvc  = models.IntegerField(null=True)

    email = models.EmailField(null=True)

    class Meta:
        pass
    
    def __str__(self):
        # return f'Booking {self.booking_id} for {self.show} ({self.quantity} {self.ticket_type} tickets)'
        return f'Booking {self.booking_id} for {self.show}'