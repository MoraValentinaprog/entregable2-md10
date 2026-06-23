from django.contrib import admin
from .models import Author, Tag, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Configuración avanzada del panel para Autores."""
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Configuración avanzada del panel para Etiquetas."""
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Configuración avanzada del panel para Publicaciones."""
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content', 'author__name')
    date_hierarchy = 'published_date'
    filter_horizontal = ('tags',)
