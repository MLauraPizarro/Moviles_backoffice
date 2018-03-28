from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from django.http import Http404



class TagList(APIView):
    
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many = True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = TagSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PersonaList(APIView):
    
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many = True)
        return Response(serializer.data)
        
    def post(self):
        pass


class SeguidoresXPersonaList(APIView):
    
    def get(self, request):
        seguidores = SeguidoresXPersona.objects.all()
        serializer = SeguidoresXPersonaSerializer(seguidores, many = True)
        return Response(serializer.data)
        
    def post(self):
        pass


class RecetaList(APIView):
    
    def get(self, request):
        recetas = Receta.objects.all()
        serializer = RecetaSerializer(recetas, many = True)
        return Response(serializer.data)
        
    def post(self):
        pass


class RecetaXPersonaList(APIView):
    
    def get(self, request):
        favoritos = RecetaXPersona.objects.all()
        serializer = RecetaXPersonaSerializer(favoritos, many = True)
        return Response(serializer.data)
        
    def post(self):
        pass


class IngredienteList(APIView):
    
    def get(self, request):
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many = True)
        return Response(serializer.data)
        
    def post(self):
        pass


class CarritoList(APIView):
    
    def get(self, request):
        carritos = Carrito.objects.all()
        serializer = CarritoSerializer(carritos, many = True)
        return Response(serializer.data)
        
    def post(self):
        pass


class NotificacionList(APIView):
    
    def get(self, request):
        notificaciones = Notificacion.objects.all()
        serializer = NotificacionSerializer(notificaciones, many = True)
        return Response(serializer.data)
        
    def post(self):
        pass


class ComentarioList(APIView):
    
    def get(self, request):
        comentarios = Comentario.objects.all()
        serializer = ComentarioSerializer(comentarios, many = True)
        return Response(serializer.data)
        
    def post(self):
        pass



'''

- In website/urls.py:
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stocks/', views.StockList.as_view()),
    url(r'^stocks/(?P<pk>[0-9]+)/', views.StockDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)






- In companies/views.py:

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from django.http import Http404


# Lists all stocks or creates a new one
# stocks/
class StockList(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockDetail(APIView):
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = StockSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = StockSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


if you go to /stocks/<id> you can now post json code in the field and click on post. after that you can go to /stocks/ and see it being there﻿
'''