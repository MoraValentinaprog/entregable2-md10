from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Post

class PostListView(ListView):
    """Vista para listar todas las publicaciones."""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Filtra posts publicados hasta la fecha actual y los ordena de forma descendente."""
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    """Vista para mostrar el detalle de una publicación específica."""
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    """Vista para crear una nueva publicación. Requiere estar logueado."""
    model = Post
    fields = ['title', 'content', 'published_date', 'author', 'tags']
    template_name = 'blog/post_form.html'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    """Vista para editar una publicación existente. Requiere estar logueado."""
    model = Post
    fields = ['title', 'content', 'published_date', 'author', 'tags']
    template_name = 'blog/post_form.html'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para eliminar una publicación. Requiere estar logueado."""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
