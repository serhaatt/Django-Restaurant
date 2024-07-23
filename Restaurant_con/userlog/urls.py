from . import views
from django.urls import path

urlpatterns = [
    path('login',views.user_login,name="login"),
    path('register',views.user_register,name="register"),
    path('activate<uidb64>/<token>',views.activate,name='activate'),
    path('logout/',views.user_logout,name="logout"),
]