from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from UWEflix import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("upcoming", views.upcoming, name="upcoming"),
    #path("booking", views.booking, name="booking"),
    #path("booking_confirm", views.booking_confirm, name="booking_confirm"),
    path("film_details/<int:id>/", views.film_details, name="film_details"),
    path("film_details/<int:id>/booking/<int:pk>/", views.booking, name="booking"),
    path("film_details/<int:id>/booking/<int:pk>/tickets", views.ticketsPurchase, name="tickets_purchase"),
    path("film_details/<int:id>/booking/<int:pk>/tickets/<int:pi>/booking_processing", views.bookingProcessing, name="booking_processing"),
    path("film_details/<int:id>/booking/<int:pk>/tickets/<int:pi>/booking_processing/booking_confirm", views.booking_confirm, name="booking_confirm"),
    path("upcoming_details/<int:id>/", views.upcoming_details, name="upcoming_details"),
    path("create_club",views.create_club,name="create_club"),
    path("update_club",views.update_club,name="update_club"),
    path("delete_club",views.delete_club,name="delete_club"),
    path("view_club",views.Club_list_view,name="view_club"),

    path("login",views.login_page,name="login_page"),
    path("club_representative", views.club_representative_home, name="club_representative_home"),
    path("book",views.book_tickets,name="book_tickets"),
    path("manage",views.manage_account,name="manage_account"),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

