from rest_framework import serializers
from .models import BaseStation


class BaseStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseStation
        fields = '__all__'
