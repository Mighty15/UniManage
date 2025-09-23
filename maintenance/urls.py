from django.urls import path
from . import views

urlpatterns = [
    path("", views.maintenance_list, name="maintenance_list"),
    path("nuevo/", views.maintenance_create, name="maintenance_create"),
    path("<int:pk>/editar/", views.maintenance_edit, name="maintenance_edit"),
    path("<int:pk>/eliminar/", views.maintenance_delete, name="maintenance_delete"),
]
