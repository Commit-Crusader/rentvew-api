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
