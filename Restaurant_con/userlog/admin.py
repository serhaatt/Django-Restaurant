from django.contrib import admin
from django.contrib.auth.models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

