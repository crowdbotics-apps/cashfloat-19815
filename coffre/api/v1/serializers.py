from rest_framework import serializers
from coffre.models import Coffre


class CoffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffre
        fields = "__all__"
