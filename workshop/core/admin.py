from django.contrib import admin
from .models import Categoria, Documental

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Configuración del panel de administración para el modelo Categoria."""
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Documental)
class DocumentalAdmin(admin.ModelAdmin):
    """Configuración del panel de administración para el modelo Documental."""
    # Columnas que se mostrarán en la lista principal
    list_display = ('titulo', 'tematica', 'anio_estreno')
    # Barra de búsqueda por título y temática
    search_fields = ('titulo', 'tematica')
    # Panel de filtros lateral derecho
    list_filter = ('tematica', 'anio_estreno')
    # Orden predeterminado (por año de estreno descendente, luego alfabéticamente)
    ordering = ('-anio_estreno', 'titulo')
