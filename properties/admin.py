from django.contrib import admin
from .models import Property, VirtualTour


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'property_type', 'city', 'price', 'bedrooms',
        'bathrooms', 'status', 'is_featured', 'is_active',
        'owner', 'created_at'
    )
    list_filter = (
        'property_type', 'status', 'is_active', 'is_featured',
        'bedrooms', 'bathrooms', 'city', 'state', 'country',
        'created_at'
    )
    search_fields = (
        'title', 'description', 'address', 'city',
        'owner__username', 'owner__email'
    )
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active', 'is_featured', 'status')
    list_per_page = 25
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('owner', 'title', 'description', 'property_type')
        }),
        ('Pricing', {
            'fields': ('price', 'deposit')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'country', 'zip_code', 'location')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'square_feet', 'amenities')
        }),
        ('Media', {
            'fields': ('main_image',)
        }),
        ('Availability', {
            'fields': ('status', 'available_from')
        }),
        ('Flags', {
            'fields': ('is_active', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        """Optimize queryset with select_related"""
        qs = super().get_queryset(request)
        return qs.select_related('owner')


@admin.register(VirtualTour)
class VirtualTourAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'property', 'platform', 'is_active',
        'created_at', 'updated_at'
    )
    list_filter = ('platform', 'is_active', 'created_at')
    search_fields = (
        'title', 'description', 'property__title',
        'property__city'
    )
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active',)
    list_per_page = 25
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('property', 'title', 'description')
        }),
        ('Tour Details', {
            'fields': ('tour_url', 'platform', 'preview_image')
        }),
        ('Custom Embed', {
            'fields': ('iframe_code',),
            'classes': ('collapse',),
            'description': 'Optional: Provide custom iframe code for embedding'
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        """Optimize queryset with select_related"""
        qs = super().get_queryset(request)
        return qs.select_related('property', 'property__owner')
