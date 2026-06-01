```markdown
![Texto alternativo](https://github.com/user-attachments/assets/6965211b-8ccd-4084-9759-f2c92697f52c" />
)
# 🏦 BANCO DIGITAL - SISTEMA BANCARIO CON DJANGO

**Nombre del Proyecto:** Sistema Bancario  
**Materia:** Implementa Base De Datos Relaciones En Sistema de Información  
**Profesor:** Romero Hernandez Jose Christian  
**Fecha de Entrega:** Jueves 28 de Mayo del 2026  

**Integrantes:**  
- Arista Flores Karla Gissel  
- Arrez Guzman Eikoo Mizrrain  
- Gonzalez Limon Kimberly  
- Perez Torres Angel Geovany  
- Reynosa Duran Esmeralda  
- Medina Alatorre Guillermo Esteban  

---

## 📋 ÍNDICE

1. [Introducción](#1-introducción)
2. [Desarrollo](#2-desarrollo)
   - 2.1 Configuración del proyecto (settings.py)
   - 2.2 Modelos y relaciones (models.py)
   - 2.3 URLs (urls.py)
   - 2.4 Formularios (forms.py)
   - 2.5 Vistas (views.py)
   - 2.6 Panel de administración (admin.py)
   - 2.7 Plantillas (templates)
   - 2.8 CRUD en el panel de administración
   - 2.9 Integración de componentes (algoritmo)
3. [Sprints del desarrollo](#3-sprints-del-desarrollo)
4. [Conclusiones](#4-conclusiones)

---

## 1. INTRODUCCIÓN

### 1.1 Contexto del proyecto

**Banco Digital** es una aplicación web desarrollada con el framework Django 5 que simula las operaciones fundamentales de un sistema bancario moderno. Este proyecto nace como una solución tecnológica para demostrar cómo las aplicaciones web pueden gestionar información financiera de forma segura, eficiente y escalable, utilizando bases de datos relacionales y buenas prácticas de desarrollo.

En la actualidad, los sistemas bancarios en línea son una necesidad fundamental para los usuarios que buscan comodidad, rapidez y seguridad en la gestión de su dinero. Este proyecto emula esas funcionalidades principales, permitiendo a los usuarios realizar operaciones bancarias básicas sin necesidad de acudir a una sucursal física. Es ideal como proyecto de portafolio, base para productos reales o material educativo sobre Django.

### 1.2 Objetivos del sistema

- **Gestionar usuarios**: Permitir el registro, autenticación y administración de clientes bancarios con información personal y foto de perfil.
- **Administrar cuentas bancarias**: Facilitar la creación, consulta y gestión de cuentas con diferentes tipos (Ahorro, Corriente, Nómina, Inversión).
- **Realizar transferencias**: Implementar un sistema de transferencias entre cuentas con validaciones de saldo y seguridad.
- **Recargar saldo**: Ofrecer una opción sencilla para que los usuarios puedan añadir fondos a sus cuentas.
- **Visualizar movimientos**: Mostrar un historial claro y actualizado de todas las transacciones realizadas.
- **Demostrar relaciones complejas**: Implementar relaciones uno a muchos (1:N) y muchos a muchos (N:M) en una base de datos relacional.

### 1.3 Funcionalidades principales

- Registrarse con foto de perfil (credencial bancaria)
- Iniciar y cerrar sesión de forma segura
- Crear cuentas bancarias (Ahorro, Corriente, Nómina, Inversión)
- Consultar dashboard con saldo total y últimos movimientos
- Realizar transferencias entre cuentas con validaciones
- Recargar saldo directamente desde la página web
- Editar perfil (datos personales y foto)
- Explorar cuentas públicas con búsqueda, filtros y paginación

### 1.4 Arquitectura técnica

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.13+ | Lenguaje principal |
| Django | 5.2+ | Framework web |
| SQLite | - | Base de datos relacional |
| Pillow | 10.3+ | Manejo de imágenes |
| HTML5/CSS3 | - | Interfaz de usuario (CSS puro) |

### 1.5 Estructura del proyecto

```
Banco Digital/
├── banco/
│   ├── settings.py
│   └── urls.py
├── core/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/core/
│       ├── base.html
│       ├── inicio.html
│       ├── registro.html
│       ├── iniciar_sesion.html
│       ├── panel.html
│       ├── crear_cuenta.html
│       ├── transferencia.html
│       ├── editar_perfil.html
│       └── recargar.html
├── media/
└── db.sqlite3
```

### 1.6 Relaciones de base de datos implementadas

| Relación | Tipo | Explicación |
|----------|------|-------------|
| Usuario → Cuenta | 1:N | Un usuario tiene muchas cuentas |
| Cuenta ↔ TipoCuenta | N:M | Una cuenta tiene varios tipos |
| Transacción ↔ Cuenta | N:M (vía DetalleTransaccion) | Una transferencia involucra dos cuentas |

### 1.7 Panel de administración

El sistema incluye un panel `/admin/` personalizado en español que permite:
- CRUD completo de usuarios, cuentas, tipos de cuenta, transacciones
- Filtros y búsqueda avanzada
- Gestión de permisos

### 1.8 Alcance y limitaciones

**Alcance:** Funciona localmente, soporta múltiples usuarios, operaciones en tiempo real.  
**Limitaciones:** Sin pasarelas de pago reales, sin notificaciones, seguridad básica.

### 1.9 Público objetivo

Desarrolladores web, instituciones educativas, pequeñas empresas.

---

## 2. DESARROLLO

### 2.1 Configuración del proyecto (settings.py)
´´´python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
´´´
### 2.2 Modelos y relaciones (models.py)

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return self.username

class TipoCuenta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cuota_mensual = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    ESTADOS = [
        ('activa', 'Activa'),
        ('bloqueada', 'Bloqueada'),
        ('cerrada', 'Cerrada'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_cuenta = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activa')

    propietario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='cuentas'
    )

    tipos_cuenta = models.ManyToManyField(
        TipoCuenta,
        related_name='cuentas'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero_cuenta} - ${self.saldo}"

class Transaccion(models.Model):
    TIPOS_TRANSACCION = [
        ('deposito', 'Depósito'),
        ('retiro', 'Retiro'),
        ('transferencia', 'Transferencia'),
        ('pago', 'Pago'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_transaccion = models.CharField(max_length=20, choices=TIPOS_TRANSACCION)
    descripcion = models.TextField(blank=True)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='transacciones'
    )

    cuentas = models.ManyToManyField(
        Cuenta,
        through='DetalleTransaccion',
        related_name='transacciones'
    )

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_transaccion} - {self.fecha}"

    @property
    def monto_total(self):
        return sum(detalle.monto for detalle in self.detalletransaccion_set.all())

class DetalleTransaccion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)

    monto = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        unique_together = ('transaccion', 'cuenta')

    @property
    def monto_absoluto(self):
        return abs(self.monto)

    def __str__(self):
        return f"{self.transaccion.id} - {self.cuenta.numero_cuenta}: ${self.monto}"

![Diagrama ER](https://github.com/user-attachments/assets/640c59b7-4889-4922-a5a5-9f1144cf89d9)

### 2.3 URLs (urls.py)

**Banco/urls.py:**
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


**Core/urls.py:**
from django.urls import path
from . import views  
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('panel/', views.panel, name='panel'),
    path('cuenta/crear/', views.crear_cuenta, name='crear_cuenta'),
    path('transferencia/', views.realizar_transferencia, name='transferencia'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('recargar/<uuid:cuenta_id>/', views.recargar_saldo, name='recargar'),
]

### 2.4 Formularios (forms.py)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Cuenta
class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=False, label="Teléfono")
    foto_perfil = forms.ImageField(required=False, label="Foto de perfil")   
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefono', 'foto_perfil', 'password1', 'password2')
class FormularioCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['numero_cuenta', 'tipos_cuenta']
        widgets = {
            'tipos_cuenta': forms.CheckboxSelectMultiple()
        }


class FormularioActualizarUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefono', 'direccion', 'foto_perfil')


### 2.5 Vistas (views.py)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Sum
from django.core.paginator import Paginator
from decimal import Decimal

from .models import Usuario, Cuenta, TipoCuenta, Transaccion, DetalleTransaccion
from .forms import FormularioRegistro, FormularioCuenta, FormularioActualizarUsuario

def inicio(request):
    busqueda = request.GET.get('q')
    tipo_cuenta_id = request.GET.get('tipo_cuenta')
    
    cuentas = Cuenta.objects.select_related('propietario').prefetch_related('tipos_cuenta').all()
    
    if busqueda:
        cuentas = cuentas.filter(
            Q(numero_cuenta__icontains=busqueda) |
            Q(propietario__username__icontains=busqueda)
        )
    
    if tipo_cuenta_id:
        cuentas = cuentas.filter(tipos_cuenta__id=tipo_cuenta_id)
    
    paginador = Paginator(cuentas, 6)
    numero_pagina = request.GET.get('page')
    pagina_objetos = paginador.get_page(numero_pagina)
    
    tipos_cuenta = TipoCuenta.objects.all()
    
    return render(request, 'core/inicio.html', {
        'pagina_objetos': pagina_objetos,
        'tipos_cuenta': tipos_cuenta
    })

def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            messages.success(request, 'Registro exitoso. Bienvenido al Banco Digital.')
            return redirect('inicio')
    else:
        formulario = FormularioRegistro()
    
    return render(request, 'core/registro.html', {'formulario': formulario})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        
        if usuario:
            login(request, usuario)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'core/iniciar_sesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

@login_required
def panel(request):
    cuentas = Cuenta.objects.filter(propietario=request.user)
    saldo_total = cuentas.aggregate(Sum('saldo'))['saldo__sum'] or 0
    transacciones_recientes = Transaccion.objects.filter(usuario=request.user).order_by('-fecha')[:5]
    
    return render(request, 'core/panel.html', {
        'cuentas': cuentas,
        'saldo_total': saldo_total,
        'transacciones_recientes': transacciones_recientes
    })

@login_required
def crear_cuenta(request):
    if request.method == 'POST':
        formulario = FormularioCuenta(request.POST)
        if formulario.is_valid():
            cuenta = formulario.save(commit=False)
            cuenta.propietario = request.user
            cuenta.saldo = 0
            cuenta.save()
            formulario.save_m2m()
            messages.success(request, 'Cuenta creada exitosamente')
            return redirect('panel')
    else:
        formulario = FormularioCuenta()
    
    return render(request, 'core/crear_cuenta.html', {'formulario': formulario})

@login_required
def realizar_transferencia(request):
    if request.method == 'POST':
        cuenta_origen_id = request.POST.get('cuenta_origen')
        numero_cuenta_destino = request.POST.get('cuenta_destino')
        monto = Decimal(request.POST.get('monto'))
        
        cuenta_origen = get_object_or_404(Cuenta, id=cuenta_origen_id, propietario=request.user)
        
        try:
            cuenta_destino = Cuenta.objects.get(numero_cuenta=numero_cuenta_destino)
        except Cuenta.DoesNotExist:
            messages.error(request, 'La cuenta destino no existe')
            return redirect('transferencia')
        
        if monto <= 0:
            messages.error(request, 'El monto debe ser mayor a cero')
        elif cuenta_origen.saldo < monto:
            messages.error(request, 'Saldo insuficiente')
        elif cuenta_origen.id == cuenta_destino.id:
            messages.error(request, 'No puedes transferir a la misma cuenta')
        else:
            transaccion = Transaccion.objects.create(
                usuario=request.user,
                tipo_transaccion='transferencia',
                descripcion=f"Transferencia a {cuenta_destino.numero_cuenta}"
            )
            
            DetalleTransaccion.objects.create(
                transaccion=transaccion,
                cuenta=cuenta_origen,
                monto=-monto
            )
            
            DetalleTransaccion.objects.create(
                transaccion=transaccion,
                cuenta=cuenta_destino,
                monto=monto
            )
            
            cuenta_origen.saldo -= monto
            cuenta_origen.save()
            cuenta_destino.saldo += monto
            cuenta_destino.save()
            
            messages.success(request, f'Transferencia de ${monto} realizada con éxito')
            return redirect('panel')
    
    cuentas = Cuenta.objects.filter(propietario=request.user, estado='activa')
    return render(request, 'core/transferencia.html', {'cuentas': cuentas})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario = FormularioActualizarUsuario(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Perfil actualizado correctamente')
            return redirect('panel')
    else:
        formulario = FormularioActualizarUsuario(instance=request.user)
    
    return render(request, 'core/editar_perfil.html', {'formulario': formulario})

@login_required
def recargar_saldo(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id, propietario=request.user)
    
    if request.method == 'POST':
        monto = Decimal(request.POST.get('monto'))
        
        if monto <= 0:
            messages.error(request, 'El monto debe ser mayor a cero')
        else:
            transaccion = Transaccion.objects.create(
                usuario=request.user,
                tipo_transaccion='deposito',
                descripcion=f"Recarga a cuenta {cuenta.numero_cuenta}"
            )
            
            DetalleTransaccion.objects.create(
                transaccion=transaccion,
                cuenta=cuenta,
                monto=monto
            )
            
            cuenta.saldo += monto
            cuenta.save()
            
            messages.success(request, f'¡Recarga exitosa! Se añadieron ${monto} a tu cuenta')
            return redirect('panel')
    
    return render(request, 'core/recargar.html', {'cuenta': cuenta})
### 2.6 Panel de administración (admin.py)
from django.contrib import admin
from .models import Usuario, TipoCuenta, Cuenta, Transaccion, DetalleTransaccion

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'telefono', 'fecha_registro', 'activo')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'telefono')
    readonly_fields = ('id', 'date_joined', 'last_login')
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('username', 'email', 'telefono', 'direccion', 'foto_perfil')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Información del Sistema', {
            'fields': ('id', 'date_joined', 'last_login'),
            'classes': ('collapse',)
        }),
    )
    
    def telefono(self, obj):
        return obj.telefono or 'No registrado'
    telefono.short_description = 'Teléfono'
    
    def fecha_registro(self, obj):
        return obj.date_joined.strftime('%d/%m/%Y %H:%M')
    fecha_registro.short_description = 'Fecha de Registro'
    
    def activo(self, obj):
        return obj.is_active
    activo.short_description = 'Activo'
    activo.boolean = True

@admin.register(TipoCuenta)
class TipoCuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tasa_interes', 'cuota_mensual', 'descripcion_corta')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('id',)
    
    fieldsets = (
        ('Información del Tipo de Cuenta', {
            'fields': ('nombre', 'descripcion', 'tasa_interes', 'cuota_mensual')
        }),
        ('Información del Sistema', {
            'fields': ('id',),
            'classes': ('collapse',)
        }),
    )
    
    def nombre(self, obj):
        return obj.nombre
    nombre.short_description = 'Nombre del Tipo'
    
    def tasa_interes(self, obj):
        return f"{obj.tasa_interes}%"
    tasa_interes.short_description = 'Tasa de Interés'
    
    def cuota_mensual(self, obj):
        return f"${obj.cuota_mensual}"
    cuota_mensual.short_description = 'Cuota Mensual'
    
    def descripcion_corta(self, obj):
        return obj.descripcion[:50] + '...' if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('numero_cuenta', 'propietario', 'saldo', 'estado', 'tipos_cuenta', 'fecha_creacion')
    list_filter = ('estado', 'tipos_cuenta', 'fecha_creacion')
    search_fields = ('numero_cuenta', 'propietario__username', 'propietario__email')
    filter_horizontal = ('tipos_cuenta',)
    readonly_fields = ('id', 'fecha_creacion')
    
    fieldsets = (
        ('Información de la Cuenta', {
            'fields': ('numero_cuenta', 'propietario', 'tipos_cuenta', 'saldo', 'estado')
        }),
        ('Información del Sistema', {
            'fields': ('id', 'fecha_creacion'),
            'classes': ('collapse',),
        }),
    )
    
    def numero_cuenta(self, obj):
        return obj.numero_cuenta
    numero_cuenta.short_description = 'Número de Cuenta'
    
    def propietario(self, obj):
        return f"{obj.propietario.username} ({obj.propietario.email})"
    propietario.short_description = 'Propietario'
    
    def saldo(self, obj):
        return f"${obj.saldo:,.2f}"
    saldo.short_description = 'Saldo Actual'
    
    def estado(self, obj):
        estados = {
            'activa': 'Activa',
            'bloqueada': 'Bloqueada',
            'cerrada': 'Cerrada'
        }
        return estados.get(obj.estado, obj.estado)
    estado.short_description = 'Estado'
    
    def tipos_cuenta(self, obj):
        return ', '.join([t.nombre for t in obj.tipos_cuenta.all()])
    tipos_cuenta.short_description = 'Tipos de Cuenta'
    
    def fecha_creacion(self, obj):
        return obj.fecha_creacion.strftime('%d/%m/%Y %H:%M')
    fecha_creacion.short_description = 'Fecha de Creación'

class DetalleTransaccionInline(admin.TabularInline):
    model = DetalleTransaccion
    extra = 1
    readonly_fields = ('id',)
    fields = ('cuenta', 'monto')

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('id_corto', 'tipo_transaccion', 'cliente', 'fecha', 'monto_total')
    list_filter = ('tipo_transaccion', 'fecha', 'usuario')
    search_fields = ('usuario__username', 'usuario__email', 'descripcion')
    readonly_fields = ('id', 'fecha')
    inlines = [DetalleTransaccionInline]
    
    fieldsets = (
        ('Información de la Transacción', {
            'fields': ('tipo_transaccion', 'usuario', 'descripcion')
        }),
        ('Información del Sistema', {
            'fields': ('id', 'fecha'),
            'classes': ('collapse',),
        }),
    )
    
    def id_corto(self, obj):
        return str(obj.id).split('-')[0]
    id_corto.short_description = 'ID'
    
    def tipo_transaccion(self, obj):
        tipos = {
            'deposito': 'Depósito',
            'retiro': 'Retiro',
            'transferencia': 'Transferencia',
            'pago': 'Pago'
        }
        return tipos.get(obj.tipo_transaccion, obj.tipo_transaccion)
    tipo_transaccion.short_description = 'Tipo de Transacción'
    
    def cliente(self, obj):
        return f"{obj.usuario.username} ({obj.usuario.email})"
    cliente.short_description = 'Cliente'
    
    def fecha(self, obj):
        return obj.fecha.strftime('%d/%m/%Y %H:%M:%S')
    fecha.short_description = 'Fecha y Hora'
    
    def monto_total(self, obj):
        total = sum(detalle.monto for detalle in obj.detalletransaccion_set.all())
        return f"${abs(total):,.2f}"
    monto_total.short_description = 'Monto Total'

@admin.register(DetalleTransaccion)
class DetalleTransaccionAdmin(admin.ModelAdmin):
    list_display = ('transaccion_id', 'cuenta', 'monto', 'monto_absoluto')
    list_filter = ('transaccion__tipo_transaccion', 'cuenta__estado')
    search_fields = ('transaccion__id', 'cuenta__numero_cuenta', 'cuenta__propietario__username')
    readonly_fields = ('id',)
    
    fieldsets = (
        ('Información del Detalle', {
            'fields': ('transaccion', 'cuenta', 'monto')
        }),
        ('Información del Sistema', {
            'fields': ('id',),
            'classes': ('collapse',),
        }),
    )
    
    def transaccion_id(self, obj):
        return str(obj.transaccion.id).split('-')[0]
    transaccion_id.short_description = 'ID Transacción'
    
    def cuenta(self, obj):
        return f"{obj.cuenta.numero_cuenta} ({obj.cuenta.propietario.username})"
    cuenta.short_description = 'Cuenta'
    
    def monto(self, obj):
        if obj.monto < 0:
            return f"-${abs(obj.monto):,.2f}"
        return f"+${obj.monto:,.2f}"
    monto.short_description = 'Monto'
    
    def monto_absoluto(self, obj):
        return f"${abs(obj.monto):,.2f}"
    monto_absoluto.short_description = 'Monto Absoluto'
### 2.7 Plantillas (templates)

Se desarrollaron **9 plantillas HTML** con CSS puro:

| # | Template | Función |
|---|----------|---------|
| 1 | `base.html` | Plantilla base (navbar, estilos) |
| 2 | `inicio.html` | Listado público de cuentas |
| 3 | `registro.html` | Formulario de registro |
| 4 | `iniciar_sesion.html` | Formulario de login |
| 5 | `panel.html` | Dashboard del usuario |
| 6 | `crear_cuenta.html` | Formulario para abrir cuenta |
| 7 | `transferencia.html` | Formulario de transferencia |
| 8 | `editar_perfil.html` | Formulario de edición de perfil |
| 9 | `recargar.html` | Formulario de recarga de saldo |

### 2.8 CRUD en el panel de administración

- **Crear:** Usuarios, tipos de cuenta, cuentas, transacciones
- **Leer:** Listados con filtros y búsqueda
- **Actualizar:** Edición de cualquier campo
- **Eliminar:** Borrado con confirmación y cascada

### 2.9 Integración de componentes (algoritmo)

```
ALGORITMO DEL BANCO DIGITAL

PASO 1: Configuración (settings.py)
PASO 2: Modelos con relaciones 1:N y N:M (models.py)
PASO 3: Admin personalizado (admin.py)
PASO 4: Formularios (forms.py)
PASO 5: URLs (urls.py)
PASO 6: Vistas con lógica (views.py)
PASO 7: Templates HTML (templates/)
PASO 8: Flujo de petición → URL → Vista → Modelo → Template → Respuesta

Ejemplo transferencia:
URL /transferencia/ → views.realizar_transferencia() → valida datos → crea Transaccion y DetalleTransaccion → actualiza saldos → redirige a panel.html
```

## 3. SPRINTS DEL DESARROLLO

### 🚀 SPRINT 1 — Setup + Modelado Base

**Objetivo:**
- Proyecto Django funcionando
- App core (banco)
- Modelos con relaciones 1:N y N:M
- Admin operativo

**Modelos creados:**
- `Usuario` (con foto_perfil, teléfono, dirección)
- `TipoCuenta` (nombre, tasa_interés, cuota_mensual)
- `Cuenta` (numero_cuenta, saldo, estado)
- `Transaccion` (tipo, descripción, fecha)
- `DetalleTransaccion` (monto, tabla intermedia)

**Relaciones implementadas:**
| Relación | Tipo |
|----------|------|
| Usuario → Cuenta | 1:N |
| Cuenta ↔ TipoCuenta | N:M |
| Transacción ↔ Cuenta | N:M (vía DetalleTransaccion) |

### 🚀 SPRINT 2 — Autenticación + UI Base

**Objetivo:**
- Sistema de registro y login
- Layout base con CSS puro
- Navbar dinámica
- Home pública

**Templates creados:** base.html, inicio.html, registro.html, iniciar_sesion.html

### 🚀 SPRINT 3 — Gestión de Cuentas + Dashboard

**Objetivo:**
- CRUD de cuentas bancarias
- Dashboard personal para clientes
- Control de permisos

**Templates creados:** panel.html, crear_cuenta.html

**Dashboard features:**
- Credencial bancaria con foto de perfil
- Saldo total de todas las cuentas
- Listado de cuentas del usuario
- Últimos movimientos recientes

### 🚀 SPRINT 4 — Transferencias + Movimientos

**Objetivo:**
- Sistema de transferencias entre cuentas
- Validación de saldo suficiente
- Registro de transacciones

**Template creado:** transferencia.html

**Lógica de transferencia:**
- Monto mayor a cero
- Saldo suficiente
- Cuenta destino existe
- No transferir a misma cuenta

### 🚀 SPRINT 5 — Optimización + UX + Recarga + Edición

**Objetivo:**
- Búsqueda y filtros
- Paginación
- Edición de perfil
- Recarga de saldo desde página web

**Templates creados:** editar_perfil.html, recargar.html

**Mejoras implementadas:**
- Búsqueda con Q
- Filtros por tipo de cuenta
- Paginación (6 cuentas por página)
- Optimización ORM (select_related, prefetch_related)

---

## 📁 LISTA COMPLETA DE TEMPLATES (9 archivos)

```
core/templates/core/
├── base.html           # Plantilla base con navegación y estilos
├── inicio.html         # Listado público de cuentas
├── registro.html       # Formulario de registro
├── iniciar_sesion.html # Formulario de login
├── panel.html          # Dashboard del usuario
├── crear_cuenta.html   # Formulario para crear cuenta
├── transferencia.html  # Formulario para transferir
├── editar_perfil.html  # Formulario para editar perfil
└── recargar.html       # Formulario para recargar saldo
```

## 📊 Diagrama de Relaciones

```
Usuario (1) ──────→ (N) Cuenta
                       │
                       │ (N:M)
                       ↓
                 TipoCuenta

Transacción (N) ←──→ (N) Cuenta (a través de DetalleTransaccion)
```

## 📦 Instalación rápida

```bash
git clone https://github.com/anitasusnanita-jpg/Proyecto-Banco-Digital.git
cd Proyecto-Banco-Digital
python -m venv venv
venv\Scripts\activate
pip install django pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 🧪 Flujo de prueba completo

| Paso | Acción | Template involucrado |
|------|--------|---------------------|
| 1 | `/registro/` | registro.html |
| 2 | `/admin/` | (admin de Django) |
| 3 | `/cuenta/crear/` | crear_cuenta.html |
| 4 | `/panel/` | panel.html |
| 5 | Click en "Recargar" | recargar.html |
| 6 | `/transferencia/` | transferencia.html |
| 7 | `/perfil/editar/` | editar_perfil.html |

## ✅ Resumen de Sprints

| Sprint | Nombre | Templates | Entregables |
|--------|--------|-----------|-------------|
| 1 | Setup + Modelado Base | 0 | Modelos 1:N y N:M |
| 2 | Autenticación + UI Base | 4 | base, inicio, registro, login |
| 3 | Gestión de Cuentas | 2 | panel, crear_cuenta |
| 4 | Transferencias | 1 | transferencia |
| 5 | Optimización + Recarga | 2 | editar_perfil, recargar |
| **Total** | | **9** | **Sistema completo** |

---

 4. CONCLUSIONES

El desarrollo de **Banco Digital** ha demostrado ser un ejercicio completo y exitoso en la construcción de una aplicación web funcional utilizando el framework Django. A lo largo de 5 sprints, se implementó un sistema bancario simulado que integra autenticación de usuarios, gestión de cuentas, transferencias, recargas de saldo, edición de perfil y un dashboard financiero personalizado.

Se cumplieron todos los objetivos planteados inicialmente: modelado de datos con relaciones 1:N y N:M, panel de administración funcional, sistema de registro y login con foto de perfil, navegación dinámica, CRUD de cuentas, transferencias seguras con validación de saldo, paginación, búsqueda con filtros y edición de perfil. El proyecto cuenta con 9 templates completamente integrados y una interfaz responsive con CSS puro.

Las decisiones técnicas adoptadas resultaron acertadas. El uso de **UUID como clave primaria** mejora la seguridad al evitar la enumeración de recursos. La tabla intermedia **DetalleTransaccion** permite mayor flexibilidad para futuros tipos de operaciones. La optimización con **select_related y prefetch_related** reduce drásticamente el número de consultas a la base de datos. Las validaciones del lado del servidor garantizan la integridad de las operaciones financieras.

**Banco Digital** es un proyecto funcional, extensible y bien documentado que sirve como base sólida para agregar nuevas características como notificaciones por correo, reportes en PDF, gráficos de gastos, autenticación con redes sociales o integración con pasarelas de pago reales. Es ideal para portafolio profesional, material educativo o punto de partida para un producto financiero real.

