from django.db import models
from django.conf import settings

# ---------------------------
# Property Model
# ---------------------------
class Property(models.Model):
    # Property type choices
    APARTMENT = 'apartment'
    HOUSE = 'house'
    CONDO = 'condo'
    STUDIO = 'studio'
    TOWNHOUSE = 'townhouse'
    ROOM = 'room'

    PROPERTY_TYPE_CHOICES = [
        (APARTMENT, 'Apartment'),
        (HOUSE, 'House'),
        (CONDO, 'Condo'),
        (STUDIO, 'Studio'),
        (TOWNHOUSE, 'Townhouse'),
        (ROOM, 'Single Room'),
    ]

    # Listing status choices
    AVAILABLE = 'available'
    RENTED = 'rented'
    PENDING = 'pending'

    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (RENTED, 'Rented'),
        (PENDING, 'Pending'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='properties'
    )

    # Basic information
    title = models.CharField(max_length=255)
    description = models.TextField()
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES,
        default=APARTMENT
    )

    # Pricing
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Monthly rent price"
    )
    deposit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        help_text="Security deposit required"
    )

    # Location
    address = models.CharField(max_length=500, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, default='USA')
    zip_code = models.CharField(max_length=20, blank=True)

    # Keep location for backward compatibility
    location = models.CharField(max_length=255, blank=True)

    # Property details
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        help_text="Number of bathrooms (e.g., 1.5, 2.0)"
    )
    square_feet = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Property size in square feet"
    )

    # Amenities (comma-separated for simplicity)
    amenities = models.TextField(
        blank=True,
        help_text="Comma-separated list (e.g., WiFi, Parking, Gym, Pool)"
    )

    # Availability
    available_from = models.DateField(
        null=True,
        blank=True,
        help_text="Date when property becomes available"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=AVAILABLE
    )

    # Media
    main_image = models.ImageField(
        upload_to='properties/',
        null=True,
        blank=True
    )

    # Flags
    is_active = models.BooleanField(
        default=True,
        help_text="Soft-delete flag"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Featured listing"
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.city}"

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ['-created_at']

    def get_amenities_list(self):
        """Return amenities as a list"""
        return [amenity.strip() for amenity in self.amenities.split(',') if amenity.strip()]


# ---------------------------
# VirtualTour Model
# ---------------------------
class VirtualTour(models.Model):
    # Tour platform choices
    MATTERPORT = 'matterport'
    KUULA = 'kuula'
    CUPIX = 'cupix'
    YOUTUBE = 'youtube'
    CUSTOM = 'custom'

    PLATFORM_CHOICES = [
        (MATTERPORT, 'Matterport'),
        (KUULA, 'Kuula'),
        (CUPIX, 'Cupix'),
        (YOUTUBE, 'YouTube 360'),
        (CUSTOM, 'Custom/Other'),
    ]

    property = models.OneToOneField(
        Property,
        on_delete=models.CASCADE,
        related_name='virtual_tour'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    # 3D Tour URL (main field for embedding tours)
    tour_url = models.URLField(
        max_length=500,
        help_text="URL of the 3D tour (e.g., Matterport, Kuula embed link)",
        default='https://example.com/tour'
    )

    # Platform selection
    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES,
        default=MATTERPORT,
        help_text="Select the 3D tour platform"
    )

    # Optional preview image
    preview_image = models.ImageField(
        upload_to='tours/previews/',
        null=True,
        blank=True,
        help_text="Preview image for the tour"
    )

    # Iframe embed code (optional, for custom platforms)
    iframe_code = models.TextField(
        null=True,
        blank=True,
        help_text="Optional iframe embed code for custom platforms"
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Virtual Tour: {self.title} for {self.property.title}"

    class Meta:
        verbose_name = "Virtual Tour"
        verbose_name_plural = "Virtual Tours"
