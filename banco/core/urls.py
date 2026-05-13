from django.urls import path
from . import views  # views en inglés

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('panel/', views.panel, name='panel'),
    path('cuenta/crear/', views.crear_cuenta, name='crear_cuenta'),
    path('transferencia/', views.realizar_transferencia, name='transferencia'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]