from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
    """
    Formulario para la creación y edición de activos.
    
    Utiliza el modelo `Asset` y personaliza los widgets para que
    tengan una clase CSS estándar para el estilo.
    """
    class Meta:
        model = Asset
        fields = ["name", "category", "location", "status"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }