from .models import Category, Genre, Title
from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'username', 'role', 'bio')
    search_fields = ('role',)
    empty_value_display = '-пусто-'

# Register your models here.


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'year',
        'category',
    )
    list_editable = ('category',)
    search_fields = ('description',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


admin.site.register(Title, TitleAdmin)
admin.site.register(Category)
admin.site.register(Genre)
