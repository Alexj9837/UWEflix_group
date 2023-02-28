from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
    path('', views.home, name='home'),
    path("create_club",views.create_club,name="create_club"),
    path('purchase-ticket/', views.purchase_ticket, name='purchase_ticket'),
    path('manage-account/', views.manage_account, name='manage_account'),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name="cinema_booking_system/login.html",
        authentication_form=AuthenticationForm
        ), 
        name="login"
    ),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path('showings/', views.get_showings, name='get_shows'),
    path('showings/<int:pk>/', views.book_show, name='select_tickets'),
    path('book-tickets/', views.book_tickets, name='book_tickets'),
]