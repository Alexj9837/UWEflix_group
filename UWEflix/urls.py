from django.urls import path
from UWEflix import views


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
    path("update_film",views.update_film,name="update_film"),
    path("update_showing",views.update_showing,name="update_showing"),
    path("update_screen",views.update_screen,name="update_screen"),

    path("delete_club /<str:pk>",views.delete_club,name="delete_club"),
    path("delete_film",views.delete_film,name="delete_film"),
    path("delete_Showing",views.delete_showing,name="delete_Showing"),
    path("delete_screen",views.delete_screen,name="delete_screen"),

    path("view_film",views.view_film,name="view_film"),
    path("view_shooing",views.view_showing,name="view_showing"),
    path("view_screen",views.view_screen,name="view_screen"), 
    path("view_club",views.view_club,name="view_club"),

]