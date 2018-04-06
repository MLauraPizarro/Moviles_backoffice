from django.db import models

# Create your models here.



class Persona(models.Model):
    nombre = models.CharField(max_length = 50)
    correo = models.CharField(max_length = 50)
    contrasena = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 50,blank=True)
    foto = models.FileField(blank=True)
  

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
    foto = models.ImageField(upload_to = 'recetas')
    publico = models.BooleanField()
    costo = models.CharField(max_length = 50)
    publicacion = models.DateTimeField(auto_now_add=True)
    calificacion = models.FloatField()
    cantidad_calificaciones = models.IntegerField()

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
    publicacion = models.DateTimeField(auto_now_add=True)
    




