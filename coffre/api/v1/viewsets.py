from rest_framework import authentication
from coffre.models import Coffre
from .serializers import CoffreSerializer
from rest_framework import viewsets


class CoffreViewSet(viewsets.ModelViewSet):
    serializer_class = CoffreSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Coffre.objects.all()
