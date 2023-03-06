from django.urls import path
from UWEflix import views


urlpatterns = [
    path("", views.home, name="home"),
    path("create_club",views.create_club,name="create_club"),
    path("update_club",views.update_club,name="update_club"),
    path("delete_club",views.delete_club,name="delete_club"),
]