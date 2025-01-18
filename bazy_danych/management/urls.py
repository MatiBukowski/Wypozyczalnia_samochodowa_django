from django.urls import path, include
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.offerManagePanel, name="manage_panelN"),
    path('add-vehicle/', views.addVehicle, name="addN"),
    path('remove-vehicle/', views.removeVehicle, name="removeN"),
    path('update-vehicle/', views.updateVehicle, name="updateN"),
]