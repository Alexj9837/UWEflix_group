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

# #####################################################
# ######### CLUBS #####################################
# #####################################################

def update_club(request, pk):
    club = Club.objects.get(pk=pk)
    form = ClubForm(request.POST, instance=club)
    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            return redirect("view_club")

    return render(request, 'UWEflix/cinema_manager/clubs/update_club.html',{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html", "form": form, "club": club})

# #####################################################
# ######### FILMS #####################################
# #####################################################

def update_film(request, pk):
    film = Film.objects.get(pk=pk)
    form = filmForm(request.POST, instance=film)
    if request.method == "POST":
        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            return redirect("view_film")
    return render(request, "UWEflix/cinema_manager/films/update_film.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form, "film": film})

# #####################################################
# ######### SCREENS ###################################
# #####################################################

def update_screen(request, pk):
    screen = Screen.objects.get(pk=pk)
    form = screenForm(request.POST, instance=screen)
    if request.method == "POST":
        if form.is_valid():
            screen = form.save(commit=False)
            screen.save()
            return redirect("view_screen")
    return render(request, "UWEflix/cinema_manager/screens/update_screen.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form, "screen": screen})

# #####################################################
# ######### SHOWINGS ##################################
# #####################################################

def update_showing(request,pk):
    show = Show.objects.get(pk=pk)
    form = showForm(request.POST, instance=show)
    if request.method == "POST":
        if form.is_valid():
            show = form.save(commit=False)
            show.save()
            return redirect("view_showing")
    return render(request, "UWEflix/cinema_manager/showings/update_showing.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form": form, "show": show})

# #####################################################
# ######### TESTING ###################################
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

def create_club(request):
    return CRUD_create(request, ClubForm, "UWEflix/cinema_manager/create.html", "view_club")

def view_club(request):
    return CRUD_view(request, Club, "UWEflix/cinema_manager/clubs/view_club.html")

def delete_club(request, pk):
    return CRUD_delete(request, pk, Club, "view_club")

def create_film(request):
    return CRUD_create(request, filmForm, "UWEflix/cinema_manager/create.html", "view_film")

def view_film(request):
    return CRUD_view(request, Film, "UWEflix/cinema_manager/films/view_film.html")

def delete_film(request, pk):
    return CRUD_delete(request, pk, Film, "view_film")

def create_screen(request):
    return CRUD_create(request, screenForm, "UWEflix/cinema_manager/create.html", "view_screen")

def view_screen(request):
    return CRUD_view(request, Screen, "UWEflix/cinema_manager/screens/view_screen.html")

def delete_screen(request, pk):
    return CRUD_delete(request, pk, Screen, "view_screen")

def create_showing(request):
    return CRUD_create(request, showForm, "UWEflix/cinema_manager/create.html", "view_showing")

def view_showing(request):
    return CRUD_view(request, Show, "UWEflix/cinema_manager/showings/view_showing.html")

def delete_showing(request, pk):
    return CRUD_delete(request, pk, Show, "view_showing")

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

# def create_showing(request):
#     form = showForm(request.POST or None)
#     films = Film.objects.all()  # Get all films from database
#     screens = Screen.objects.all()
#     if request.method == "POST":
#         if form.is_valid():
#             show = Show.save(commit=False)
#             show.save()
#             return redirect("view_screen")
#     else:
#             form = showForm()
#     return render(request, "UWEflix/cinema_manager/showings/create_showing.html",{"footer_content":"UWEflix/base/footer_base.html","header_content":"UWEflix/cinema_manager/header_cinema_manager.html","form":form, "films" :films, "screens":screens})

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
