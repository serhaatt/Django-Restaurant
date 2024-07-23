from django.contrib import admin
from .models import Contact,Reservation

admin.site.register(Contact)
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('First_Name','Phone','Date','hour','person')
    search_fields = ('First_Name','Last_Name')

