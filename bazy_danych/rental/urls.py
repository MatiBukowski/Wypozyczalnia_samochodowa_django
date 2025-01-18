from django.urls import path, include
from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.offers_list, name="offersN"),
    path('<slug:slug>', views.offers_cars_list, name="offerCarN"),
    path('<slug:oferta_slug>/<slug:sprzet_slug>/', views.cars_data, name="carDataN"),
    path('<slug:oferta_slug>/<slug:sprzet_slug>/reservation/', views.reservation, name="reservationN"),
    path('resList/', views.resList, name="resListN"),
    path('notifications/', views.notificationsList, name="notificationsN"),
    path('notifications/<slug:not_slug>', views.notificationData, name="notificationDataN"),
    path('report/', views.report, name="reportN"),
    path('reports/', views.reportsList, name="reportsN"),

    # path('', views.rental_list),
]