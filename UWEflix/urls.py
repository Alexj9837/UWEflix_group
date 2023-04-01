from django.urls import path
from UWEflix import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", views.home, name="home"),

#####################################################
######### FILMS/SHOWINGS/SCREENS/CLUBS ##############
#####################################################

    path("create_club",views.create_club,name="create_club"),
    path("create_film",views.create_film,name="create_film"),
    path("create_showing",views.create_showing,name="create_showing"),
    path("create_screen",views.create_screen,name="create_screen"),
    
    path("update_club /<str:pk>/",views.update_club,name="update_club"),
    path("update_film /<str:pk>/",views.update_film,name="update_film"),
    path("update_showing /<str:pk>/",views.update_showing,name="update_showing"),
    path("update_screen /<str:pk>/",views.update_screen,name="update_screen"),

    path("delete_club /<str:pk>",views.delete_club,name="delete_club"),
    path("delete_film /<str:pk>/",views.delete_film,name="delete_film"),
    path("delete_Showing /<str:pk>/",views.delete_showing,name="delete_Showing"),
    path("delete_screen /<str:pk>/",views.delete_screen,name="delete_screen"),

    path("view_film",views.view_film,name="view_film"),
    path("view_showing",views.view_showing,name="view_showing"),
    path("view_screen",views.view_screen,name="view_screen"), 
    path("view_club",views.view_club,name="view_club"),
    
    path("upcoming", views.upcoming, name="upcoming"),
    path("film_details/<int:id>/", views.film_details, name="film_details"),
    path("film_details/<int:id>/booking/<int:pk>/", views.booking, name="booking"),
    path("film_details/<int:id>/booking/<int:pk>/tickets", views.ticketsPurchase, name="tickets_purchase"),
    path("film_details/<int:id>/booking/<int:pk>/tickets/<int:pi>/booking_processing", views.bookingProcessing, name="booking_processing"),
    path("film_details/<int:id>/booking/<int:pk>/tickets/<int:pi>/booking_processing/booking_confirm", views.booking_confirm, name="booking_confirm"),
    path("upcoming_details/<int:id>/", views.upcoming_details, name="upcoming_details"),


]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

