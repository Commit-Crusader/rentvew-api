from rest_framework import generics, permissions
from .models import Property, VirtualTour
from .serializers import PropertySerializer, VirtualTourSerializer

# ---------------------------
# Property API Views
# ---------------------------
class PropertyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property.objects.filter(is_active=True)
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Assign logged-in user as owner


class PropertyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().owner:
            raise PermissionError("You do not have permission to update this property")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.owner:
            raise PermissionError("You do not have permission to delete this property")
        instance.is_active = False
        instance.save()


# ---------------------------
# VirtualTour API Views
# ---------------------------
class VirtualTourCreateAPIView(generics.CreateAPIView):
    serializer_class = VirtualTourSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        property_id = self.kwargs['property_id']
        property_obj = Property.objects.get(id=property_id)
        if property_obj.owner != self.request.user:
            raise PermissionError("Only the owner can add a virtual tour")
        serializer.save(property=property_obj)


class VirtualTourRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VirtualTour.objects.all()
    serializer_class = VirtualTourSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if serializer.instance.property.owner != self.request.user:
            raise PermissionError("Only the owner can update this virtual tour")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.property.owner != self.request.user:
            raise PermissionError("Only the owner can delete this virtual tour")
        instance.delete()
