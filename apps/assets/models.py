from django.db import models

class AssetCategory(models.Model):
    """
    Representa una categoría para los activos.
    
    Ejemplos: Computadores, Impresoras, Proyectores.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """Devuelve el nombre de la categoría."""
        return self.name


class Asset(models.Model):
    """
    Representa un activo individual en el inventario.
    
    Cada activo tiene un nombre, una categoría, una ubicación y un estado.
    También registra cuándo fue creado y actualizado.
    """
    name = models.CharField(max_length=100)
    category = models.ForeignKey(AssetCategory, on_delete=models.CASCADE, related_name="assets")
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ("Disponible", "Disponible"),
        ("En uso", "En uso"),
        ("En mantenimiento", "En mantenimiento"),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Devuelve el nombre del activo."""
        return self.name
