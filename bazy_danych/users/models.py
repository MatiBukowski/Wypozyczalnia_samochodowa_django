from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password       # użyte do haszowania hasła
from django.contrib.auth.backends import BaseBackend

# Create your models here.
class Klient(models.Model):
    ID_klienta = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    telefon = models.IntegerField(null=True, blank=True)
    login = models.CharField(unique=True, max_length=20)
    haslo = models.CharField(max_length=30)
    is_pracownik = models.BooleanField(default=False)

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Pracownik(models.Model):
    ID_pracownika = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.CharField(max_length=100, unique=True)
    telefon = models.IntegerField(null=True, blank=True)
    login = models.CharField(unique=True, max_length=20)
    haslo = models.CharField(max_length=30)
    rola = models.CharField(max_length=30)
    is_pracownik = models.BooleanField(default=True)

    def __str__(self):
        return self.imie + " " + self.nazwisko