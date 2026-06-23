from django.contrib import admin
from .models import Documental

@admin.register(Documental)
class DocumentalAdmin(admin.ModelAdmin):
    """Configuración del panel para el catálogo de Documentales."""
    list_display = ('titulo', 'tematica', 'anio_estreno')
    list_filter = ('tematica', 'anio_estreno')
    search_fields = ('titulo',)
