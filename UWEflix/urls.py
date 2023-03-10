from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
    path("", views.home, name="home"),
    path("create_club",views.create_club,name="create_club")
]