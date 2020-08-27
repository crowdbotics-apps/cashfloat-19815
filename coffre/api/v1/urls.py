from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CoffreViewSet

router = DefaultRouter()
router.register("coffre", CoffreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
