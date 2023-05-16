from rest_framework import filters, permissions, viewsets
from rest_framework import mixins

from reviews.models import Category, Genre, Title
from .serializers import (CategorySerializer, GenreSerializer,
                          RetrieveTitleSerializer, TitleSerializer)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

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


class GenreViewSet(ListCreateDeleteViewSet): # то, что работает
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
