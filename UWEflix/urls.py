from django.urls import path
from UWEflix import views

# urls page includes the paths we have for each webpage

urlpatterns = [
    path("", views.home, name="home"),
    path("create_club",views.create_club,name="create_club")
]