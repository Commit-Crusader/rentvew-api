from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Property, VirtualTour
from .forms import PropertyForm, VirtualTourForm

# ---------------------------
# List all properties (public)
# ---------------------------
def property_list(request):
    properties = Property.objects.filter(is_active=True)
    return render(request, 'properties/property_list.html', {'properties': properties})

# ---------------------------
# Create new property (landlord only)
# ---------------------------
@login_required  # ensures user is authenticated
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.owner = request.user  # assign current logged-in user
            prop.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/property_form.html', {'form': form})

# ---------------------------
# Add virtual tour for a property (owner only)
# ---------------------------
@login_required
def virtual_tour_create(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    # Only allow the property owner to add a tour
    if request.user != property_obj.owner:
        return render(request, 'properties/error.html', {
            'message': 'You do not have permission to add a virtual tour to this property.'
        })

    if request.method == 'POST':
        form = VirtualTourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.property = property_obj
            tour.save()
            return redirect('property_list')
    else:
        form = VirtualTourForm()
    return render(request, 'properties/virtualtour_form.html', {'form': form, 'property': property_obj})
