from django.urls import path
from UWEflix import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
     path("upcoming", views.upcoming, name="upcoming"),
    path("signup", views.signup, name="signup"),
    path("booked", views.booked, name="booked"),
    path("details/<int:id>/", views.details, name="details"),
    path("updetails/<int:id>/", views.updetails, name="updetails"),
    path("create_club",views.create_club,name="create_club"),
    path("update_club",views.update_club,name="update_club"),
    path("delete_club",views.delete_club,name="delete_club"),
    path("view_club",views.Club_list_view,name="view_club"),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 