from django.contrib import admin
from .models import Club, ClubRepresentative, Film, Showing, Ticket
# Register your models here.


admin.site.register(Club)
admin.site.register(ClubRepresentative)
admin.site.register(Film)
admin.site.register(Showing)
admin.site.register(Ticket)