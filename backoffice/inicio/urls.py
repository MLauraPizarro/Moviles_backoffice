from django.urls import path,include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

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
    
]

