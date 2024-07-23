from . import views
from django.urls import path

urlpatterns = [
    path('',views.menuView,name="menu"),
    path('dishes/<int:dish_id>',views.dish_detail,name="dish_detail")
]