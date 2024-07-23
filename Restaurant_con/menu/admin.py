from django.contrib import admin
from . models import Dish,Category

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('Food_Name','Food_Price','Food_Available')
    list_filter = ('Food_Available',)
    search_fields = ('Food_Name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)