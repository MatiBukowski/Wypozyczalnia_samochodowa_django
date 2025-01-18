import datetime

from django.db import models
from django.utils.text import slugify
from users.models import Klient, Pracownik
from datetime import date
# Create your models here.
class Oferta(models.Model):
    ID_oferty = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(max_length=8000)
    cena = models.FloatField()
    typ_sprzetu = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.nazwa


class Sprzet(models.Model):
    ID_sprzetu = models.AutoField(primary_key=True)
    marka = models.CharField(max_length=15, )
    model = models.CharField(max_length=20)
    silnik = models.CharField(max_length=25)
    moc = models.IntegerField()
    moment_obrotowy = models.IntegerField()
    lokalizacja = models.CharField(max_length=50, default='Wrocław')
    status_dostepnosci = models.CharField(max_length=15, default='dostępny')
    typ_sprzetu = models.CharField(max_length=30)
    status_zamkniecia = models.CharField(max_length=15, default='zamknięty')
    status_zablokowania = models.CharField(max_length=15, default='zablokowany')
    ID_oferty = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name='sprzety', default='1')                       # gdy oferta zostanie usunięta, rekordy z tą ofertą także zostaną usunięte, (related_name='sprzety' pozwala na dostęp do wszystkich sprzętów powiązanych z daną ofertą)
    slug = models.SlugField(default='', blank=True)

    def save(self, *args, **kwargs):
        # Generowanie slug na podstawie marki i modelu
        self.slug = slugify(f"{self.marka}-{self.model}")       # slugify: Funkcja, która konwertuje tekst na przyjazny dla URL format (np. "BMW X5" -> "bmw-x5")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.marka + " " + self.model

# class Klient(models.Model):
#     ID_klienta = models.IntegerField(primary_key=True)
#     imie = models.CharField(max_length=20)
#     nazwisko = models.CharField(max_length=30)
#     email = models.CharField(max_length=100)
#     telefon = models.IntegerField()
#     login = models.CharField(max_length=10)
#     haslo = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.imie + " " + self.nazwisko

# class Pracownik(models.Model):
#     ID_pracownika = models.IntegerField(primary_key=True)
#     imie = models.CharField(max_length=20)
#     nazwisko = models.CharField(max_length=30)
#     email = models.CharField(max_length=100)
#     telefon = models.IntegerField()
#     login = models.CharField(max_length=10)
#     haslo = models.CharField(max_length=30)
#     rola = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.imie + " " + self.nazwisko
class Rezerwacja(models.Model):
    ID_rezerwacji = models.AutoField(primary_key=True)
    ID_klienta = models.ForeignKey(Klient, on_delete=models.CASCADE)
    ID_oferty = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    ID_sprzetu = models.ForeignKey(Sprzet, on_delete=models.CASCADE)
    data_poczatku = models.DateField()
    data_zwrotu = models.DateField()
    status = models.CharField(max_length=20)

class Usterka(models.Model):
    ID_usterki = models.AutoField(primary_key=True)
    ID_sprzetu = models.ForeignKey(Sprzet, on_delete=models.CASCADE)
    ID_klienta_zglaszajacego = models.ForeignKey(Klient, on_delete=models.CASCADE)
    opis = models.CharField(max_length=8000)
    data_wyslania = models.DateField(default='2025-01-01')
    status = models.CharField(max_length=20, default='w trakcie')

class Powiadomienie(models.Model):
    ID_powiadomienia = models.AutoField(primary_key=True)
    ID_pracownika = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    ID_klienta = models.ForeignKey(Klient, on_delete=models.CASCADE)
    ID_sprzetu = models.ForeignKey(Sprzet, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=30)
    tresc = models.CharField(max_length=8000)
    data_wyslania = models.DateField(default='2025-01-01')
    typ = models.CharField(max_length=30)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return self.tytul

    def save(self, *args, **kwargs):
        # Generowanie slug na podstawie marki i modelu
        self.slug = slugify(f"{self.ID_powiadomienia}-{self.tytul}")
        super().save(*args, **kwargs)