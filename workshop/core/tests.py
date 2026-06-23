from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Documental

class DocumentalModelTests(TestCase):
    """Casos de prueba para verificar la integridad del catálogo."""
    
    def test_creacion_documental(self):
        """Verifica que el modelo guarde correctamente los datos básicos."""
        doc = Documental.objects.create(
            titulo="Planeta Tierra",
            tematica="Naturaleza",
            anio_estreno=2006
        )
        self.assertEqual(doc.titulo, "Planeta Tierra")

    def test_anio_futuro_invalido(self):
        """Verifica que el método clean bloquee años de estreno futuros."""
        anio_invalido = timezone.now().year + 5
        doc = Documental(
            titulo="Viaje al Futuro",
            tematica="Ciencia",
            anio_estreno=anio_invalido
        )
        with self.assertRaises(ValidationError):
            doc.clean()