from django.contrib import admin
from .models import Asset, AssetCategory

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'status', 'created_at', 'updated_at')
    list_filter = ('category', 'status')
    search_fields = ('name', 'location')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status', 'location')  # Permite edición rápida

@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)