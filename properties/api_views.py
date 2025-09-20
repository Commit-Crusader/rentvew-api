from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import Property, VirtualTour
from .serializers import PropertySerializer, VirtualTourSerializer
from .permissions import IsLandlordOrReadOnly, IsOwnerOrReadOnly, IsPropertyOwner
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

# Property views
class PropertyListView(generics.ListAPIView):
    """
    List all active properties.
    Public access.
    """
    queryset = Property.objects.filter(is_active=True)
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]


class PropertyCreateView(generics.CreateAPIView):
    """
    Create a new property.
    Only landlords can create properties.
    """
    serializer_class = PropertySerializer
    permission_classes = [IsLandlordOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a property.
    Only the owner can update/delete.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_destroy(self, instance):
        # Soft delete
        instance.is_active = False
        instance.save()


# Virtual tour creation
@api_view(['POST'])
@permission_classes([IsPropertyOwner])
def virtual_tour_create(request, property_id):
    """
    Create a virtual tour for a property.
    Only the property owner can create tours.
    """
    property_obj = get_object_or_404(Property, pk=property_id)

    serializer = VirtualTourSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(property=property_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
