from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import Rover_Base_Station_Serializer  
from .models import Rover_Base_Station

class Rover_Base_Station_View(viewsets.ModelViewSet):
    serializer_class = Rover_Base_Station_Serializer 
    queryset = Rover_Base_Station.objects.all()