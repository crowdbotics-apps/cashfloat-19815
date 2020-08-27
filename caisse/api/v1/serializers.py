from rest_framework import serializers
from caisse.models import ANCV, Caisse


class ANCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = ANCV
        fields = "__all__"


class CaisseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caisse
        fields = "__all__"
