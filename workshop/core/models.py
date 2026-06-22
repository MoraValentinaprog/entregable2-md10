from django.db import models

class Documental(models.Model):
    titulo = models.CharField(max_length=200)
    tematica = models.CharField(max_length=100)
    anio_estreno = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.anio_estreno})"

