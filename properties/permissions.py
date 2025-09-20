from rest_framework import permissions


class IsLandlordOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow landlords to create properties.
    Tenants and unauthenticated users can only read.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only for authenticated landlords
        return request.user.is_authenticated and request.user.role == 'landlord'


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a property to edit/delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only for the owner of the property
        return obj.owner == request.user


class IsPropertyOwner(permissions.BasePermission):
    """
    Permission to check if user is the property owner.
    Used for virtual tour creation.
    """

    def has_permission(self, request, view):
        # Must be authenticated
        if not request.user.is_authenticated:
            return False

        # For virtual tour creation, check property ownership
        property_id = view.kwargs.get('property_id')
        if property_id:
            from .models import Property
            try:
                property_obj = Property.objects.get(pk=property_id)
                return property_obj.owner == request.user
            except Property.DoesNotExist:
                return False

        return True


class IsLandlord(permissions.BasePermission):
    """
    Permission to check if user is a landlord.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'landlord'
