from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import api

router = DefaultRouter()

router.register("categorias", api.CategoriaViewSet, basename="categoria")

urlpatterns = [
    path("", include(router.urls)),
    # path("auth/register/", api.RegistroView.as_view(), name="registro"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # path("auth/profile/", api.PerfilView.as_view(), name="perfil"),
]
