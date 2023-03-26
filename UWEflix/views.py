from django.shortcuts import render
from django.shortcuts import redirect
#from UWEflix_APP.forms import RegisterClubForm
#from UWEflix_APP.models import register_club
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from UWEflix.forms import ClubForm, LoginForm, ClubRegistrationForm
from UWEflix.models import Film, upcomings

# Create your views here.

def home(request):
    movie = upcomings.objects.all()
    return render(request, "UWEflix/customer/home.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", "movie" : movie})

def upcoming(request):
    upcome = Film.objects.all()
    return render(request,"UWEflix/customer/upcoming.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html","movie":upcome})

def film_details(request, id):
    filmdetails = upcomings.objects.get(id=id)
    return render(request, 'UWEflix/customer/film_details.html' , {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", 'd':filmdetails})


def upcoming_details(request, id):
    upcomedetails = Film.objects.get(id=id)
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


def login(request):
    form = LoginForm(request.POST or None)
    
    if request.method == "POST":
        #Logic for logging in
        return redirect('home')
    else:
        return render(request, "UWEflix/cinema_booking_system/login.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_booking_system/header_cinema_booking_system.html","form":form})
    
def book_tickets(request):
    if request.method == "POST":
        return render(request, "UWEflix/cinema_booking_system/booking_success.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_booking_system/header_cinema_booking_system.html"})
    else:
        return render(request, "UWEflix/cinema_booking_system/book_show.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_booking_system/header_cinema_booking_system.html"})

def manage_account(request):
    form = ClubRegistrationForm(request.POST or None)
    if request.method == "POST":
        #update request for account
        return redirect('home')
    else:
        return render(request, "UWEflix/cinema_booking_system/manage_account.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_booking_system/header_cinema_booking_system.html","form": form})

