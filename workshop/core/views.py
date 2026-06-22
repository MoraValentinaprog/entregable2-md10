from django.shortcuts import render
from .models import Documental

def lista_documentales(request):
    documentales = Documental.objects.all()
    return render(request, 'core/lista_documentales.html', {'documentales': documentales})
