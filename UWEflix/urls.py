from django.urls import path
from UWEflix import views


urlpatterns = [
    path("", views.home, name="home"),
]