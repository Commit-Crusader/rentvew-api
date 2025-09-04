from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    # Role choices
    TENANT = 'tenant'
    LANDLORD = 'landlord'
    ROLE_CHOICES = [
        (TENANT, 'Tenant'),
        (LANDLORD, 'Landlord'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=TENANT)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
