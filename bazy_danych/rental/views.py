from django.shortcuts import render, redirect
from .models import Oferta, Sprzet, Rezerwacja, Usterka, Powiadomienie
from . import forms
from users.models import Klient, Pracownik
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now


from django.http import HttpResponse

# Create your views here.

def offers_list(request):
    oferty = Oferta.objects.all().order_by('ID_oferty')
    return render(request, 'offers/offers_list.html', {'oferty': oferty})                               # w offers_list tworzę slug

def offers_cars_list(request, slug):                                                                                        # utworzonę slug przekazuję tutaj
    # return HttpResponse(slug)
    oferta = Oferta.objects.get(slug=slug)
    sprzety = Sprzet.objects.filter(ID_oferty=oferta.ID_oferty)
    return render(request, 'rental/rental_list.html', {'sprzetyy': sprzety, 'oferta': oferta})           # w rental_list tworzę ofert_slug oraz sprzet_slug bo inaczej w adresie dwa sie nie wczytają i nie będą widoczne

def cars_data(request, oferta_slug, sprzet_slug):                                                                                        # utworzonę oferta_slug oraz sprzet_slug przekazuję tutaj
    sprzet = Sprzet.objects.get(slug=sprzet_slug)
    oferta = Oferta.objects.get(slug=oferta_slug)
    return render(request, 'cars/data_list.html', {'sprzett': sprzet, 'oferta': oferta})

def reservation(request, oferta_slug, sprzet_slug):
    # form = forms.CreateReservation()
    sprzet = Sprzet.objects.get(slug=sprzet_slug)
    oferta = Oferta.objects.get(slug=oferta_slug)
    klient = Klient.objects.filter(login=request.user.username)  # Pobieramy obiekt Klient na podstawie loginu
    today = date.today()

    if request.method == 'POST':
        form = forms.CreateReservation(request.POST)
        if form.is_valid():
            rezerwacja = form.save(commit=False)                        # commit=False - jeszcze formularz nie zapisywany, tylko tworzony na podstawie formularza obiekt rezerwacja
            rezerwacja.ID_klienta = klient[0]
            rezerwacja.ID_oferty = oferta
            rezerwacja.ID_sprzetu = sprzet

            if rezerwacja.data_poczatku <= today <= rezerwacja.data_zwrotu:
                rezerwacja.status = "W trakcie"
                sprzet.status_dostepnosci = "niedostępny"
                sprzet.save()
            else:
                rezerwacja.status = "Zaplanowana"
            rezerwacja.save()
            return redirect('home')
    else:
        form = forms.CreateReservation()
    return render(request, 'reservation/reservation.html', {'formm': form, 'sprzett': sprzet, 'ofertaa': oferta})

def resList(request):                       # lista rezerwacji wykonanych przez klienta
    # rezerwacja = Rezerwacja.objects.all().order_by('ID_rezerwacji')
    klient = Klient.objects.filter(login=request.user.username)
    rezerwacja = Rezerwacja.objects.filter(ID_klienta = klient[0])
    return render(request, 'reservation/resList.html', {'rezerwacje': rezerwacja})

def notificationsList(request):
    klient = Klient.objects.filter(login=request.user.username).first()
    powiadomienia = Powiadomienie.objects.filter(ID_klienta=klient)
    return render(request, 'notification/notificationsList.html', {'powiadomieniaa': powiadomienia})

def notificationData(request, not_slug):
    powiadomienie = Powiadomienie.objects.get(slug=not_slug)
    return render(request, 'notification/notificationMessage.html', {'powiadomieniee': powiadomienie})
def report(request):
    if request.method == 'POST':
        form = forms.ReportFault(request.POST, user=request.user)
        if form.is_valid():
            usterka = form.save(commit=False)
            usterka.ID_klienta_zglaszajacego = Klient.objects.get(login=request.user.username)
            usterka.data_wyslania = now().date()
            usterka.save()
            return redirect('home')  # Zmień na odpowiednią stronę
    else:
        form = forms.ReportFault(user=request.user)

    return render(request, 'report/report_fault.html', {'formm': form})

def reportsList(request):                       # lista rezerwacji wykonanych przez klienta
    usterka = Usterka.objects.all()
    return render(request, 'report/reportList.html', {'usterkii': usterka})
# def rental_list(request):
#     sprzety = Sprzet.objects.all().order_by('ID_sprzetu')                                                                  # - to na odwrót
#     return render(request, 'rental/rental_list.html', {'sprzety': sprzety})                             # trzeci parametr to dictionary
