from . import views
from django.urls import path

urlpatterns = [
    path('',views.IndexView,name='index'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact/', views.ContactView.as_view(),name="contact"),
    path('reservation/', views.ReservationView.as_view(),name="reservation"),
    path('reservationQuery/', views.ReservationQuery,name="reservationQuery"),
    path('reservationDelete/<int:reservation_id>/', views.ReservationDelete,name="reservationDelete"),
]