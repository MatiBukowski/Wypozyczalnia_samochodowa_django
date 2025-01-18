from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import offers_list, offers_cars_list, cars_data, reservation, resList

class RentalURLsTest(SimpleTestCase):
    def test_offers_list_url_is_resolved(self):
        url = reverse('rental:offersN')
        self.assertEqual(resolve(url).func, offers_list)

    def test_offers_cars_list_url_is_resolved(self):
        url = reverse('rental:offerCarN', args=['some-slug'])
        self.assertEqual(resolve(url).func, offers_cars_list)

    def test_cars_data_url_is_resolved(self):
        url = reverse('rental:carDataN', args=['some-offer-slug', 'some-car-slug'])
        self.assertEqual(resolve(url).func, cars_data)

    def test_reservation_url_is_resolved(self):
        url = reverse('rental:reservationN', args=['some-offer-slug', 'some-car-slug'])
        self.assertEqual(resolve(url).func, reservation)

    def test_res_list_url_is_resolved(self):
        url = reverse('rental:resListN')
        self.assertEqual(resolve(url).func, resList)
