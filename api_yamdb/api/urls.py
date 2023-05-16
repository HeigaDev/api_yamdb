from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, GenreViewSet,
                    TitleViewSet)

v1_router = DefaultRouter()
v1_router.register(r'titles', TitleViewSet)
v1_router.register(r'categories', CategoryViewSet)
v1_router.register(r'genres', GenreViewSet)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
]