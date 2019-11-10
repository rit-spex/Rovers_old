# todo/serializers.py

from rest_framework import serializers
from .models import Rover_Base_Station

# Specifies the model to work with and the fields we want to be converted to JSON.
class Rover_Base_Station_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Rover_Base_Station
        fields = ('id', 'title', 'description', 'completed')