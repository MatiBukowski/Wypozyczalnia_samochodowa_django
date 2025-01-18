from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateVehicle, RemoveVehicle, UpdateVehicleSprzet, UpdateVehicle
from rental.models import Sprzet

global Sprzettt
# Create your views here.
@login_required
def offerManagePanel(request):
    return render(request, 'offers_management_panel/offers_management.html')

@login_required
def addVehicle(request):
    if request.method == 'POST':
        form = CreateVehicle(request.POST)
        if form.is_valid():
            form.save()
            return redirect('management:manage_panelN')
    else:
        form = CreateVehicle()
    return render(request, 'offers_management_panel/addVehicle.html', {'formm': form})

@login_required
def removeVehicle(request):
    if request.method == 'POST':
        form = RemoveVehicle(request.POST)
        if form.is_valid():
            sprzet = form.cleaned_data['ID_sprzetu']
            sprzet.delete()
            return redirect('management:manage_panelN')
    else:
        form = RemoveVehicle()
    return render(request, 'offers_management_panel/removeVehicle.html', {'formm': form})

@login_required
def updateVehicle(request):
    global Sprzettt
    if request.method == 'POST':
        if 'select_vehicle' in request.POST:            # jeśli krok 1 - wybór pojazdu
            form_sprzet = UpdateVehicleSprzet(request.POST)
            if form_sprzet.is_valid():
                sprzet = form_sprzet.cleaned_data['ID_sprzetu']
                Sprzettt = sprzet
                form = UpdateVehicle(instance=sprzet)   # po wyborze sprzętu wyświetla się nowy, wypełniony istniejącymi danymi formularz
                return render(request, 'offers_management_panel/updateVehicle.html', {'formm': form, 'step': 2})

        elif 'update_vehicle' in request.POST:          # jeśli krok 2 - aktualizacja danych pojazdu
            form = UpdateVehicle(request.POST, instance=Sprzettt)
            if form.is_valid():
                form.save()
                return redirect('management:manage_panelN')
    else:
        form_sprzet = UpdateVehicleSprzet()
    return render(request, 'offers_management_panel/updateVehicle.html', {'formm': form_sprzet, 'step': 1})
