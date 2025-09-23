from django.db import models
from assets.models import Asset
from django.utils import timezone

class Maintenance(models.Model):
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
        return f"{self.asset.name} - {self.status} ({self.created_at.date()})"
