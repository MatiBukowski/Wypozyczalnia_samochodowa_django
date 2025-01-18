from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import offerManagePanel, addVehicle, removeVehicle, updateVehicle

class ManagementURLsTest(SimpleTestCase):
    def test_manage_panel_url_is_resolved(self):
        url = reverse('management:manage_panelN')
        self.assertEqual(resolve(url).func, offerManagePanel)

    def test_add_vehicle_url_is_resolved(self):
        url = reverse('management:addN')
        self.assertEqual(resolve(url).func, addVehicle)

    def test_remove_vehicle_url_is_resolved(self):
        url = reverse('management:removeN')
        self.assertEqual(resolve(url).func, removeVehicle)

    def test_update_vehicle_url_is_resolved(self):
        url = reverse('management:updateN')
        self.assertEqual(resolve(url).func, updateVehicle)
