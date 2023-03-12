from django.contrib import admin

from UWEflix.models.clubs import Club
from UWEflix.models.clubrep import ClubRepresentative
from UWEflix.models.film import Film
from UWEflix.models.show import Show
from UWEflix.models.ticket import Ticket

# Register your models here.
admin.site.register(Club)
admin.site.register(ClubRepresentative)
admin.site.register(Film)
admin.site.register(Show)
admin.site.register(Ticket)
