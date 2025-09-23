from django.conf import settings
from django.utils import timezone
from django.db import models

class Loan(models.Model):
    asset = models.ForeignKey("assets.Asset", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ("Activo", "Activo"),
        ("Devuelto", "Devuelto"),
    ])

    def __str__(self):
        return f"{self.asset.name} → {self.user.username}"
