from rental.models import Oferta
from .forms import CreateVehicle
from django.test import TestCase
from rental.models import Sprzet

class CreateVehicleFormTest(TestCase):
    def setUp(self):
        """Utwórz przykładową ofertę i przygotuj testy."""
        self.oferta = Oferta.objects.create(nazwa="Oferta Testowa", ID_oferty=1, cena=1)

    def test_create_vehicle_form_valid(self):
        """Test przesyłania poprawnych danych formularza."""
        data = {
            'marka': 'Testowa Marka',
            'model': 'Testowy Model',
            'silnik': '2.0 TDI',
            'moc': 150,
            'moment_obrotowy': 320,
            'typ_sprzetu': 'SUV',
            'ID_oferty': self.oferta,  # Upewnij się, że oferta jest przypisana
        }

        form = CreateVehicle(data=data)
        self.assertTrue(form.is_valid())  # Formularz powinien być poprawny

        # Zapisz dane do bazy, jeśli formularz jest ważny
        sprzet = form.save()

        # Sprawdź, czy obiekt został zapisany w bazie danych
        self.assertEqual(Sprzet.objects.count(), 1)
        self.assertEqual(sprzet.marka, 'Testowa Marka')
        self.assertEqual(sprzet.model, 'Testowy Model')
        self.assertEqual(sprzet.silnik, '2.0 TDI')
        self.assertEqual(sprzet.moc, 150)
        self.assertEqual(sprzet.moment_obrotowy, 320)
        self.assertEqual(sprzet.typ_sprzetu, 'SUV')
        self.assertEqual(sprzet.ID_oferty, self.oferta)
