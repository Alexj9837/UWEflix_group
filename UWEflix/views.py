from django.shortcuts import render
from django.shortcuts import redirect
#from UWEflix_APP.forms import RegisterClubForm
#from UWEflix_APP.models import register_club
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from UWEflix.forms import *
from UWEflix.models import *
from .models.upcoming import upcomings
from .models.booking import Booking
# from .forms import bookingForm
from django.template.defaultfilters import date
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("User not valid")
    else:
        form = LoginForm()
        return render(request, "UWEflix/base/login.html", {"form": form})
    





def home(request):
    movie = Film.objects.all()
    return render(request, "UWEflix/customer/home.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", "movie" : movie})

def upcoming(request):
    upcome = upcomings.objects.all()
    return render(request,"UWEflix/customer/upcoming.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html","movie":upcome})

def film_details(request, id):
    filmdetails = Film.objects.get(id=id)
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

# #####################################################
# ######### CRUD ######################################
# #####################################################

def CRUD_create(request, form_class, template_name, redirect_url):
    form = form_class(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(redirect_url)

    context = {
        "form": form,
        "footer_content": "UWEflix/base/footer_base.html",
        "header_content": "UWEflix/cinema_manager/header_cinema_manager.html",
    }
    return render(request, template_name, context)

def CRUD_view(request, model_class, template_name):
    objects = model_class.objects.all()
    context = {
        "objects": objects,
        "footer_content": "UWEflix/base/footer_base.html",
        "header_content": "UWEflix/cinema_manager/header_cinema_manager.html",
    }
    return render(request, template_name, context)

def CRUD_delete(request, pk, model_class, redirect_url):
    if request.method == "POST":
            instance = model_class.objects.get(pk=pk)
            instance.delete()
            return redirect(redirect_url)

    context = {
        "footer_content": "UWEflix/base/footer_base.html",
        "header_content": "UWEflix/cinema_manager/header_cinema_manager.html",
    }
    return render(request, "UWEflix/base/confirm_delete.html", context)

# #####################################################
# ######### CLUBS #####################################
# #####################################################

def create_club(request):
    return CRUD_create(request, ClubForm, "UWEflix/cinema_manager/create.html", "view_club")

def view_club(request):
    return CRUD_view(request, Club, "UWEflix/cinema_manager/clubs/view_club.html")

def update_club(request, pk):
    club = Club.objects.get(pk=pk)
    form = ClubForm(request.POST, instance=club)
    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            return redirect("view_club")

    return render(request, 'UWEflix/cinema_manager/clubs/update_club.html',{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html", "form": form, "club": club})

def delete_club(request, pk):
    return CRUD_delete(request, pk, Club, "view_club")

# #####################################################
# ######### FILMS #####################################
# #####################################################

def create_film(request):
    return CRUD_create(request, filmForm, "UWEflix/cinema_manager/create.html", "view_film")

def view_film(request):
    return CRUD_view(request, Film, "UWEflix/cinema_manager/films/view_film.html")

def update_film(request, pk):
    film = Film.objects.get(pk=pk)
    form = filmForm(request.POST, instance=film)
    if request.method == "POST":
        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            return redirect("view_film")
    return render(request, "UWEflix/cinema_manager/films/update_film.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form, "film": film})

def delete_film(request, pk):
    return CRUD_delete(request, pk, Film, "view_film")

# #####################################################
# ######### SCREENS ###################################
# #####################################################

def create_screen(request):
    return CRUD_create(request, screenForm, "UWEflix/cinema_manager/create.html", "view_screen")

def view_screen(request):
    return CRUD_view(request, Screen, "UWEflix/cinema_manager/screens/view_screen.html")

def update_screen(request, pk):
    screen = Screen.objects.get(pk=pk)
    form = screenForm(request.POST, instance=screen)
    if request.method == "POST":
        if form.is_valid():
            screen = form.save(commit=False)
            screen.save()
            return redirect("view_screen")
    return render(request, "UWEflix/cinema_manager/screens/update_screen.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form, "screen": screen})

def delete_screen(request, pk):
    return CRUD_delete(request, pk, Screen, "view_screen")

# #####################################################
# ######### SHOWINGS ##################################
# #####################################################

def create_showing(request):
    form = showForm(request.POST or None)
    films = Film.objects.all() 
    screens = Screen.objects.all()
    if request.method == "POST":
        if form.is_valid():
            show = Show.save(commit=False)
            show.save()
            return redirect("view_screen")
    else:
            form = showForm()
    return render(request, "UWEflix/cinema_manager/showings/create_showing.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form":form, "films" :films, "screens":screens})

def view_showing(request):
    return CRUD_view(request, Show, "UWEflix/cinema_manager/showings/view_showing.html")

def update_showing(request,pk):
    show = Show.objects.get(pk=pk)
    form = showForm(request.POST, instance=show)
    if request.method == "POST":
        if form.is_valid():
            show = form.save(commit=False)
            show.save()
            return redirect("view_showing")
    return render(request, "UWEflix/cinema_manager/showings/update_showing.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form, "show": show})

def delete_showing(request, pk):
    return CRUD_delete(request, pk, Show, "view_showing")

# #####################################################
# ######### Bookings ##################################
# #####################################################

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
def booking(request,id,pk):


    film = Film.objects.get(id=id)
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
    film = Film.objects.get(id=id)
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


    film = Film.objects.get(id=id)
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




def manage_account(request):
    form = ClubRegistrationForm(request.POST or None)
    if request.method == "POST":
        #update request for account
        return redirect('home')
    else:
        return render(request, "UWEflix/cinema_booking_system/manage_account.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_booking_system/header_cinema_booking_system.html","form": form})

def booking_confirm(request,id,pk,pi):
    return render(request, 'UWEflix/customer/booking_confirm.html',{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html",})

#############################################################
## dosent work / unsused ####################################
#############################################################

# def update_showing(request, pk):
#     return CRUD_update(request, pk, Show, showForm, "UWEflix/cinema_manager/showings/update_showing.html", "view_showing")

# def update_screen(request, pk):
#     return CRUD_update(request, pk, Screen,screenForm, "UWEflix/cinema_manager/update.html", "view_screen")

# def update_film(request, pk):
#     return CRUD_update(request, pk, Film, filmForm, "UWEflix/cinema_manager/films/update_film.html", "view_film")

# def update_club(request, pk):
#     return CRUD_update(request, pk, Club, ClubForm, "UWEflix/cinema_manager/clubs/update_club.html", "view_club")

# def update_screen(request, pk):
#     return CRUD_update(request, pk, Screen,screenForm, "UWEflix/cinema_manager/update.html", "view_screen")

# def CRUD_update(request, pk, model_class, form_class, template_name, redirect_url):
#     dd = model_class.objects.get(pk=pk)
#     form = form_class(request.POST or None, instance=dd)

#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect(redirect_url)

#     context = {
#         "form": form,
#         "footer_content": "UWEflix/base/footer_base.html",
#         "header_content": "UWEflix/cinema_manager/header_cinema_manager.html",
#         "instance": dd,
#     }
#     return render(request, template_name, context)

# def delete_showing(request,pk):
#     if request.method == 'POST':
#         show = Show.objects.get(pk=pk)
#         show.delete()
#         return redirect('view_screen')
#     else:
#         return render(request, "UWEflix/cinema_manager/showings/view_showing.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

# def view_showing(request):
#     showing = Show.objects.all()
#     print("show")
#     return render(request, "UWEflix/cinema_manager/showings/view_showing.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","showings": showing})

# def create_screen(request):
#     form = screenForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             screen = form.save(commit=False)
#             screen.save()
#             return redirect("view_screen")
#     else:
#             form = screenForm()
#     return render(request, "UWEflix/cinema_manager/screens/create_screen.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form} )

# def delete_screen(request, pk):
#     if request.method == 'POST':
#         screen = Screen.objects.get(pk=pk)
#         screen.delete()
#         return redirect('view_screen')
#     else:
#         return render(request, "UWEflix/cinema_manager/screens/view_screens.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})
    
# def view_screen(request):
#     screen = Screen.objects.all()
#     return render(request, "UWEflix/cinema_manager/screens/view_screen.html", {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html", "view_screen_data": screen})


# def create_club(request):
#     form = ClubForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             club = form.save(commit=False)
#             club.save()
#             return redirect("view_club")
#     else:
#             form = ClubForm()
#     return render(request, "UWEflix/cinema_manager/clubs/create_club.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form} )

# def delete_club(request, pk):
#     if request.method == 'POST':
#         club = Club.objects.get(pk=pk)
#         club.delete()
#         return redirect('view_club')
#     else:
#         return render(request, "UWEflix/cinema_manager/clubs/view_club.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

# def view_club(request):
#     clubs = Club.objects.all()
#     print(clubs) 
#     return render(request, "UWEflix/cinema_manager/clubs/view_club.html", {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html", "view_club_data": clubs})

# def create_film(request):
#     form = filmForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             film = form.save(commit=False)
#             film.save()
#             return redirect("view_film")
#     else:
#             form = filmForm()
#     return render(request, "UWEflix/cinema_manager/films/create_film.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form} )

# def delete_film(request, pk):
#     if request.method == 'POST':
#         film = Film.objects.get(pk=pk)
#         film.delete()
#         return redirect('view_film')
#     else:
#         return render(request, "UWEflix/cinema_manager/films/view_film.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

# def view_film(request):
#     films = Film.objects.all()
#     return render(request, "UWEflix/cinema_manager/films/view_film.html", {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html", "view_film_data": films})

