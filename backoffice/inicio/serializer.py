import base64, uuid
from django.core.files.base import ContentFile

from rest_framework import serializers
from .models import *




# Custom image field - handles base 64 encoded images
class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        
        if isinstance(data, str) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,') # format ~= data:image/X,
            ext = format.split('/')[-1] # guess file extension
            id = uuid.uuid4()
            data = ContentFile(base64.b64decode(imgstr), name = id.urn[9:] + '.' + ext)
        return super(Base64ImageField, self).to_internal_value(data)

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    foto = Base64ImageField(required = False,
        max_length = None, use_url = True,
    )
    
    class Meta:
        model = Persona
        fields = ("id", 'nombre', 'correo', 'contrasena','descripcion','foto','url' ) 
        
    
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