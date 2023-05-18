from rest_framework import filters, permissions, viewsets
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import Category, Genre, Title
from .serializers import (CategorySerializer, GenreSerializer,
                          RetrieveTitleSerializer, TitleSerializer)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('year', 'name', 'genre__slug', 'category__slug',)

    def get_serializer_class(self):
        # Если запрошенное действие — получение одного объекта
        if self.action == 'retrieve':
            return RetrieveTitleSerializer
        return TitleSerializer


class ListCreateDeleteViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    Собственный базовый класс вьюсета для Post, Delete
    и Get методов.Метод Get только для списка объектов.
    """
    pass


class CategoryViewSet(ListCreateDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(ListCreateDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
