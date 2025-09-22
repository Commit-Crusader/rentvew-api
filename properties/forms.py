from django import forms
from .models import Property, VirtualTour

# Form for creating/editing a Property
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'title', 'description', 'property_type', 'price', 'deposit',
            'address', 'city', 'state', 'country', 'zip_code',
            'bedrooms', 'bathrooms', 'square_feet', 'amenities',
            'available_from', 'status', 'main_image', 'is_active', 'is_featured'
        ]

# Form for creating/editing a Virtual Tour
class VirtualTourForm(forms.ModelForm):
    class Meta:
        model = VirtualTour
        fields = ['title', 'description', 'tour_url', 'platform', 'preview_image', 'iframe_code', 'is_active']
