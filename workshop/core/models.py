from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

class Documental(models.Model):
    """Modelo que representa un documental dentro del catálogo general del proyecto."""
    titulo = models.CharField(
        max_length=200, 
        verbose_name="Título del documental",
        help_text="Ingrese el nombre completo de la producción cinematográfica o serie."
    )
    tematica = models.CharField(
        max_length=100, 
        verbose_name="Temática principal",
        help_text="Categoría o género del documental (ej: Deportes, Historia)."
    )
    anio_estreno = models.IntegerField(
        verbose_name="Año de estreno",
        help_text="Año en el que la producción fue lanzada oficialmente."
    )

    class Meta:
        verbose_name = "Documental"
        verbose_name_plural = "Documentales"

    def __str__(self):
        return f"{self.titulo} ({self.anio_estreno})"

    def get_absolute_url(self):
        """Retorna la URL canónica para acceder al detalle de este documental."""
        return reverse('documental_detalle', args=[str(self.id)])

    def clean(self):
        """Validación personalizada: El año de estreno no puede ser posterior al año en curso."""
        from django.utils import timezone
        anio_actual = timezone.now().year
        if self.anio_estreno and self.anio_estreno > anio_actual:
            raise ValidationError({
                'anio_estreno': f'El año de estreno no puede ser mayor al año actual ({anio_actual}).'
            })

