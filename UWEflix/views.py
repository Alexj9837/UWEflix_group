from django.shortcuts import render
from django.shortcuts import redirect
#from UWEflix_APP.forms import RegisterClubForm
#from UWEflix_APP.models import register_club
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from UWEflix.forms import ClubForm
from .models.film import  films 
from .models.show import  Show 
from .models.upcoming import  upcomings 
from .models.booking import Booking
from .forms import bookingForm
from django.template.defaultfilters import date
from datetime import datetime


# Create your views here.

def home(request):
    movie = films.objects.all()
    return render(request, "UWEflix/customer/home.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", "movie" : movie})

def upcoming(request):
    upcome = upcomings.objects.all()
    return render(request,"UWEflix/customer/upcoming.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html","movie":upcome})

def film_details(request, id):
    filmdetails = films.objects.get(id=id)
    show = Show.objects.filter(film=filmdetails)[0].show_id
    return render(request, 'UWEflix/customer/film_details.html' , {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", 'd':filmdetails,"s":show})


def upcoming_details(request, id):
    upcomedetails = upcomings.objects.get(id=id)
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


def booking(request,id,pk):


    film = films.objects.get(id=id)
    allShow = Show.objects.filter(film=film)
    show = Show.objects.get(show_id=pk)
    allShowDetails = {}

    for details in allShow:
        allShowDetails.setdefault(date(details.date,"D j M"),[]).append([details.show_id ,datetime.strptime(str(details.time) , '%H:%M:%S').strftime('%I:%M %p')])

    details = {
        'show' : show,
        'film' : film.name,
        'currentWeekName' : date(show.date,"D"),
        'currentDateMonthName' : date(show.date,"j M"),
        "allShowDetails" : allShowDetails,
    }


    return render(request,'UWEflix/customer/booking.html', {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", 'details' : details} )


def ticketsPurchase(request,id,pk):

    show = Show.objects.get(show_id=pk)
    film = films.objects.get(id=id)
    timing = Show.objects.filter(film=film)

    # print(show.screen.capacity)


    allShowDetails = {show.show_id: datetime.strptime(str(show.time) , '%H:%M:%S').strftime('%I:%M %p') for show in timing}

    if request.method == "POST":
        # print(request.POST.get("name"))
        pass
    
    return render(request,'UWEflix/customer/tickets_purchase.html', {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html" , "d" : show , "f" : film , "s" : allShowDetails , "time" : allShowDetails[pk] , 'pk' : pk , 'id' : id } )



def t(request):

    return render(request,'UWEflix/customer/booking_processing.html', {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html"} )

