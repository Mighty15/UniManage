from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('asset', 'user', 'loan_date', 'return_date', 'status')
    list_filter = ('status', 'loan_date')
    search_fields = ('asset__name', 'user__username')
