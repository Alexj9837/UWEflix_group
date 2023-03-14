from django.urls import path
from UWEflix import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("upcoming", views.upcoming, name="upcoming"),
    path("booking", views.booking, name="booking"),
    path("booking_confirm", views.booking_confirm, name="booking_confirm"),
    path("film_details/<int:id>/", views.film_details, name="film_details"),
    path("upcoming_details/<int:id>/", views.upcoming_details, name="upcoming_details"),
    path("create_club",views.create_club,name="create_club"),
    path("update_club",views.update_club,name="update_club"),
    path("delete_club",views.delete_club,name="delete_club"),
    path("view_club",views.Club_list_view,name="view_club"),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 