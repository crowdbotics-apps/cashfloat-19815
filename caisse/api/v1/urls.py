from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ANCVViewSet, CaisseViewSet

router = DefaultRouter()
router.register("ancv", ANCVViewSet)
router.register("caisse", CaisseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
