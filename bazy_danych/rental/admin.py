from django.contrib import admin
from .models import Oferta, Sprzet, Klient, Pracownik, Rezerwacja, Usterka, Powiadomienie
# Register your models here.
admin.site.register(Oferta)
admin.site.register(Sprzet)
admin.site.register(Klient)
admin.site.register(Pracownik)
admin.site.register(Rezerwacja)
admin.site.register(Usterka)
admin.site.register(Powiadomienie)