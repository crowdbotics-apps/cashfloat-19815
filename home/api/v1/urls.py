from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CbViewSet,
    ChequeViewSet,
    CustomTextViewSet,
    EspeceViewSet,
    HomePageViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("espece", EspeceViewSet)
router.register("cheque", ChequeViewSet)
router.register("cb", CbViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
