from django_filters import rest_framework as filters
from reviews.models import Category, Genre, Review, Title


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
        pass

class TitleFilter(filters.FilterSet):
    genre = CharFilterInFilter(
        field_name='genre__slug', lookup_expr='in'
    )
    category = CharFilterInFilter(
        field_name='category__slug', lookup_expr='in'
    )
    class Meta:
        model = Title
        fields = ['year', 'name', 'category', 'genre']