from django.urls import path,include
from . import views
from rest_framework import routers
<<<<<<< HEAD
from django.conf.urls.static import static
from django.conf import settings
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> f2486a7aa69b803cc2bf874d8154fdc588c0cca6

router = routers.DefaultRouter()
router.register('tag',views.TagView)
router.register('persona',views.PersonaView)
router.register('ingrediente',views.IngredienteView)
router.register('notificacion',views.NotificacionView)
router.register('comentario',views.ComentarioView)
router.register('seguidor',views.SeguidoresXPersonaView)
router.register('carrito',views.CarritoView)
router.register('receta',views.RecetaView)
router.register('favorito',views.RecetaXPersonaView)



urlpatterns = [
    path('',include(router.urls)),
    path('privatePolicy/',views.privacyPolicy,name = 'privacy'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

