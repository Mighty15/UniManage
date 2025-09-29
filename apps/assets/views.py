from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AssetCategory, Asset
from .forms import AssetForm
from django.db.models import Q

@login_required
def asset_list(request):
    """
    Muestra una lista de todos los activos, con opciones de filtrado.

    Permite filtrar los activos por nombre, categoría, ubicación y estado.
    También calcula y muestra métricas generales sobre los activos filtrados.
    """
    categories = AssetCategory.objects.all()
    all_assets = Asset.objects.select_related("category").all()

    # Obtener parámetros de filtrado de la solicitud GET.
    name_query = request.GET.get('name', '')
    selected_category_id = request.GET.get('category', '')
    location_query = request.GET.get('location', '')
    status_query = request.GET.get('status', '')

    # Aplicar filtros al queryset de activos.
    if name_query:
        all_assets = all_assets.filter(name__icontains=name_query)
    if selected_category_id:
        all_assets = all_assets.filter(category__id=selected_category_id)
    if location_query:
        all_assets = all_assets.filter(location__icontains=location_query)
    if status_query:
        all_assets = all_assets.filter(status=status_query)

    # El queryset filtrado final.
    activos = all_assets

    # Calcular métricas para las tarjetas basadas en el queryset filtrado.
    total_assets = activos.count()
    available_assets = activos.filter(status="Disponible").count()
    in_use_assets = activos.filter(status="En uso").count()
    maintenance_assets = activos.filter(status="En mantenimiento").count()

    context = {
        "activos": activos,
        "categories": categories,
        "asset_statuses": Asset._meta.get_field('status').choices,
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

@login_required
def asset_create(request):
    """
    Crea un nuevo activo.

    Muestra un formulario para crear un nuevo activo y procesa la
    información enviada.
    """
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asset_list")
    else:
        form = AssetForm()
    return render(request, "assets/asset_form.html", {"form": form, "title": "Crear Activo"})

@login_required
def asset_edit(request, pk):
    """
    Edita un activo existente.

    Muestra un formulario pre-rellenado para editar un activo
    identificado por su clave primaria (pk).
    """
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == "POST":
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect("asset_list")
    else:
        form = AssetForm(instance=asset)
    return render(request, "assets/asset_form.html", {"form": form, "title": "Editar Activo"})

@login_required
def asset_delete(request, pk):
    """
    Elimina un activo existente.

    Pide confirmación antes de eliminar un activo identificado por su
    clave primaria (pk).
    """
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == "POST":
        asset.delete()
        return redirect("asset_list")
    return render(request, "assets/asset_confirm_delete.html", {"asset": asset})
