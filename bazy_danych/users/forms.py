from django import forms
from .models import Klient
from django.contrib.auth.hashers import make_password       # użyte do haszowania hasła
from django.contrib.auth import authenticate

class CustomRegisterForm(forms.ModelForm):
    haslo_2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Potwierdź hasło', 'style': 'width: 500px'}),
        required=True,
        label="Potwierdź hasło",
    )

    class Meta:
        model = Klient
        fields = ['imie', 'nazwisko', 'email', 'telefon', 'login', 'haslo']
        widgets = {
            'imie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię', 'style': 'width: 500px'}),
            'nazwisko': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko', 'style': 'width: 500px'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail', 'style': 'width: 500px'}),
            'login': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login', 'style': 'width: 500px'}),
            'haslo': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło', 'style': 'width: 500px'}),
            'telefon': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Telefon', 'style': 'width: 500px'}),
        }

    def clean(self):                                                         # walidacja hasła
        cleaned_data = super().clean()                                      # pobiera oczyszczone dane
        password1 = cleaned_data.get('haslo')
        password2 = cleaned_data.get('haslo_2')
        phone_number = cleaned_data.get('telefon')
        imie = cleaned_data.get('imie')
        nazwisko = cleaned_data.get('nazwisko')

        if password1 and password2 and password1 != password2:              # jeśli hasła są zgodne
            raise forms.ValidationError("Hasła nie są zgodne!")

        if len(password1) < 8:
            raise forms.ValidationError("Hasło musi być zbudowane z co najmniej 8 znaków")

        if len(str(phone_number)) != 9:                                     # jeśli wprowadzony telefon nie ma 9 cyfr
            raise forms.ValidationError("Błędny numer telefonu!")

        if not imie.isalpha():
            raise forms.ValidationError("Nieprawidłowe imię")

        if not nazwisko.isalpha():
            raise forms.ValidationError("Nieprawidłowe nazwisko")

        return cleaned_data

class CustomLoginForm(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login', 'style': 'width: 500px'}),
        required=True,
    )

    haslo = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło', 'style': 'width: 500px'}),
        required=True,
    )