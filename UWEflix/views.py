from django.shortcuts import render
from django.shortcuts import redirect
#from UWEflix_APP.forms import RegisterClubForm
#from UWEflix_APP.models import register_club
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from UWEflix.forms import ClubForm, TicketPurchaseForm

# Create your views here.

def home(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html"})


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

def get_shows(request):
    
    if request.method == "POST":
        #filtered shows
        return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_booking_system/show.html"})
    else:
        return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_booking_system/header_cinema_booking_system.html"})

def purchase_ticket(request):
    form = TicketPurchaseForm(request.POST or None)

    if request.method == "POST":
        if (form.is_valid()):
            ticket = form.save(commit=False)
            ticket.save()
            return redirect("home")
    else:
        return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_booking_system/purchase_ticket.html"})
    

def book_show(request):
    form = TicketPurchaseForm(request.POST)

    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.save()
        return redirect("home")

def manage_account(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_booking_system/header_cinema_booking_system.html"})