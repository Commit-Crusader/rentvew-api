from django.db import models
from django.conf import settings

# ---------------------------
# Property Model
# ---------------------------
class Property(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Link to your custom User model
        on_delete=models.CASCADE,
        related_name='properties'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Money
    location = models.CharField(max_length=255)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    main_image = models.ImageField(upload_to='properties/', null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Soft-delete flag
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.location}"


# ---------------------------
# VirtualTour Model
# ---------------------------
class VirtualTour(models.Model):
    property = models.OneToOneField(
        Property,
        on_delete=models.CASCADE,
        related_name='virtual_tour'
    )
    tour_image = models.ImageField(upload_to='tours/')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Virtual Tour: {self.title} for {self.property.title}"
