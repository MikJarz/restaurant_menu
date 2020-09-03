from django.test import TestCase
from http import HTTPStatus


class AddMenuViewTests(TestCase):
    def test_get(self):
        response = self.client.get("/menu/new/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # def test_menu_success(self):
    #     response = self.client.post(
    #         "/menu/new/", data={"title": "Menu#1",
    #                             "description": "AAAAAAAAAA",
    #                             "food": "Pizza"
    #                             }, follow=True
    #     )
    #     self.assertEqual(response.status_code, HTTPStatus.FOUND)
    #     self.assertEqual(response["Location"], "/menu/") /jak zrobić przekierownaie z odpowiadajacym pk?


class AddFoodViewTests(TestCase):
    def test_get(self):
        response = self.client.get("/food/new/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_food_success(self):
        response = self.client.post(
            "/food/new/", data={"title": "Food#1",
                                "description": "AAAAAAAAAA",
                                "price": "500000",
                                "prepare_time": "535",
                                "vegan": "True"
                                }
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], "/")
