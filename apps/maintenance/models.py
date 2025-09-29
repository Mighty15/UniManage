from django.db import models
from apps.assets.models import Asset
from django.utils import timezone

class Maintenance(models.Model):
    """
    Representa una tarea de mantenimiento para un activo.

    Registra el activo que requiere mantenimiento, una descripción del
    trabajo, quién lo realiza, el estado de la tarea y cuándo se creó.
    """
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    description = models.TextField()
    performed_by = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pendiente", "Pendiente"),
            ("En proceso", "En proceso"),
            ("Finalizado", "Finalizado"),
        ],
    )
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        """Devuelve una representación en string del mantenimiento."""
        return f"{self.asset.name} - {self.status} ({self.created_at.date()})"