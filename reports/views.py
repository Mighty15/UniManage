from django.shortcuts import render
from assets.models import Asset, AssetCategory
from loans.models import Loan
from maintenance.models import Maintenance
from django.utils.timezone import now

def dashboard(request):
    total_assets = Asset.objects.count()
    categories = AssetCategory.objects.all()

    # Construir datos de categorías
    category_data = []
    for category in categories:
        total = Asset.objects.filter(category=category).count()
        disponibles = Asset.objects.filter(category=category, status="Disponible").count()
        en_uso = Asset.objects.filter(category=category, status="En uso").count()
        en_mantenimiento = Asset.objects.filter(category=category, status="En mantenimiento").count()
        
        category_data.append({
            "name": category.name,
            "total": total,
            "disponibles": disponibles,
            "en_uso": en_uso,
            "en_mantenimiento": en_mantenimiento,
            "porcentaje": round((total / total_assets) * 100, 2) if total_assets > 0 else 0
        })

    context = {
        "total_assets": total_assets,
        "available_assets": Asset.objects.filter(status="Disponible").count(),
        "in_use_assets": Asset.objects.filter(status="En uso").count(),
        "maintenance_assets": Asset.objects.filter(status="En mantenimiento").count(),
        "active_loans": Loan.objects.filter(status="Activo").count(),
        "maintenance_pending": Maintenance.objects.filter(status="En proceso").count(),
        "current_date": now().strftime("%Y-%m-%d"),
        "categories": category_data,
    }

    return render(request, "reports/dashboard.html", context)
