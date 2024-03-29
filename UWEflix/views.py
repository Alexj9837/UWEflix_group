from django.shortcuts import render
from django.shortcuts import redirect
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
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.http.response import JsonResponse
from django.contrib import messages


# Create your views here.

def get_header(request):
    user = request.user
    if not request.user.is_anonymous:
        if user.role == 'Cinema manager':
            header_content = "UWEflix/cinema_manager/header_cinema_manager.html"
        elif user.role == 'account manager':
            header_content = "UWEflix/account_manager/header_account_manager.html"
        elif user.role == 'club rep':
            header_content = "UWEflix/cinema_booking_system/header_cinema_booking_system.html"
        elif user.role == 'student':
            header_content = "UWEflix/base/header_base.html"
    else:
        header_content = "UWEflix/base/header_base.html"
    return header_content

def login_view(request):
     if request.method == 'POST':
        try:
            
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return HttpResponse("User not valid")
                # Handle guest user
                #request.session['guest'] = True
                #return redirect('home')
        except:
        
            request.session['guest'] = True
            return redirect('home')
    
     else:
        form = LoginForm()
        return render(request, "UWEflix/base/login.html", {"form": form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password1')
            role = 'student'

            user = Custom_user.objects.create_user(username=username, email=email, password=password,
                                            first_name=first_name, last_name=last_name, role=role)
            user.save()
            # Log the user in.
            #login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'UWEflix/base/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("home")


def home(request):
    movie = Film.objects.all()
    return render(request, "UWEflix/customer/home.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html", "movie" : movie})


def upcoming(request):
    upcome = upcomings.objects.all()
    return render(request, "UWEflix/customer/upcoming.html", {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "movie": upcome})


def film_details(request, id):
    filmdetails = Film.objects.get(id=id)
    show = Show.objects.filter(film=filmdetails)[0].show_id
    shows = Show.objects.filter(film=filmdetails)

    showId = 0
    disable = False

    movieSlots = {show.show_id: Booking.objects.filter(
        show=show) for show in shows}
    screen = {}

    for key, value in movieSlots.items():
        if (len(value) != 0):
            for i in value:
                screen.setdefault(i.show.show_id, []).append(
                    i.quantity_adult + i.quantity_children + i.quantity_student)

    sum_dict = {key: sum(value) for key, value in screen.items()}

    for slot in shows:
        if (slot.show_id in sum_dict):
            if Show.objects.get(show_id=slot.show_id).screen.capacity > sum_dict[slot.show_id]:
                for key, value in sum_dict.items():
                    if value == sum_dict[slot.show_id]:
                        showId = key
                break
        else:
            showId = slot.show_id
            break

    if showId == 0:
        disable = True

    return render(request, 'UWEflix/customer/film_details.html', {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), 'd': filmdetails, "s": show, 'id': showId, "dis": disable})


def upcoming_details(request, id):
    upcomedetails = upcomings.objects.get(id=id)
    return render(request, "UWEflix/customer/upcoming_details.html", {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), 'd': upcomedetails})

# #####################################################
# ######### CRUD ######################################
# #####################################################


@login_required(login_url='/login')
def CRUD_create(request, form_class, template_name, redirect_url):
    form = form_class(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(redirect_url)

    context = {
        "form": form,
        "footer_content": "UWEflix/base/footer_base.html",
        "header_content": get_header(request),
    }
    return render(request, template_name, context)


@login_required(login_url='/login')
def CRUD_view(request, model_class, template_name):
    user = request.user
    if user.role == 'Cinema manager' or user.role == 'account manager':
        objects = model_class.objects.all()
        context = {
            "objects": objects,
            "footer_content": "UWEflix/base/footer_base.html",
            "header_content": get_header(request),
        }
        return render(request, template_name, context)
    else:
        return redirect("home")


@login_required(login_url='/login')
def CRUD_delete(request, pk, model_class, redirect_url):
    if request.method == "POST":
        instance = model_class.objects.get(pk=pk)
        if isinstance(instance, Screen) or isinstance(instance, Film):
            has_showing = Show.objects.filter(screen=instance).exists() if isinstance(instance, Screen) else Show.objects.filter(film=instance).exists()
            
            if has_showing:
                messages.error(request, "Cannot delete the screen or film as it is associated with a showing.")
                return redirect(redirect_url)

        instance.delete()
        return redirect(redirect_url)

    context = {
        "footer_content": "UWEflix/base/footer_base.html",
        "header_content": get_header(request),
    }
    return render(request, "UWEflix/base/confirm_delete.html", context)

# #####################################################
# ######### CLUBS #####################################
# #####################################################


@login_required(login_url='/login')
def create_club(request):
    return CRUD_create(request, ClubForm, "UWEflix/cinema_manager/create.html", "view_club")


@login_required(login_url='/login')
def view_club(request):
    user = request.user
    if user.role == 'Cinema manager':
        return CRUD_view(request, Club, "UWEflix/cinema_manager/clubs/view_club.html")
    else:
        return redirect("home")


@login_required(login_url='/login')
def update_club(request, pk):
    club = Club.objects.get(pk=pk)
    form = ClubForm(request.POST, instance=club)
    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            return redirect("view_club")

    return render(request, 'UWEflix/cinema_manager/clubs/update_club.html', {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "form": form, "club": club})


@login_required(login_url='/login')
def delete_club(request, pk):
    return CRUD_delete(request, pk, Club, "view_club")

# #####################################################
# ######### FILMS #####################################
# #####################################################


@login_required(login_url='/login')
def create_film(request):
    return CRUD_create(request, filmForm, "UWEflix/cinema_manager/create.html", "view_film")


@login_required(login_url='/login')
def view_film(request):
    user = request.user
    if user.role == 'Cinema manager':
        return CRUD_view(request, Film, "UWEflix/cinema_manager/films/view_film.html")
    else:
        return redirect("home")

@login_required(login_url='/login')
def update_film(request, pk):
    film = Film.objects.get(pk=pk)
    form = filmForm(request.POST, instance=film)
    if request.method == "POST":
        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            return redirect("view_film")
    return render(request, "UWEflix/cinema_manager/films/update_film.html", {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "form": form, "film": film})


@login_required(login_url='/login')
def delete_film(request, pk):
    return CRUD_delete(request, pk, Film, "view_film")

# #####################################################
# ######### SCREENS ###################################
# #####################################################


@login_required(login_url='/login')
def create_screen(request):
    return CRUD_create(request, screenForm, "UWEflix/cinema_manager/create.html", "view_screen")


@login_required(login_url='/login')
def view_screen(request):
    user = request.user
    if user.role == 'Cinema manager':
        return CRUD_view(request, Screen, "UWEflix/cinema_manager/screens/view_screen.html")
    else:
        return redirect("home")


@login_required(login_url='/login')
def update_screen(request, pk):
    screen = Screen.objects.get(pk=pk)
    form = screenForm(request.POST, instance=screen)
    if request.method == "POST":
        if form.is_valid():
            screen = form.save(commit=False)
            screen.save()
            return redirect("view_screen")
    return render(request, "UWEflix/cinema_manager/screens/update_screen.html", {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "form": form, "screen": screen})


@login_required(login_url='/login')
def delete_screen(request, pk):
    return CRUD_delete(request, pk, Screen, "view_screen")

# #####################################################
# ######### SHOWINGS ##################################
# #####################################################


@login_required(login_url='/login')
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
    return render(request, "UWEflix/cinema_manager/showings/create_showing.html", {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "form": form, "films": films, "screens": screens})


@login_required(login_url='/login')
def view_showing(request):
    user = request.user
    if user.role == 'Cinema manager':
        return CRUD_view(request, Show, "UWEflix/cinema_manager/showings/view_showing.html")
    else:
        return redirect("home")


@login_required(login_url='/login')
def update_showing(request, pk):
    show = Show.objects.get(pk=pk)
    form = showForm(request.POST, instance=show)
    if request.method == "POST":
        if form.is_valid():
            show = form.save(commit=False)
            show.save()
            return redirect("view_showing")
    return render(request, "UWEflix/cinema_manager/showings/update_showing.html", {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "form": form, "show": show})


@login_required(login_url='/login')
def delete_showing(request, pk):
    return CRUD_delete(request, pk, Show, "view_showing")

# #####################################################
# ######### Bookings ##################################
# #####################################################


def book_tickets(request, pk):
    show = Show.objects.get(show_id=pk)
    current_user = request.user
    club_rep = ClubRepresentative.objects.get(user=current_user.id)

    if request.method == "POST":

        bookings = Booking.objects.filter(show=show)

        bookedSeat = 0

        for seat in bookings:
            bookedSeat = bookedSeat + seat.quantity_adult + \
                seat.quantity_children + seat.quantity_student

        availableSeat = show.screen.capacity - bookedSeat
        number_of_ticket = int(request.POST.get("number_of_ticket"))

        if number_of_ticket <= availableSeat:
            booking = Booking({
                'show': show,
                'quantity_student': number_of_ticket,
            })
            booking.save()

        return redirect('home')
    else:
        context = {
            "footer_content": "UWEflix/base/footer_base.html",
            "header_content": get_header(request),
            "show": show,
            "discount": club_rep.club.discount,
        }
        return render(request, "UWEflix/cinema_booking_system/book_show.html", context)


#@login_required(login_url='/login')
def booking(request, id, pk):
    # Check if user is logged in as a guest
    #is_guest = request.session.get('guest', False)
    #if not request.session.get('guest'):
    if not request.user.is_authenticated and not request.session.get('guest'):
        return redirect('login')
    
 
    film = Film.objects.get(id=id)
    allShow = Show.objects.filter(film=film)
    show = Show.objects.get(show_id=pk)
    allShowDetails = {}

    movieSlots = {show.show_id: Booking.objects.filter(
        show=show) for show in allShow}
    screen = {}
    for key, value in movieSlots.items():
        if (len(value) != 0):
            for i in value:
                screen.setdefault(i.show.show_id, []).append(
                    i.quantity_adult + i.quantity_children + i.quantity_student)
        else:
            screen.setdefault(key, []).append(0)

    sum_dict = {key: sum(value) for key, value in screen.items()}

    for details in allShow:
        allShowDetails.setdefault(date(details.date, "D j M"), []).append([details.show_id, datetime.strptime(str(
            details.time), '%H:%M:%S').strftime('%I:%M %p'), not details.screen.capacity > sum_dict[details.show_id]])

    details = {
        'id' : id,
        'show': show,
        'film': film.name,
        'currentWeekName': date(show.date, "D"),
        'currentDateMonthName': date(show.date, "j M"),
        "allShowDetails": allShowDetails,
    }

    return render(request, 'UWEflix/customer/booking.html', {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), 'details': details})



#@login_required(login_url='/login')
def ticketsPurchase(request, id, pk):
    
    role = ''
    if not request.user.is_authenticated and not request.session.get('guest'):
        return redirect('login')

    if request.user.is_authenticated:
        role = request.user.role
 
    show = Show.objects.get(show_id=pk)
    film = Film.objects.get(id=id)
    timing = Show.objects.filter(film=film)
    bookings = Booking.objects.filter(show=show)

    bookedSeat = 0

    for seat in bookings:
        bookedSeat = bookedSeat + seat.quantity_adult + seat.quantity_children + seat.quantity_student

    availableSeat = show.screen.capacity - bookedSeat

    allShowDetails = {show.show_id: datetime.strptime(
        str(show.time), '%H:%M:%S').strftime('%I:%M %p') for show in timing}

    if request.method == "POST":
        adult_num = int(request.POST.get("adult_num"))
        children_num = int(request.POST.get("children_num"))
        student_num = int(request.POST.get("student_num"))
        email = request.POST.get("email")

        booking = Booking(show=show, quantity_adult=adult_num,
                          quantity_children=children_num, quantity_student=student_num, email=email)
        booking.save()

        return redirect(f"/film_details/{id}/booking/{pk}/tickets/{booking.pk}/booking_processing")

    return render(request, 'UWEflix/customer/tickets_purchase.html', {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "d": show, "f": film, "s": allShowDetails, "time": allShowDetails[pk], 'pk': pk, 'id': id, 'a': availableSeat, 'role':role})


#@login_required(login_url='/login')
def bookingProcessing(request, id, pk, pi):
    if not request.user.is_authenticated and not request.session.get('guest'):
        return redirect('login')
    
        
    
    film = Film.objects.get(id=id)
    booking = Booking.objects.get(booking_id=pi)

    total = {"Adult": booking.quantity_adult, "Children": booking.quantity_children, "Student": booking.quantity_student,
             "total": booking.quantity_adult * 10 + booking.quantity_children * 8 + booking.quantity_student * 7}

    details = {
        "id": id,
        "pk": pk,
        "pi": pi,
        'film': film.name,
        "total": total,
        "email": booking.email
    }

    if request.method == "POST":

        # booking.card_number = int(request.POST.get("num"))
        # booking.card_holder = request.POST.get("name")
        # booking.card_expire_year = int(request.POST.get("exp_year"))
        # booking.card_expire_month = int(request.POST.get("exp_date"))
        # booking.card_cvc = int(request.POST.get("cvc"))

        # booking.save()

        # return redirect(f"/film_details/{id}/booking/{pk}/tickets/{booking.pk}/booking_processing/booking_payment/")
        # return redirect(f"/film_details/{id}/booking/{pk}/tickets/{booking.pk}/booking_processing/booking_confirm")

    value = {'sessionId': ""}

    if request.method == 'POST':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        print(f'{domain_url}media/{film.image}')
        try:
            checkout_session = stripe.checkout.Session.create(
                # client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + f"film_details/{id}/booking/{pk}/tickets/{booking.pk}/booking_processing/booking_confirm",
                cancel_url=domain_url,
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                    'price_data': {
                    'currency': 'gbp',
                    'unit_amount': total['total'] * 100,
                    'product_data': {
                        'name': film.name,
                        'description': film.type,
                    },
                    },
                    #'quantity': total['Adult'] + total['Children'] + total['Student'],
                    'quantity': 1,
                }],
            )
            # return JsonResponse({'sessionId': checkout_session['id']})
            value = {'sessionId': checkout_session['id']}
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return render(request, 'UWEflix/customer/booking_processing.html', {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), 'details': details , 'value' : value})


def booking_confirm(request, id, pk, pi):
    return redirect(f"/film_details/{id}/booking/{pk}/tickets/{booking.pk}/booking_processing/booking_confirm")


@login_required(login_url='/login')
def manage_account(request):
    form = ClubRegistrationForm(request.POST or None)
    if request.method == "POST":
        # update request for account
        return redirect('home')
    else:
        return render(request, "UWEflix/cinema_booking_system/manage_account.html", {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "form": form})


#@login_required(login_url='/login')
def booking_confirm(request, id, pk, pi):
    return render(request, 'UWEflix/customer/booking_confirm.html', {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), })


# #####################################################
# ######### Account Manager ##################################
# #####################################################

#Account Manager Home Page
@login_required(login_url='/login')
def account_home(request):
    users = Custom_user.objects.all()
    reps = Representitive.objects.all()
    return render(request, "UWEflix/account_manager/account_home.html", {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "users": users, "reps": reps})

@login_required(login_url='/login')
def create_user(request):
    return CRUD_create(request, UserForm, "UWEflix/account_manager/create.html", "view_user")

#CRUD for User
@login_required(login_url='/login')
def createUser(request):
    userForm = UserForm(request.POST or None)

    context = {
        "userForm": userForm
    }

    if request.method != 'POST':
        return render(request, "UWEflix/account_manager/user/create_user.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/account_manager/header_account_manager.html","form": context} )

    if userForm.is_valid():
        user = userForm.save(commit=False)
        user.encryptPassword(userForm.cleaned_data['password'])
        user.save()
        return redirect("account_home")
    else:
        print("Form is not valid")
        return render(request, "UWEflix/account_manager/user/create_user.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/account_manager/header_account_manager.html","form": context} )

@login_required(login_url='/login')
def view_user(request):
    user = request.user
    if user.role == 'account manager':
        return CRUD_view(request, Custom_user, "UWEflix/account_manager/user/view_user.html")
    else:
        return redirect("account_home")

@login_required(login_url='/login')
def update_user(request, pk):
    user = Custom_user.objects.get(pk=pk)
    form = UserForm(request.POST, instance=user)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("account_home")
    return render(request, 'UWEflix/account_manager/user/update_user.html', {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "form": form, "user": user})

@login_required(login_url='/login')
def delete_user(request, pk):
    return CRUD_delete(request, pk, Custom_user, "account_home")

#CRUD for Rep
@login_required(login_url='/login')
def createRep(request):
    repForm = RepForm(request.POST or None)

    context = {
        "repForm": repForm
    }

    if request.method != 'POST':
        return render(request, "UWEflix/account_manager/rep/create_rep.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/account_manager/header_account_manager.html","form": context} )

    if repForm.is_valid():
        rep = repForm.save(commit=False)
        rep.encryptPassword(repForm.cleaned_data['password'])
        repForm.save()
        return redirect("account_home")
    else:
        print("Form is not valid")
        return render(request, "UWEflix/account_manager/rep/create_rep.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/account_manager/header_account_manager.html","form": context} )

@login_required(login_url='/login')    
def view_rep(request):
    return CRUD_view(request, Representitive, "UWEflix/account_manager/rep/view_rep.html")

@login_required(login_url='/login')
def update_rep(request, pk):
    rep = Representitive.objects.get(pk=pk)
    form = RepForm(request.POST, instance=rep)
    if request.method == "POST":
        if form.is_valid():
            rep = form.save(commit=False)
            rep.save()
            return redirect("account_home")

    return render(request, 'UWEflix/account_manager/rep/update_rep.html', {"footer_content": "UWEflix/base/footer_base.html", "header_content": get_header(request), "form": form, "rep": rep})

@login_required(login_url='/login')
def delete_rep(request, pk):
    return CRUD_delete(request, pk, Representitive, "account_home")