from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm                         # automatycznie wbudowany formularz rejestracji i logowania
from .forms import CustomRegisterForm, CustomLoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import authenticate
from .models import Klient, Pracownik
from django.contrib import messages


# Create your views here.

def register_view(request):
    # form = UserCreationForm()
    # użytkownik wysyła formularz po uzupełnieniu danych. Zapytanie HTTP to POST (ponieważ dane są wysyłane do serwera przez kliknięcie przycisku „Zatwierdź”). (Metoda POST - dane przesyłane na serwer)

    if request.method == "POST":                                    # jeśli formularz został zatwierdzony pozytywnie (nie było żadnych błędów i wyjątków, wszystko zostało uzupełnione)
        form = CustomRegisterForm(request.POST)                       # request.POST zawiera dane wysłane przez użytkownika (Django odbiera dane z formularza za pomocą request.POST
        if form.is_valid():                                         # jeśli dane są poprawne
            user = User.objects.create_user(                        # zapisywanie też do modelu User
                username=form.cleaned_data['login'],
                password=form.cleaned_data['haslo'],
            )
            form.save()
            # login(request, form.save())                             # dane są zapisywane, użytkownik zostaje zalogowany
            return redirect("home")
    else:                                                           # jeśli zapytanie nie jest typu POST (czyli użytkownik odwiedza stronę z formularzem po raz pierwszy), wtedy tworzony jest pusty formularz
        form = CustomRegisterForm()
    return render(request, "users/register.html", {"formm":form})

# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():                                         # jeśli dane są poprawne
#             login(request, form.get_user())                         # użytkownik zostaje zalogowany
#             return redirect("home")
#     else:
#         form = AuthenticationForm()
#     return render(request, "users/login.html", {"formm": form})

def login_klient_view(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            login_input = form.cleaned_data['login']
            password = form.cleaned_data['haslo']
            user = authenticate(request, username=login_input, password=password)
            if user is not None:
                try:
                    Klient.objects.get(login=user.username)  # sprawdza czy użytkownik jest klientem
                    login(request, user)
                    return redirect("home")
                except Klient.DoesNotExist:
                    form.add_error(None, 'To konto nie jest zautoryzowane jako klient')
            else:
                form.add_error(None, "Nieprawidłowy login lub hasło")
    else:
        form = CustomLoginForm()
    return render(request, "users/login.html", {"formm": form})

def login_pracownik_view(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            login_input = form.cleaned_data['login']
            password = form.cleaned_data['haslo']
            user = authenticate(request, username=login_input, password=password)
            if user is not None:
                try:
                    Pracownik.objects.get(login=user.username)  # sprawdza czy użytkownik jest pracownikiem
                    login(request, user)
                    return redirect('management:manage_panelN')                        # zalogowanego pracownika przekierowuje do panelu zarządzania ofertą
                except Pracownik.DoesNotExist:
                    form.add_error(None, 'To konto nie jest zautoryzowane jako pracownik')
            else:
                form.add_error(None, "Nieprawidłowy login lub hasło")
    else:
        form = CustomLoginForm()
    return render(request, "users/loginP.html", {"formm": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")