from django.shortcuts import render
from django.shortcuts import redirect
#from UWEflix_APP.forms import RegisterClubForm
#from UWEflix_APP.models import register_club
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    return render(request, "UWEflix/customer/home.html",{"footer_base":"UWEflix/footers/footer_base.html","header_content":"UWEflix/headers/header_customer.html"})
