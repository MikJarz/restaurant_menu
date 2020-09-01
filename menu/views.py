from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Menu
from django.shortcuts import render, get_object_or_404
from .forms import MenuForm, FoodForm
from django.core.paginator import Paginator
from django.db.models import Count


def menu_list(request):
    menus = Menu.objects.filter(created_date__lte=timezone.now())
    answer = request.GET.get('sort', False)

    if answer == "name":
        menus = Menu.objects.filter(created_date__lte=timezone.now()).order_by('title')
    if answer == "-name":
        menus = Menu.objects.filter(created_date__lte=timezone.now()).order_by('-title')
    if answer == "count":
        foodcount = Menu.objects.filter(created_date__lte=timezone.now())
        menus = foodcount.annotate(num_food=Count('food')).order_by('-num_food')
    if answer == "-count":
        foodcount = Menu.objects.filter(created_date__lte=timezone.now())
        menus = foodcount.annotate(num_food=Count('food')).order_by('num_food')

    paginator = Paginator(menus, 1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'menu/menu_list.html', {'menus': page_obj.object_list,
                                                   'paginator': paginator})


def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def menu_new(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.modified_date = timezone.now()
            menu.created_date = timezone.now()
            menu.save()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm()
    return render(request, 'menu/menu_edit.html', {'form': form})


def food_new(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.created_date = timezone.now()
            food.save()
            return redirect('menu_list')
    else:
        form = FoodForm()
    return render(request, 'menu/food_edit.html', {'form': form})


def menu_edit(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.modified_date = timezone.now()
            menu.save()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm(instance=menu)
    return render(request, 'menu/menu_edit.html', {'form': form})
