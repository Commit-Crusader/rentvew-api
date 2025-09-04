from django.contrib import admin
from .models import Property, VirtualTour

# ---------------------------
# Inline setup: show VirtualTour inside Property admin
# ---------------------------
class VirtualTourInline(admin.StackedInline):
    model = VirtualTour
    extra = 0  # don’t show extra empty forms
    can_delete = True


# ---------------------------
# Property Admin
# ---------------------------
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'location', 'is_active', 'created_at')
    list_filter = ('is_active', 'location', 'created_at')
    search_fields = ('title', 'location', 'description')
    inlines = [VirtualTourInline]  # Allow managing VirtualTour inside Property


# ---------------------------
# VirtualTour Admin
# ---------------------------
@admin.register(VirtualTour)
class VirtualTourAdmin(admin.ModelAdmin):
    list_display = ('title', 'property', 'created_at')
    search_fields = ('title', 'description')
