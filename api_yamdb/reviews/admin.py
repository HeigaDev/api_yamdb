from django.contrib import admin

# Register your models here.
from .models import Category, Genre, Title


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


"""
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'title', 'pub_date', 'author')
    list_filter = ('pub_date',)
    search_fields = ('text',)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'review', 'pub_date', 'author')
    list_filter = ('pub_date',)
    search_fields = ('text',)"""


admin.site.register(Title, TitleAdmin)
admin.site.register(Category)
admin.site.register(Genre)