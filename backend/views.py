from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import TouristDestination
from .serializers import TouristDestinationSerializer

class TouristDestinationListAPIView(generics.ListAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

class TouristDestinationDetailAPIView(generics.RetrieveAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

class TouristDestinationCreateAPIView(generics.CreateAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

class TouristDestinationDeleteAPIView(generics.DestroyAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TouristDestinationUpdateAPIView(generics.UpdateAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer