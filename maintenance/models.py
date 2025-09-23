from django.db import models
from assets.models import Asset

class Maintenance(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)  # Activo que recibe mantenimiento
    description = models.TextField()                           # Detalle del mantenimiento
    date = models.DateField(auto_now_add=True)                 # Fecha automática
    performed_by = models.CharField(max_length=100)            # Técnico o responsable
    status = models.CharField(
        max_length=20,
        choices=[('Pendiente', 'Pendiente'),
                 ('En proceso', 'En proceso'),
                 ('Completado', 'Completado')],
        default='Pendiente'
    )

    def __str__(self):
        return f"{self.asset.name} - {self.status} ({self.date})"
