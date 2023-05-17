from .views import (CategoryViewSet, GenreViewSet,
                    TitleViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, get_jwt_token, register

router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]


v1_router = DefaultRouter()
v1_router.register(r'titles', TitleViewSet)
v1_router.register(r'categories', CategoryViewSet)
v1_router.register(r'genres', GenreViewSet)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
