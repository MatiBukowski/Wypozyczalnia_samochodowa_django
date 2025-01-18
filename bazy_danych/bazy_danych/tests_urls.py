from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.admin.sites import AdminSite
from .views import homepage, about

class MainURLsTest(SimpleTestCase):
    def test_homepage_url_is_resolved(self):
        url = reverse('home')       # generuje URL na podstawie nazwy widoku
        self.assertEqual(resolve(url).func, homepage) # sprawdza, czy podany URL prowadzi do odpowiedniej funkcji widoku.

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

