from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

class Author(models.Model):
    """Modelo que representa al autor de las publicaciones del blog."""
    name = models.CharField(
        max_length=100, 
        verbose_name="Nombre completo", 
        help_text="Nombre y apellido del autor de forma obligatoria."
    )
    email = models.EmailField(
        unique=True, 
        verbose_name="Correo electrónico", 
        help_text="Dirección de email única e irrepetible para el autor."
    )

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.name

class Tag(models.Model):
    """Modelo que representa las etiquetas o categorías de clasificación."""
    name = models.CharField(
        max_length=30, 
        unique=True, 
        verbose_name="Nombre de la etiqueta", 
        help_text="Palabra clave única para agrupar publicaciones."
    )

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return self.name

class Post(models.Model):
    """Modelo principal que almacena el contenido y las relaciones de cada publicación."""
    title = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título descriptivo de la publicación (mínimo 5 caracteres)."
    )
    content = models.TextField(
        verbose_name="Contenido", 
        help_text="Cuerpo de texto principal del artículo."
    )
    published_date = models.DateTimeField(
        verbose_name="Fecha de publicación", 
        help_text="Fecha y hora en la que se hace público el artículo."
    )
    
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Autor",
        help_text="Autor que redactó la publicación."
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="posts",
        blank=True,
        verbose_name="Etiquetas",
        help_text="Etiquetas vinculadas. Este campo es opcional para permitir flexibilidad."
    )

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Retorna la URL canónica para visualizar esta publicación en detalle."""
        return reverse('post_detail', args=[str(self.id)])

    def clean(self):
        """Validación personalizada a nivel de modelo para el título de la publicación."""
        if self.title and len(self.title) < 5:
            raise ValidationError({
                'title': 'El título es demasiado corto. Debe contener al menos 5 caracteres.'
            })

