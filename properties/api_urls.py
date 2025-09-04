from django.urls import path
from .api_views import PropertyListView, PropertyCreateView, PropertyDetailView, virtual_tour_create

urlpatterns = [
    path('', PropertyListView.as_view(), name='property-list'),
    path('create/', PropertyCreateView.as_view(), name='property-create'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
    path('<int:property_id>/tour/', virtual_tour_create, name='virtual-tour-create'),
]
