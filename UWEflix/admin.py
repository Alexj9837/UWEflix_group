from django.contrib import admin
from .models.show import Show
from .models.film import Film
from .models.upcoming import upcomings
from .models.screen import Screen
from .models.booking import Booking


from UWEflix.models.clubs import Club
from UWEflix.models.clubrep import ClubRepresentative
from UWEflix.models.film import Film
from UWEflix.models.show import Show
from UWEflix.models.ticket import Ticket
from .models.clubs import Club
from .models.clubrep import ClubRepresentative
from .models.ticket import Ticket
from .models.user import Custom_user

# Register your models here.
admin.site.register(Club)
admin.site.register(Film)
admin.site.register(Show)
admin.site.register(Ticket)
admin.site.register(upcomings)
admin.site.register(Screen) 
admin.site.register(Booking)
admin.site.register(ClubRepresentative)
admin.site.register(Custom_user)