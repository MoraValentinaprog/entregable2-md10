from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Documental

class DocumentalModelTest(TestCase):
    """Pruebas unitarias para garantizar la integridad del modelo Documental."""

    def setUp(self):
        # Configuramos un objeto válido en memoria antes de cada prueba
        self.documental = Documental(
            titulo="El Ritmo de la Tierra",
            tematica="Naturaleza",
            anio_estreno=2020
        )

    def test_creacion_documental_valido(self):
        """Verifica que un documental con datos correctos pase la validación."""
        self.documental.full_clean()  # Forza la ejecución del método clean()
        self.documental.save()
        self.assertEqual(Documental.objects.count(), 1)

    def test_anio_estreno_futuro_invalido(self):
        """Verifica que el sistema rechace años de estreno superiores al actual."""
        anio_futuro = timezone.now().year + 1
        self.documental.anio_estreno = anio_futuro
        
        # El test pasa a verde solo si el sistema lanza correctamente el ValidationError
        with self.assertRaises(ValidationError):
            self.documental.full_clean()