from django.test import TestCase
from menu.models import Menu
from django.urls import reverse


class MenuListTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_menus = 15

        for menu_id in range(number_of_menus):
            Menu.objects.create(title="Menu",
                                description="Winter Menu",
                                )

    def test_view_url_exists_at_desired_location(self):
        url = reverse('menu_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('menu_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu_list.html')
