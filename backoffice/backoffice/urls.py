from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework .urlpatterns import format_suffix_patterns
from inicio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tag/', views.TagList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)