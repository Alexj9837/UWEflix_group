from django.shortcuts import render
from django.shortcuts import redirect
#from UWEflix_APP.forms import RegisterClubForm
#from UWEflix_APP.models import register_club
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from UWEflix.forms import ClubForm

# Create your views here.

# views file takes a web request and returns a web response 

# home being the home page for the all users has the login and sign up area,
# admins and managers must go through this page to sign in, thus being the first page.
# we include the base footers and headers for the page 

# "render" combines a template and returns a Https response object to render the page
def home(request):
    return render(request, "UWEflix/customer/home.html",{"footer_base":"UWEflix/footers/footer_base.html","header_content":"UWEflix/headers/header_customer.html"})

# create 
def create_club(request):
    form = ClubForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            return redirect("home")
    else:
        return render(request, "UWEflix/cinema_manager/create_club.html",{"footer_base":"UWEflix/footers/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form} )

