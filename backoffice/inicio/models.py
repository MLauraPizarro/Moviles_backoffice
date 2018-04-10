from django.db import models
from django.utils.safestring import mark_safe
import base64
import os

from datetime import datetime
from imgurpython import ImgurClient



client_id = '8e93376c5991784'
client_secret = 'fe404cefcac0b78fbcb31224437b7262ad2b1ec1'

access_token = '5ba02ffdb021bb2b282af917a289b431e7fd65c3'
refresh_token = 'f8ea8ae27d89ab6ca592959ec311e09cb66c2e4e'

client = ImgurClient(client_id, client_secret)
client.set_user_auth(access_token, refresh_token)



def upload_image(client,image_path,album,nombre):
    album = None
    """
    Uploads and image to imgur
    """
    BASE = os.path.dirname(os.path.abspath(__file__))
    config = {
        'album': album,
        'name': nombre,
        'title': nombre,
        'description': 'Imagen: {0}'.format(datetime.now())
    }

    print('Uploading image...')
    image = client.upload_from_path(os.path.join(BASE, image_path), config=config, anon=False)
    print("Done")
    print()

    return image

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length = 50)
    correo = models.CharField(max_length = 50)
    contrasena = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 50,blank=True)
    foto = models.FileField(upload_to = 'personas',blank=True)
    url = models.TextField(max_length = 250, blank=True, editable = False)
    __original_foto = None


    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.foto != self.__original_foto and self.foto != None:
            super(Persona, self).save()
            nombre = ""
            nombre = (os.path.basename(self.foto.name))
            path = "../media_root/personas/" + nombre.replace(" ", "_")
            print (nombre.replace(" ", "_"))

            image = upload_image(client,path,"Persona",nombre)
            self.url = format(image['link'])
            print("Image was posted!")
            print("You can find the image here: {0}".format(image['link']))
            self.__original_foto = self.foto
            self.save()
        else:
            super(Persona, self).save()

    def __init__(self, *args, **kwargs):
        super(Persona, self).__init__(*args, **kwargs)
        self.__original_foto = self.foto

    def __str__(self):
        return self.nombre
  

class SeguidoresXPersona(models.Model):
    seguidor = models.ForeignKey(Persona, on_delete = models.CASCADE, related_name='seguidor') 
    seguido = models.ForeignKey(Persona, on_delete = models.CASCADE, related_name='seguido')


class Receta(models.Model):
    autor = models.ForeignKey(Persona, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 50)
    procedimiento = models.CharField(max_length = 100)
    notas = models.CharField(max_length = 100,blank=True)
    dificultad = models.CharField(max_length = 10)
    tiempo = models.TimeField(auto_now_add=True)
    porciones = models.IntegerField()
    publico = models.BooleanField()
    costo = models.CharField(max_length = 50)
    publicacion = models.DateTimeField(auto_now_add=True)
    calificacion = models.FloatField()
    cantidad_calificaciones = models.IntegerField()
    foto = models.FileField(upload_to = 'recetas',blank=True)
    url = models.TextField(max_length = 250, blank=True, editable = False)
    __original_foto = None


    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.foto != self.__original_foto and self.foto != None:
            super(Receta, self).save()
            nombre = ""
            nombre = (os.path.basename(self.foto.name))
            path = "../media_root/recetas/" + nombre.replace(" ", "_")
            print (nombre.replace(" ", "_"))

            image = upload_image(client,path,"Receta",nombre)
            self.url = format(image['link'])
            print("Image was posted!")
            print("You can find the image here: {0}".format(image['link']))
            self.__original_foto = self.foto
            self.save()
        else:
            super(Receta, self).save()

    def __init__(self, *args, **kwargs):
        super(Receta, self).__init__(*args, **kwargs)
        self.__original_foto = self.foto

    def __str__(self):
        return self.nombre

class Tag(models.Model):
    nombre = models.CharField(max_length = 20)
    #receta = models.ForeignKey(Receta, on_delete = models.CASCADE)

class RecetaXPersona(models.Model):
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete = models.CASCADE)



class Ingrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete = models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete = models.CASCADE)

class Notificacion(models.Model):
    dueno = models.ForeignKey(Persona, on_delete = models.CASCADE, related_name='dueno')
    motivo = models.CharField(max_length = 50)
    hora = models.DateTimeField()
    persona_externa = models.ForeignKey(Persona, on_delete = models.CASCADE, related_name='externo')
    receta = models.ForeignKey(Receta, on_delete = models.CASCADE)



class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete = models.CASCADE)
    comentario = models.CharField(max_length=250)
    publicacion = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    




