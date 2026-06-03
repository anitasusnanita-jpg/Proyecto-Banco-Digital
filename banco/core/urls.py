# banco/core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 🏠 Rutas Principales y de Autenticación
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),  # 👈 Ajustado a tu plantilla
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),    # 👈 ¡AQUÍ ESTÁ LA SOLUCIÓN! Cambiado de 'logout' a 'cerrar_sesion'
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    
    # 📊 Panel de Control y Operaciones Bancarias
    path('panel/', views.panel, name='panel'),
    path('cuenta/crear/', views.crear_cuenta, name='crear_cuenta'),
    path('transferencia/', views.realizar_transferencia, name='transferencia'),
    path('cuenta/recargar/<int:cuenta_id>/', views.recargar_saldo, name='recargar'),
    
    # ========================================================================
    # 🤖 CANAL DE COMUNICACIÓN ASÍNCRONA DEL CHATBOT (FETCH API)
    # ========================================================================
    path('asistente/chat/', views.asistente_chat_api, name='asistente_chat_api'),
]