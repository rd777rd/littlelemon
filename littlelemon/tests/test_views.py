from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="IceCream", price=80, inventory=60)
        self.menu2 = Menu.objects.create(title="Burger", price=120, inventory=70)

    def test_getall(self):
        response = self.client.get('/restaurant/menu-items/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, 200)
