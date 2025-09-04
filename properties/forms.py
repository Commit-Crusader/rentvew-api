from django import forms
from .models import Property, VirtualTour

# Form for creating/editing a Property
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'location', 'bedrooms', 'bathrooms', 'main_image', 'is_active']

# Form for creating/editing a Virtual Tour
class VirtualTourForm(forms.ModelForm):
    class Meta:
        model = VirtualTour
        fields = ['tour_image', 'title', 'description']
