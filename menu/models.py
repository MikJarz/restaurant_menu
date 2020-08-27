from django.db import models
from django.utils import timezone


class Menu(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)


class FoodItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    prepare_time = models.PositiveIntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    vegan = models.BooleanField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title