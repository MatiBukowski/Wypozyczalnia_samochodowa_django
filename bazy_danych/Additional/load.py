from bazy_danych.rental.models import Users

Users.objects.all()                             # patrzenie na tablicę Users
user = Users(firstname='Mati', lastname='Bukowski', region='Polska')
user.save()

