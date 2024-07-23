from django.shortcuts import render
from . models import Dish

def menuView(request):
    dishes_drink = Dish.objects.filter(Food_Category__name='İçecek')
    dishes = Dish.objects.filter(Food_Category__name='Ana Yemek')
    dishes_desserts = Dish.objects.filter(Food_Category__name='Tatlı')
    context = {
        'dishes_drinks' : dishes_drink,
        'dishes' : dishes,
        'dishes_desserts' : dishes_desserts,
    }
    return render(request,'menu.html',context)

def dish_detail(request,dish_id):
    dish = Dish.objects.get(id=dish_id)
    context = {
        'dish':dish,
    }
    return render(request,'dish.html',context)

