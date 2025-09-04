from django.urls import path
from . import api_views

urlpatterns = [
    # Property API endpoints
    path('', api_views.PropertyListCreateAPIView.as_view(), name='api_property_list_create'),
    path('<int:pk>/', api_views.PropertyRetrieveUpdateDestroyAPIView.as_view(), name='api_property_detail'),

    # Virtual Tour API endpoints
    path('<int:property_id>/tour/', api_views.VirtualTourCreateAPIView.as_view(), name='api_tour_create'),
    path('tour/<int:pk>/', api_views.VirtualTourRetrieveUpdateDestroyAPIView.as_view(), name='api_tour_detail'),
]
