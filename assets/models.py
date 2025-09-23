from django.db import models

class AssetCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(AssetCategory, on_delete=models.CASCADE, related_name="assets")
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ("Disponible", "Disponible"),
        ("En uso", "En uso"),
        ("En mantenimiento", "En mantenimiento"),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Nuevo campo para tracking de actividad

    def __str__(self):
        return self.name