from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_club", views.create_club,name="create_club"),
    path("shows", views.get_shows, name="get_shows"),
    path("purchase_ticket", views.purchase_ticket, name="purchase_ticket"),
    path("book_show", views.book_show, name="book_show"),
    path("manage_account", views.manage_account, name="manage_account"),
]
