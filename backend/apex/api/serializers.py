from rest_framework.serializers import ModelSerializer
from .models import *


class FiszkiSerializer(ModelSerializer):
    class Meta:
        model= fiszka
        fields= '__all__'