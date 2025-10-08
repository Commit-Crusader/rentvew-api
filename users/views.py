from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer, UserProfileSerializer

User = get_user_model()


class UserRegisterView(generics.CreateAPIView):
    """
    Endpoint for registering a new user.
    Public access.
    """
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Endpoint to retrieve and update the current logged-in user's profile.
    Requires JWT authentication.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Return the current authenticated user"""
        return self.request.user
