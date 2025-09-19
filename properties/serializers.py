from rest_framework import serializers
from .models import Property, VirtualTour

# ---------------------------
# VirtualTour Serializer
# ---------------------------
class VirtualTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualTour
        fields = [
            'id', 'title', 'description', 'tour_url', 'platform',
            'preview_image', 'iframe_code', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

# ---------------------------
# Property Serializer
# ---------------------------
class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Show owner's username
    virtual_tour = VirtualTourSerializer(read_only=True)  # Nested virtual tour

    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'price', 'location',
            'bedrooms', 'bathrooms', 'main_image', 'is_active',
            'owner', 'virtual_tour', 'created_at', 'updated_at'
        ]
