from django.contrib import admin
from .models import Maintenance

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('asset', 'status', 'date', 'performed_by')
    list_filter = ('status', 'date')
    search_fields = ('asset__name', 'performed_by')
