from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Import login_required
from assets.models import AssetCategory, Asset
from loans.models import Loan # Import Loan model
from maintenance.models import Maintenance # Import Maintenance model

@login_required # Protect this view
def dashboard(request):
    categories = AssetCategory.objects.all()
    data = []

    # General asset information
    total_assets = Asset.objects.count()
    available_assets = Asset.objects.filter(status="Disponible").count()
    in_use_assets = Asset.objects.filter(status="En uso").count()
    maintenance_assets = Asset.objects.filter(status="En mantenimiento").count()
    total_categories = AssetCategory.objects.count()

    for category in categories:
        total = Asset.objects.filter(category=category).count()
        disponibles = Asset.objects.filter(category=category, status="Disponible").count()
        en_uso = Asset.objects.filter(category=category, status="En uso").count()
        mantenimiento = Asset.objects.filter(category=category, status="En mantenimiento").count()

        if total > 0:
            disponibles_pct = round((disponibles / total) * 100, 2)
            en_uso_pct = round((en_uso / total) * 100, 2)
            # Calculate remaining_pct to ensure the sum is 100% for the progress bar
            remaining_pct = round(100 - (disponibles_pct + en_uso_pct), 2)
            # Ensure remaining_pct is not negative due to rounding
            if remaining_pct < 0:
                remaining_pct = 0
            mantenimiento_pct = round((mantenimiento / total) * 100, 2) # Still pass the actual maintenance_pct
        else:
            disponibles_pct = en_uso_pct = mantenimiento_pct = remaining_pct = 0

        data.append({
            "categoria": category.name,
            "total": total,
            "disponibles": disponibles,
            "en_uso": en_uso,
            "mantenimiento": mantenimiento,
            "disponibles_pct": disponibles_pct,
            "en_uso_pct": en_uso_pct,
            "mantenimiento_pct": mantenimiento_pct, # This is the actual percentage
            "remaining_pct_for_bar": remaining_pct, # This is for the progress bar width
        })

    # Get last 10 loans and maintenances
    last_10_loans = Loan.objects.select_related('asset', 'user').order_by('-loan_date')[:10]
    last_10_maintenances = Maintenance.objects.select_related('asset').order_by('-created_at')[:10]

    # Data for Asset Status Distribution Pie Chart
    asset_status_labels = ["Disponible", "En uso", "En mantenimiento"]
    asset_status_data = [available_assets, in_use_assets, maintenance_assets]

    # Removed data for Assets by Category Bar Chart

    context = {
        "data": data,
        "total_assets": total_assets,
        "available_assets": available_assets,
        "in_use_assets": in_use_assets,
        "maintenance_assets": maintenance_assets,
        "total_categories": total_categories,
        "last_10_loans": last_10_loans,
        "last_10_maintenances": last_10_maintenances,
        "asset_status_labels": asset_status_labels,
        "asset_status_data": asset_status_data,
        # Removed category_labels and assets_by_category_data from context
    }

    return render(request, "dashboard.html", context)