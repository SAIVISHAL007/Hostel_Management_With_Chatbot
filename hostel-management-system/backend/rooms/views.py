from rest_framework import viewsets
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):  # Changed to ModelViewSet
    queryset = Room.objects.all()
    serializer_class = RoomSerializer