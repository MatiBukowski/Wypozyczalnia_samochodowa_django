from django import forms
from rental.models import Sprzet, Oferta

class CreateVehicle(forms.ModelForm):
    TYP_SPRZETU_CHOICES = [
        ('Supersamochód', 'Supersamochód'),                 # pierwsze zapisywane w bazie danych, drugie wyświetlane
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Kompakt', 'Kompakt'),
    ]

    typ_sprzetu = forms.ChoiceField(
        choices=TYP_SPRZETU_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px'}),
    )

    ID_oferty = forms.ModelChoiceField(
        queryset=Oferta.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px'}),
        label="ID oferty",
    )

    class Meta:
        model = Sprzet
        fields = ['marka', 'model', 'silnik', 'moc', 'moment_obrotowy', 'typ_sprzetu', 'ID_oferty']
        widgets = {
            'marka': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marka', 'style': 'width: 300px'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model', 'style': 'width: 300px'}),
            'silnik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Silnik', 'style': 'width: 300px'}),
            'moc': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Moc', 'style': 'width: 300px'}),
            'moment_obrotowy': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Moment obrotowy', 'style': 'width: 300px'}),
        }

    def clean(self):
        cleaned_data = super().clean()  # pobiera oczyszczone dane
        moc = cleaned_data.get('moc')
        moment = cleaned_data.get('moment_obrotowy')

        if moc < 0:
            raise forms.ValidationError("Moc pojazdu nie może być ujemna")

        if moment < 0:
            raise forms.ValidationError("Moment obortowy pojazdu nie może być ujemny")

        return cleaned_data

class RemoveVehicle(forms.Form):
    ID_sprzetu = forms.ModelChoiceField(
        queryset=Sprzet.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px'}),
        label="Wybierz pojazd",
    )

class UpdateVehicleSprzet(forms.Form):
    ID_sprzetu = forms.ModelChoiceField(
        queryset=Sprzet.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px'}),
        label="Wybierz pojazd",
    )



class UpdateVehicle(forms.ModelForm):
    STATUS_DOSTEPNOSCI_CHOICES = [
        ('dostępny', 'dostępny'),  # pierwsze zapisywane w bazie danych, drugie wyświetlane
        ('niedostępny', 'niedostępny'),
    ]
    STATUS_ZAMKNIECIA_CHOICES = [
        ('zamknięty', 'zamknięty'),  # pierwsze zapisywane w bazie danych, drugie wyświetlane
        ('otwarty', 'otwarty'),
    ]
    STATUS_ZABLOKOWANIA_CHOICES = [
        ('zablokowany', 'zablokowany'),  # pierwsze zapisywane w bazie danych, drugie wyświetlane
        ('odblokowany', 'odblokowany'),
    ]
    TYP_SPRZETU_CHOICES = [
        ('Supersamochód', 'Supersamochód'),  # pierwsze zapisywane w bazie danych, drugie wyświetlane
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Kompakt', 'Kompakt'),
    ]

    status_dostepnosci = forms.ChoiceField(
        choices=STATUS_DOSTEPNOSCI_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px'}),
    )
    status_zamkniecia = forms.ChoiceField(
        choices=STATUS_ZAMKNIECIA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px'}),
    )
    status_zablokowania = forms.ChoiceField(
        choices=STATUS_ZABLOKOWANIA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px'}),
    )
    typ_sprzetu = forms.ChoiceField(
        choices=TYP_SPRZETU_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px'}),
    )

    ID_oferty = forms.ModelChoiceField(
        queryset=Oferta.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px'}),
        label="ID oferty",
    )


    class Meta:
        model = Sprzet
        fields = ['ID_sprzetu', 'marka', 'model', 'silnik', 'moc', 'moment_obrotowy', 'lokalizacja', 'status_dostepnosci', 'typ_sprzetu', 'status_zamkniecia', 'status_zablokowania', 'ID_oferty']
        widgets = {
            'marka': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'silnik': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'moc': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'moment_obrotowy': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'lokalizacja': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
        }

    def clean(self):
        cleaned_data = super().clean()  # pobiera oczyszczone dane
        moc = cleaned_data.get('moc')
        moment = cleaned_data.get('moment_obrotowy')

        if moc < 0:
            raise forms.ValidationError("Moc pojazdu nie może być ujemna")

        if moment < 0:
            raise forms.ValidationError("Moment obortowy pojazdu nie może być ujemny")

        return cleaned_data


