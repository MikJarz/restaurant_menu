from django import forms
from .models import Menu, FoodItem


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('title', 'description', 'food',)


class FoodForm(forms.ModelForm):

    class Meta:
        model = FoodItem
        fields = ('title', 'description', 'price', 'prepare_time', 'vegan')
