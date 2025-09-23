from django.shortcuts import render
from .models import AssetCategory, Asset

def dashboard(request):
    categories = AssetCategory.objects.all()
    data = []

    for category in categories:
        total = Asset.objects.filter(category=category).count()
        disponibles = Asset.objects.filter(category=category, status="Disponible").count()
        en_uso = Asset.objects.filter(category=category, status="En uso").count()
        mantenimiento = Asset.objects.filter(category=category, status="En mantenimiento").count()

        # evitar división por cero
        if total > 0:
            disponibles_pct = (disponibles / total) * 100
            en_uso_pct = (en_uso / total) * 100
            mantenimiento_pct = (mantenimiento / total) * 100
        else:
            disponibles_pct = en_uso_pct = mantenimiento_pct = 0

        data.append({
            "categoria": category.name,
            "total": total,
            "disponibles": disponibles,
            "en_uso": en_uso,
            "mantenimiento": mantenimiento,
            "disponibles_pct": disponibles_pct,
            "en_uso_pct": en_uso_pct,
            "mantenimiento_pct": mantenimiento_pct,
        })

    return render(request, "dashboard.html", {"data": data})
