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
# from .forms import bookingForm
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
    shows = Show.objects.filter(film=filmdetails)
 

    showId = 0
    disable = False

    
    movieSlots = {show.show_id : Booking.objects.filter(show=show) for show in shows}
    screen = {} 

    for key , value in movieSlots.items():
        if(len(value) != 0 ):
            for i in value:
                screen.setdefault(i.show.show_id,[]).append(i.quantity_adult + i.quantity_children + i.quantity_student)

    sum_dict = {key: sum(value) for key, value in screen.items()}


    for slot in shows:
        if (slot.show_id in sum_dict):
            if Show.objects.get(show_id=slot.show_id).screen.capacity > sum_dict[slot.show_id]:
                for key , value in sum_dict.items():
                    if value == sum_dict[slot.show_id]:
                        showId = key
                break
        else:
            showId = slot.show_id
            break

    if showId == 0 :
        disable = True




    return render(request, 'UWEflix/customer/film_details.html' , {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", 'd':filmdetails,"s":show , 'id' : showId , "dis" : disable})


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

    movieSlots = {show.show_id : Booking.objects.filter(show=show) for show in allShow}
    screen = {}
    for key , value in movieSlots.items():
        if(len(value) != 0 ):
            for i in value:
                screen.setdefault(i.show.show_id,[]).append(i.quantity_adult + i.quantity_children + i.quantity_student)
        else:
            screen.setdefault(key,[]).append(0)
    
    sum_dict = {key: sum(value) for key, value in screen.items()}



    for details in allShow:
        allShowDetails.setdefault(date(details.date,"D j M"),[]).append([details.show_id ,datetime.strptime(str(details.time) , '%H:%M:%S').strftime('%I:%M %p') , not details.screen.capacity > sum_dict[details.show_id] ])


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
    bookings = Booking.objects.filter(show=show)

    bookedSeat = 0

    for seat in bookings:
        bookedSeat = bookedSeat + seat.quantity_adult + seat.quantity_children + seat.quantity_student

    availableSeat = show.screen.capacity - bookedSeat


    allShowDetails = {show.show_id: datetime.strptime(str(show.time) , '%H:%M:%S').strftime('%I:%M %p') for show in timing}


    if request.method == "POST":
        adult_num = int(request.POST.get("adult_num"))
        children_num = int(request.POST.get("children_num"))
        student_num = int(request.POST.get("student_num"))
        email = request.POST.get("email")

        booking = Booking(show=show,quantity_adult=adult_num,quantity_children=children_num,quantity_student=student_num,email=email)
        booking.save()

        return redirect(f"/film_details/{id}/booking/{pk}/tickets/{booking.pk}/booking_processing")



    
    return render(request,'UWEflix/customer/tickets_purchase.html', {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html" , "d" : show , "f" : film , "s" : allShowDetails , "time" : allShowDetails[pk] , 'pk' : pk , 'id' : id , 'a' : availableSeat } )

def bookingProcessing(request,id,pk,pi):


    film = films.objects.get(id=id)
    booking = Booking.objects.get(booking_id=pi)

    total = { "Adult" : booking.quantity_adult , "Children" : booking.quantity_children , "Student" : booking.quantity_student, "total" : booking.quantity_adult * 10 + booking.quantity_children * 8 + booking.quantity_student * 7 }

    details = {
        "id" : id,
        "pk" : pk,
        "pi" : pi,
        'film' : film.name,
        "total" : total,
        "email" : booking.email
    }

   
    if request.method == "POST":

        booking.card_number = int(request.POST.get("num"))
        booking.card_holder = request.POST.get("name")
        booking.card_expire_year  = int(request.POST.get("exp_year"))
        booking.card_expire_month  = int(request.POST.get("exp_date"))
        booking.card_cvc  = int(request.POST.get("cvc"))

        booking.save()

        return redirect(f"/film_details/{id}/booking/{pk}/tickets/{booking.pk}/booking_processing/booking_confirm")

    return render(request,'UWEflix/customer/booking_processing.html', {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html" , 'details' : details} )





def booking_confirm(request,id,pk,pi):
    return render(request, 'UWEflix/customer/booking_confirm.html',{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html",})
