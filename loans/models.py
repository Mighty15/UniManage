from django.db import models
from django.contrib.auth.models import User
from assets.models import Asset

class Loan(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)  # Activo prestado
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # Usuario que recibe el activo
    loan_date = models.DateField(auto_now_add=True)             # Fecha de préstamo
    return_date = models.DateField(null=True, blank=True)       # Fecha de devolución
    status = models.CharField(
        max_length=20,
        choices=[('Activo', 'Activo'),
                 ('Devuelto', 'Devuelto')],
        default='Activo'
    )

    def __str__(self):
        return f"{self.asset.name} → {self.user.username} ({self.status})"

