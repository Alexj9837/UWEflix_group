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

    path("Film_list_view",views.Film_list_view,name="Film_list_view"),
    path("Showing_list_view",views.Showing_list_view,name="Showing_list_view"),
    path("Screen_list_view",views.Screen_list_view,name="Screen_list_view"), 

]