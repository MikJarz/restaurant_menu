from django.db import models
from django.utils import timezone


class FoodItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField()
    prepare_time = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    vegan = models.BooleanField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    food = models.ManyToManyField(FoodItem)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
