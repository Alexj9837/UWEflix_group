from django.shortcuts import render
from django.shortcuts import redirect
#from UWEflix_APP.forms import RegisterClubForm
#from UWEflix_APP.models import register_club
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from UWEflix.forms import ClubForm
from .models.film import  films 
from .models.upcoming import  upcomings 
from .models.booking import Booking
from .forms import bookingForm


# Create your views here.

def home(request):
    movie = upcomings.objects.all()
    return render(request, "UWEflix/customer/home.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", "movie" : movie})

def upcoming(request):
    upcome = films.objects.all()
    return render(request,"UWEflix/customer/upcoming.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html","movie":upcome})

def film_details(request, id):
    filmdetails = upcomings.objects.get(id=id)
    return render(request, 'UWEflix/customer/film_details.html' , {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", 'd':filmdetails})


def upcoming_details(request, id):
    upcomedetails = films.objects.get(id=id)
    return render(request, "UWEflix/customer/upcoming_details.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html",'d': upcomedetails})

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

def booking(request):
    if request.method == "POST":
        form = bookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/booking_confirm")
    else:
        form = bookingForm()
        return render(request, 'UWEflix/customer/booking.html', {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html",'form': form})


def booking_confirm(request):
    ob = Booking.objects.all()
    return render(request, 'UWEflix/customer/booking_confirm.html',{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", 'ob': ob})
