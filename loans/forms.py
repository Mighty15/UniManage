from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ["asset", "user", "return_date", "status"]  # ❌ quita loan_date
