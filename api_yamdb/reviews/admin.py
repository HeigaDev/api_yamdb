from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'username', 'role', 'bio')
    search_fields = ('role',)
    empty_value_display = '-пусто-'
