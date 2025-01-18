from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Klient
from .models import Pracownik

class KlientAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Znajdź klienta po nazwie użytkownika
            klient = Klient.objects.get(login=username)

            # Porównanie hasła wprost (niehaszowane)
            if password == klient.haslo:
                return klient
        except Klient.DoesNotExist:
            return None

    def get_user(self, id_klienta):
        try:
            return Klient.objects.get(pk=id_klienta)
        except Klient.DoesNotExist:
            return None

class PracownikAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Znajdź pracownika po nazwie użytkownika
            pracownik = Pracownik.objects.get(login=username)

            # Porównanie hasła wprost (niehaszowane)
            if password == pracownik.haslo:
                return pracownik
        except Pracownik.DoesNotExist:
            return None

    def get_user(self, id_pracownika):
        try:
            return Pracownik.objects.get(pk=id_pracownika)
        except Pracownik.DoesNotExist:
            return None