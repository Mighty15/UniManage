from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    """
    Formulario para la creación y edición de préstamos.
    
    Utiliza el modelo `Loan` y define los campos que se mostrarán en el
    formulario. El campo `loan_date` se gestiona automáticamente.
    """
    class Meta:
        model = Loan
        fields = ["asset", "user", "return_date", "status"]