from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    """
    Endpoint for registering a new user
    Public access
    """
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

class UserProfileView(APIView):
    """
    Endpoint to fetch the current logged-in user's profile
    Requires JWT authentication
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserRegisterSerializer(request.user)
        return Response(serializer.data)
