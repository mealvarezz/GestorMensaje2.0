from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
   path('mensajes/', views.ver_mensajes, name='ver_mensajes'),
    path('buscar/', views.buscar_mensaje, name='buscar_mensaje'),
    path('eliminar/<int:mensaje_id>/', views.eliminar_mensaje, name='eliminar_mensaje'),
    path('crear/', views.crear_mensaje, name='crear_mensaje'),
]








