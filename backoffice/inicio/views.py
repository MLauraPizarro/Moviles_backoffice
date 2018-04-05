
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from django.http import HttpResponse
from django.template import loader


def privacyPolicy(request):
    return render(request,'privacy.html')


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PersonaView(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class SeguidoresXPersonaView(viewsets.ModelViewSet):
    queryset = SeguidoresXPersona.objects.all()
    serializer_class = SeguidoresXPersonaSerializer

class RecetaView(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class RecetaXPersonaView(viewsets.ModelViewSet):
    queryset = RecetaXPersona.objects.all()
    serializer_class = RecetaXPersonaSerializer

class IngredienteView(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class CarritoView(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class NotificacionView(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class ComentarioView(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer



