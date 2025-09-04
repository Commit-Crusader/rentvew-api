from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import Property, VirtualTour
from .serializers import PropertySerializer, VirtualTourSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

# Property views
class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.filter(is_active=True)
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]

class PropertyCreateView(generics.CreateAPIView):
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().owner != self.request.user:
            raise PermissionError("You do not have permission to update this property.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionError("You do not have permission to delete this property.")
        instance.is_active = False
        instance.save()

# Virtual tour creation
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def virtual_tour_create(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    if property_obj.owner != request.user:
        return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = VirtualTourSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(property=property_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
