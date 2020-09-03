from django.test import TestCase
from django.urls import reverse, resolve
from menu.views import menu_list


class UrlsTest(TestCase):
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, menu_list)

    def test_menu_detail(self):
        response = reverse('menu_detail', args=[1254])
        self.assertEqual(response, '/menu/1254/')

    def test_menu_new(self):
        url = reverse('menu_new')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_food_new(self):
        url = reverse('food_new')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_menu_edit(self):
        response = reverse('menu_edit', args=[1254])
        self.assertEqual(response, '/menu/1254/edit/')
