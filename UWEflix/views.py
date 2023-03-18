from django.shortcuts import render
from django.shortcuts import redirect
#from UWEflix_APP.forms import RegisterClubForm
#from UWEflix_APP.models import register_club
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from UWEflix.forms import *
from UWEflix.models import *

# Create your views here.

def home(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/base/header_base.html"})

#####################################################
######### CLUBS #####################################
#####################################################


def create_club(request):
    form = ClubForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            return redirect("view_club")
    else:
            form = ClubForm()
    return render(request, "UWEflix/cinema_manager/clubs/create_club.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form} )

# def update_club(request):

#     if request.method == "POST":
#         pk = request.POST.get('pk')
#         club = Club.objects.get(pk=pk)
#         form = ClubForm(request.POST or None, instance=club)
#         if form.is_valid():
#             club = form.save(commit=False)

#             club.save()
#             return redirect("view_club")
#     else:
#         return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def update_club(request):
    pk = request.POST.get('pk')
    club = Club.objects.get(pk=pk)

    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)

        if form.is_valid():
            form.save()
            return redirect("view_club")
        
    else:
        form = ClubForm(instance=club)    
        return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form})


def delete_club(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        club = Club.objects.get(pk=pk)
        club.delete()
        return redirect('view_club')
    else:
        return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def view_club(request):
    clubs = Club.objects.all()
    print(clubs)  # add this line to check if clubs is not empty
    return render(request, "UWEflix/cinema_manager/clubs/view_club.html", {"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html", "view_club_data": clubs})

#####################################################
######### FILMS/SHOWINGS/SCREENS ####################
#####################################################

def create_showing(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def create_film(request):
    form = filmForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            return redirect("view_film")
    else:
        return render(request, "UWEflix/cinema_manager/films/create_film.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def create_screen(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def update_showing(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def update_film(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def update_screen(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def delete_showing(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def delete_film(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def delete_screen(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def view_film(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def view_screen(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})

def view_showing(request):
    return render(request, "UWEflix/base/base.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html"})
