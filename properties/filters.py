import django_filters
from .models import Property


class PropertyFilter(django_filters.FilterSet):
    """
    Custom filter for Property model.
    Supports filtering by multiple fields and price ranges.
    """
    # Price range filters
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    # Bedroom/bathroom filters
    min_bedrooms = django_filters.NumberFilter(field_name='bedrooms', lookup_expr='gte')
    max_bedrooms = django_filters.NumberFilter(field_name='bedrooms', lookup_expr='lte')
    min_bathrooms = django_filters.NumberFilter(field_name='bathrooms', lookup_expr='gte')

    # Square feet range
    min_square_feet = django_filters.NumberFilter(field_name='square_feet', lookup_expr='gte')
    max_square_feet = django_filters.NumberFilter(field_name='square_feet', lookup_expr='lte')

    # City filter (case-insensitive contains)
    city = django_filters.CharFilter(lookup_expr='icontains')

    # Amenities filter (case-insensitive contains)
    amenities = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Property
        fields = {
            'property_type': ['exact'],
            'status': ['exact'],
            'bedrooms': ['exact'],
            'bathrooms': ['exact'],
            'city': ['exact', 'icontains'],
            'state': ['exact'],
            'country': ['exact'],
            'is_featured': ['exact'],
            'owner': ['exact'],
        }
