from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="Pizza", price=10.50, description="Cheese pizza")
        self.assertEqual(str(item), "Pizza")
