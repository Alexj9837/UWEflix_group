from django.urls import path
from UWEflix import views


urlpatterns = [

    path("", views.home, name="home"),

#####################################################
######### FILMS/SHOWINGS/SCREENS/CLUBS ##############
#####################################################

    path("create_club",views.create_club,name="create_club"),
    path("Create_film",views.Create_film,name="Create_film"),
    path("Create_showing",views.Create_showing,name="Create_showing"),
    path("Create_screen",views.Create_screen,name="Create_screen"),
    
    path("update_club",views.update_club,name="update_club"),
    path("Update_film",views.Update_film,name="Update_film"),
    path("Update_showing",views.Update_showing,name="Update_showing"),
    path("Update_screen",views.Update_screen,name="Update_screen"),

    path("delete_club",views.delete_club,name="delete_club"),
    path("Delete_film",views.Delete_film,name="Delete_film"),
    path("Delete_Showing",views.Delete_showing,name="Delete_Showing"),
    path("Delete_screen",views.Delete_screen,name="Delete_screen"),

    path("view_film",views.view_film,name="view_film"),
    path("view_shooing",views.view_showing,name="view_showing"),
    path("view_screen",views.view_screen,name="view_screen"), 
    path("view_club",views.view_club,name="view_club"),

]