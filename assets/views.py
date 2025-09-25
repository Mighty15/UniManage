from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required # Import login_required
from .models import AssetCategory, Asset
from .forms import AssetForm
from django.db.models import Q


# ✅ Lista de activos
@login_required # Protect this view
def asset_list(request):
    categories = AssetCategory.objects.all() # Get all categories for the filter dropdown
    all_assets = Asset.objects.select_related("category").all() # Start with all assets

    # Get filter parameters from GET request
    name_query = request.GET.get('name', '')
    selected_category_id = request.GET.get('category', '')
    location_query = request.GET.get('location', '')
    status_query = request.GET.get('status', '')

    # Apply filters
    if name_query:
        all_assets = all_assets.filter(name__icontains=name_query)
    if selected_category_id:
        all_assets = all_assets.filter(category__id=selected_category_id)
    if location_query:
        all_assets = all_assets.filter(location__icontains=location_query)
    if status_query:
        all_assets = all_assets.filter(status=status_query)

    activos = all_assets # The filtered queryset

    # Calculate metrics for the cards based on the filtered queryset
    total_assets = activos.count()
    available_assets = activos.filter(status="Disponible").count()
    in_use_assets = activos.filter(status="En uso").count()
    maintenance_assets = activos.filter(status="En mantenimiento").count()

    context = {
        "activos": activos,
        "categories": categories, # For category filter dropdown
        "asset_statuses": Asset._meta.get_field('status').choices, # Pass status choices to template
        "name_query": name_query,
        "selected_category_id": selected_category_id,
        "location_query": location_query,
        "status_query": status_query,
        "total_assets": total_assets,
        "available_assets": available_assets,
        "in_use_assets": in_use_assets,
        "maintenance_assets": maintenance_assets,
    }
    return render(request, "assets/asset_list.html", context)

@login_required # Protect this view
def asset_create(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asset_list")
    else:
        form = AssetForm()
    return render(request, "assets/asset_form.html", {"form": form, "title": "Crear Activo"})

@login_required # Protect this view
def asset_edit(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == "POST":
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect("asset_list")
    else:
        form = AssetForm(instance=asset)
    return render(request, "assets/asset_form.html", {"form": form, "title": "Editar Activo"})

@login_required # Protect this view
def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == "POST":
        asset.delete()
        return redirect("asset_list")
    return render(request, "assets/asset_confirm_delete.html", {"asset": asset})