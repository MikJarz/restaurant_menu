from django.shortcuts import render
from django.utils import timezone
from .models import Menu
from django.shortcuts import render, get_object_or_404


def menu_list(request):
    menus = Menu.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'menu/menu_list.html', {'menus': menus})

def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})
