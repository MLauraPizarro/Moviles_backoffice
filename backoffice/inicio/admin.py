from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(Tag)

class PersonaAdmin(admin.ModelAdmin):
    readonly_fields=('url',)


admin.site.register(Persona,PersonaAdmin)

admin.site.register(SeguidoresXPersona)

admin.site.register(Receta)
admin.site.register(RecetaXPersona)

admin.site.register(Ingrediente)
admin.site.register(Carrito)
admin.site.register(Notificacion)
admin.site.register(Comentario)



