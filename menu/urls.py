from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('menu/<int:pk>/', views.menu_detail, name='menu_detail'),
    path('menu/new/', views.menu_new, name='menu_new'),
    path('food/new/', views.food_new, name='food_new'),
    path('menu/<int:pk>/edit/', views.menu_edit, name='menu_edit'),
]
