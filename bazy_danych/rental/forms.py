from django import forms
from .models import Rezerwacja, Sprzet, Usterka
from users.models import Klient

class CreateReservation(forms.ModelForm):

    class Meta:
        model = Rezerwacja
        fields = ['data_poczatku', 'data_zwrotu']
        widgets = {
            'data_poczatku': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data początku rezerwacji', 'type': 'date', 'style': 'width: 300px'}),
            'data_zwrotu': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data zwrotu', 'type': 'date', 'style': 'width: 300px'}),
        }

class ReportFault(forms.ModelForm):
    class Meta:
        model = Usterka
        fields = ['ID_sprzetu', 'opis']
        widgets = {
            'opis': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Opisz problem', 'style': 'width: 1000px; height: 400px; margin-left: 100px;'}),
        }

    def __init__(self, *args, **kwargs):                # konstruktor formularza
        user = kwargs.pop('user', None)  # Pobierz użytkownika przekazanego do formularza
        super().__init__(*args, **kwargs)

        self.fields['ID_sprzetu'].widget = forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'})

        if user and user.is_authenticated:
            klient = Klient.objects.filter(login=user.username).first()         # .first() - jak klinet[0] - czyli ID_klienta
            if klient:
                rezerwacje = Rezerwacja.objects.filter(ID_klienta=klient)
                sprzety = Sprzet.objects.filter(ID_sprzetu__in=rezerwacje.values_list('ID_sprzetu', flat=True)) # values_list('ID_sprzetu'): Tworzy queryset zwracający tylko wartości kolumny ID_sprzetu (zamiast pełnych obiektów Rezerwacja). flat=True: Sprawia, że wynikowa lista będzie jednowymiarowa (pojedyncze wartości ID_sprzetu zamiast krotek, np. [1, 2, 3] zamiast [(1,), (2,), (3,)])
                self.fields['ID_sprzetu'].queryset = sprzety
            else:
                self.fields['ID_sprzetu'].queryset = Sprzet.objects.none()  # Pusty queryset, gdy klient nie istnieje
        else:
            self.fields['ID_sprzetu'].queryset = Sprzet.objects.none()  # Pusty queryset dla niezalogowanego użytkownika