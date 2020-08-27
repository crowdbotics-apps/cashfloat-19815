from rest_framework import authentication
from caisse.models import ANCV, Caisse
from .serializers import ANCVSerializer, CaisseSerializer
from rest_framework import viewsets


class ANCVViewSet(viewsets.ModelViewSet):
    serializer_class = ANCVSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ANCV.objects.all()


class CaisseViewSet(viewsets.ModelViewSet):
    serializer_class = CaisseSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Caisse.objects.all()
