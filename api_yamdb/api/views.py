from rest_framework import filters, viewsets
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import Category, Genre, Title
from .permissions import IsAdminOrReadOnly
from .serializers import (CategorySerializer, GenreSerializer,
                          RetrieveTitleSerializer, TitleSerializer)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('year', 'name', 'genre__slug', 'category__slug',)
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        # Если запрошенное действие — получение одного объекта
        if self.action == 'retrieve':
            return RetrieveTitleSerializer
        return TitleSerializer


class ListCreateDestroyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    Собственный класс для категорий и жанров.
    Доступны только методы Post, Delete
    и Get. Метод Get только для списка объектов.
    """
    pass


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)

