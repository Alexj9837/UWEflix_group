from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_club", views.create_club,name="create_club"),
    path("shows", views.list_shows_view, name="list_shows_view")
]
