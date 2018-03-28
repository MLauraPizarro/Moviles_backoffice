from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework .urlpatterns import format_suffix_patterns
from inicio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tag/', views.TagList.as_view()),
    path('persona/', views.PersonaList.as_view()),
    path('ingrediente/', views.IngredienteList.as_view()),
    path('notificacion/', views.NotificacionList.as_view()),
    path('comentario/', views.ComentarioList.as_view()),
    path('seguidor/', views.SeguidoresXPersonaList.as_view()),
    path('carrito/', views.CarritoList.as_view()),
    path('receta/', views.RecetaList.as_view()),
    path('favorito/', views.RecetaXPersonaList.as_view()),
    path('tag/(?P<pk>[0-9]+)/',views.TagDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)