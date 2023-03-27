from django.contrib import admin
from .models.show import Show
from .models.film import films
from .models.upcoming import upcomings
from .models.screen import Screen
from .models.booking import Booking


# Register your models here.


admin.site.register(Show)
admin.site.register(films)
admin.site.register(upcomings)
admin.site.register(Screen) 
admin.site.register(Booking) 