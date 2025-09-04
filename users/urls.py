from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegisterView, UserProfileView

urlpatterns = [
    # Registration
    path('register/', UserRegisterView.as_view(), name='user-register'),

    # JWT login
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # JWT token refresh
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Profile
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
