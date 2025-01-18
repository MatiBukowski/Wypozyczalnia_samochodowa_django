from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import register_view, login_klient_view, login_pracownik_view, logout_view

class UsersURLsTest(SimpleTestCase):
    def test_register_url_is_resolved(self):
        url = reverse('users:registerN')
        self.assertEqual(resolve(url).func, register_view)

    def test_login_url_is_resolved(self):
        url = reverse('users:loginN')
        self.assertEqual(resolve(url).func, login_klient_view)

    def test_login_pracownik_url_is_resolved(self):
        url = reverse('users:loginPN')
        self.assertEqual(resolve(url).func, login_pracownik_view)

    def test_logout_url_is_resolved(self):
        url = reverse('users:logoutN')
        self.assertEqual(resolve(url).func, logout_view)
