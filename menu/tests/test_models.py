from django.test import TestCase
from django.utils import timezone
from menu.models import FoodItem, Menu


class FoodItemTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        FoodItem.objects.create(title="Pizza",
                                description="Good Italian Pizza",
                                price="50",  # ??
                                prepare_time="10",  # ??
                                created_date=timezone.now(),  # czy musi być mock?
                                modified_date=timezone.now(),  # jak zrobić modified_date?
                                vegan=True  # ??
                                )

    def test_title_label(self):
        fooditem = FoodItem.objects.get(id=1)
        field_label = fooditem._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        fooditem = FoodItem.objects.get(id=1)
        max_length = fooditem._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

    def test_description_label(self):
        fooditem = FoodItem.objects.get(id=1)
        field_label = fooditem._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_description_max_length(self):
        fooditem = FoodItem.objects.get(id=1)
        max_length = fooditem._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)

    def test_model_str(self):
        fooditem = FoodItem.objects.create(title="Spaghetti",
                                           description="Pasta spaghetti",
                                           price="2",
                                           prepare_time="4",
                                           created_date=timezone.now(),
                                           modified_date=timezone.now(),
                                           vegan=True
                                           )
        self.assertEqual(str(fooditem), "Spaghetti")


class MenuTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(title="Menu",
                            description="Winter Menu",
                            )

    def test_title_label(self):
        menu = Menu.objects.get(id=1)
        field_label = menu._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        menu = Menu.objects.get(id=1)
        max_length = menu._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

    def test_description_label(self):
        menu = Menu.objects.get(id=1)
        field_label = menu._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_description_max_length(self):
        menu = Menu.objects.get(id=1)
        max_length = menu._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)

    def test_menu_has_a_food(self):
        menu = Menu.objects.create(title="Menu",
                                   description="Winter Menu",
                                   )
        fooditem = FoodItem.objects.create(title="Spaghetti",
                                           description="Pasta spaghetti",
                                           price="2",
                                           prepare_time="4",
                                           created_date=timezone.now(),
                                           modified_date=timezone.now(),
                                           vegan=True
                                           )
        fooditem2 = FoodItem.objects.create(title="Lasagne",
                                            description="Italian Lasagne",
                                            price="23",
                                            prepare_time="7",
                                            created_date=timezone.now(),
                                            modified_date=timezone.now(),
                                            vegan=False
                                            )
        menu.food.set([fooditem, fooditem2])
        self.assertEqual(menu.food.count(), 2)

    def test_model_str(self):
        menu = Menu.objects.create(title="Menu",
                                   description="Winter Menu",
                                   )
        self.assertEqual(str(menu), "Menu")
