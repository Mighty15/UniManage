from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required # Import login_required
from .models import Maintenance
from .forms import MaintenanceForm
from assets.models import Asset # Import the Asset model (still needed for other views or if we re-add asset filter later)

# 📌 Lista de mantenimientos
@login_required # Protect this view
def maintenance_list(request):
    # Start with all maintenances
    all_maintenances = Maintenance.objects.select_related("asset").all()

    # Get filter parameters from GET request
    status_query = request.GET.get('status', '')

    # Apply filters
    if status_query:
        all_maintenances = all_maintenances.filter(status=status_query)

    mantenimientos = all_maintenances # The filtered queryset

    # Calculate metrics for the cards based on the filtered queryset
    pendientes = mantenimientos.filter(status="Pendiente").count()
    en_progreso = mantenimientos.filter(status="En proceso").count()
    completados = mantenimientos.filter(status="Finalizado").count()

    context = {
        "mantenimientos": mantenimientos,
        "status_query": status_query,
        "pendientes": pendientes,
        "en_progreso": en_progreso,
        "completados": completados,
        "maintenance_statuses": Maintenance._meta.get_field('status').choices, # Pass status choices to template
    }
    return render(request, "maintenance/maintenance_list.html", context)

# 📌 Crear mantenimiento
@login_required # Protect this view
def maintenance_create(request):
    if request.method == "POST":
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("maintenance_list")
    else:
        form = MaintenanceForm()
    return render(request, "maintenance/maintenance_form.html", {"form": form})

# 📌 Editar mantenimiento
@login_required # Protect this view
def maintenance_edit(request, pk):
    mantenimiento = get_object_or_404(Maintenance, pk=pk)
    if request.method == "POST":
        form = MaintenanceForm(request.POST, instance=mantenimiento)
        if form.is_valid():
            form.save()
            return redirect("maintenance_list")
    else:
        form = MaintenanceForm(instance=mantenimiento)
    return render(request, "maintenance/maintenance_form.html", {"form": form})

# 📌 Eliminar mantenimiento
@login_required # Protect this view
def maintenance_delete(request, pk):
    mantenimiento = get_object_or_404(Maintenance, pk=pk)
    if request.method == "POST":
        mantenimiento.delete()
        return redirect("maintenance_list")
    return render(request, "maintenance/maintenance_confirm_delete.html", {"mantenimiento": mantenimiento})