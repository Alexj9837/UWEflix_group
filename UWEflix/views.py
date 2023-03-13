from django.shortcuts import render
from django.shortcuts import redirect
#from UWEflix_APP.forms import RegisterClubForm
#from UWEflix_APP.models import register_club
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from UWEflix.forms import ClubForm
from .models.film import upfilm , films , reg
from .forms import regForm

# Create your views here.

def home(request):
    movie = upfilm.objects.all()
    return render(request, "UWEflix/customer/home.html",{"movie" : movie})

def upcoming(request):
    upcome = films.objects.all()
    return render(request,"UWEflix/customer/upcoming.html",{"movie":upcome})

def details(request, id):
    d = upfilm.objects.get(id=id)
    return render(request, 'UWEflix/customer/details.html' , {'d': d})


def updetails(request, id):
    d = films.objects.get(id=id)
    return render(request, 'UWEflix/customer/updetails.html', {'d': d})

def create_club(request):
    form = ClubForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            return redirect("home")
    else:
        return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form} )


def update_club(request, pk):
    club = ClubForm.objects.get(pk=pk)
    form = ClubForm(request.POST or None, instance=club)

    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)

            club.save()
            return redirect("View_clubs")
    else:
        return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})


def delete_club(request, pk):
    club = ClubForm.objects.get(pk=pk)

    club.delete()
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})


def Club_list_view(request):

    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def signup(request):
    if request.method == "POST":
        form = regForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/booked")
    else:
        form = regForm()
        return render(request, 'UWEflix/customer/signup.html', {'form': form})


def booked(request):
    ob = reg.objects.all()
    return render(request, 'UWEflix/customer/booked.html', {'ob': ob})
