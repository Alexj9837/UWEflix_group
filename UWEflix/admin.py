from django.contrib import admin
from .models.show import Show
from .models.film import Film
from .models import upcoming
from .models.screen import Screen
from .models.booking import Booking


# Register your models here.


admin.site.register(Show)
admin.site.register(Film)
admin.site.register(upcoming.upcomings)
admin.site.register(Screen) 
admin.site.register(Booking) 