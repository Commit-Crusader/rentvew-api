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
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    virtual_tour = VirtualTourSerializer(read_only=True)
    amenities_list = serializers.ReadOnlyField(source='get_amenities_list')

    class Meta:
        model = Property
        fields = [
            'id', 'owner', 'owner_id', 'title', 'description',
            'property_type', 'price', 'deposit', 'address', 'city',
            'state', 'country', 'zip_code', 'location', 'bedrooms',
            'bathrooms', 'square_feet', 'amenities', 'amenities_list',
            'available_from', 'status', 'main_image', 'is_active',
            'is_featured', 'virtual_tour', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'owner', 'owner_id']
