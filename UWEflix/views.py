from django.shortcuts import render
from django.shortcuts import redirect
#from UWEflix_APP.forms import RegisterClubForm
#from UWEflix_APP.models import register_club
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request, "UWEflix/home.html")