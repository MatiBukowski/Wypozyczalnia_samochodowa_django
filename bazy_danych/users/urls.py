from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name="registerN"),
    path("login/", views.login_klient_view, name="loginN"),
    path("loginP/", views.login_pracownik_view, name="loginPN"),
    path("logout/", views.logout_view, name="logoutN"),
]