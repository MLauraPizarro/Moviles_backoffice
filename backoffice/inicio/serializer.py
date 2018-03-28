from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Persona
        fields = '__all__'    
    
class SeguidoresXPersonaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SeguidoresXPersona
        fields = '__all__'

class RecetaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Receta
        fields = '__all__'    

class RecetaXPersonaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RecetaXPersona
        fields = '__all__'    

class IngredienteSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Ingrediente
        fields = '__all__'  

class CarritoSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Carrito
        fields = '__all__'  

class NotificacionSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Notificacion
        fields = '__all__'  

class ComentarioSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Comentario
        fields = '__all__'