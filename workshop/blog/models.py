from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    """Modelo que representa al autor de las publicaciones del blog."""
    name = models.CharField(
        max_length=100, 
        verbose_name="Nombre completo", 
        help_text="Nombre y apellido del autor."
    )
    email = models.EmailField(
        unique=True, 
        verbose_name="Correo electrónico", 
        help_text="Dirección de email única del autor."
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
        verbose_name="Nombre de la etiqueta", 
        help_text="Categoría para clasificar publicaciones."
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
        validators=[MinLengthValidator(5, message="El título debe tener al menos 5 caracteres.")],
        verbose_name="Título",
        help_text="Título de la publicación (mínimo 5 caracteres)."
    )
    content = models.TextField(
        verbose_name="Contenido", 
        help_text="Cuerpo de texto de la publicación."
    )
    published_date = models.DateTimeField(
        verbose_name="Fecha de publicación", 
        help_text="Fecha y hora exactas de publicación."
    )
    
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Autor",
        help_text="Autor asociado a esta publicación."
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="posts",
        verbose_name="Etiquetas",
        help_text="Etiquetas vinculadas a esta publicación."
    )

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.title
