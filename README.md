```markdown
<img width="148" height="148" alt="image" src="https://github.com/user-attachments/assets/fe661a68-f706-4f80-807b-e7b8545a5e5e" />

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

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%;"><span></span>INSTALLED_APPS <span style="color: #333">=</span> [
    <span style="background-color: #FFF0F0">&#39;django.contrib.admin&#39;</span>,
    <span style="background-color: #FFF0F0">&#39;django.contrib.auth&#39;</span>,
    <span style="background-color: #FFF0F0">&#39;django.contrib.contenttypes&#39;</span>,
    <span style="background-color: #FFF0F0">&#39;django.contrib.sessions&#39;</span>,
    <span style="background-color: #FFF0F0">&#39;django.contrib.messages&#39;</span>,
    <span style="background-color: #FFF0F0">&#39;django.contrib.staticfiles&#39;</span>,
    <span style="background-color: #FFF0F0">&#39;core&#39;</span>,
]
</pre></div>

### 2.2 Modelos y relaciones (models.py)

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%;"><span></span><span style="color: #080; font-weight: bold">import</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">uuid</span>
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.db</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> models
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.contrib.auth.models</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> AbstractUser


<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">Usuario</span>(AbstractUser):
    <span style="color: #007020">id</span> <span style="color: #333">=</span> models<span style="color: #333">.</span>UUIDField(primary_key<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>, default<span style="color: #333">=</span>uuid<span style="color: #333">.</span>uuid4, editable<span style="color: #333">=</span><span style="color: #080; font-weight: bold">False</span>)
    telefono <span style="color: #333">=</span> models<span style="color: #333">.</span>CharField(max_length<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">15</span>, blank<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>)
    direccion <span style="color: #333">=</span> models<span style="color: #333">.</span>TextField(blank<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>)
    foto_perfil <span style="color: #333">=</span> models<span style="color: #333">.</span>ImageField(upload_to<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;fotos_perfil/&#39;</span>, blank<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>, null<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>)


    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">__str__</span>(<span style="color: #007020">self</span>):
        <span style="color: #080; font-weight: bold">return</span> <span style="color: #007020">self</span><span style="color: #333">.</span>username


<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">TipoCuenta</span>(models<span style="color: #333">.</span>Model):
    <span style="color: #007020">id</span> <span style="color: #333">=</span> models<span style="color: #333">.</span>UUIDField(primary_key<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>, default<span style="color: #333">=</span>uuid<span style="color: #333">.</span>uuid4, editable<span style="color: #333">=</span><span style="color: #080; font-weight: bold">False</span>)
    nombre <span style="color: #333">=</span> models<span style="color: #333">.</span>CharField(max_length<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">100</span>)
    descripcion <span style="color: #333">=</span> models<span style="color: #333">.</span>TextField(blank<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>)
    tasa_interes <span style="color: #333">=</span> models<span style="color: #333">.</span>DecimalField(max_digits<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">5</span>, decimal_places<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">2</span>, default<span style="color: #333">=</span><span style="color: #60E; font-weight: bold">0.00</span>)
    cuota_mensual <span style="color: #333">=</span> models<span style="color: #333">.</span>DecimalField(max_digits<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">10</span>, decimal_places<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">2</span>, default<span style="color: #333">=</span><span style="color: #60E; font-weight: bold">0.00</span>)
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">__str__</span>(<span style="color: #007020">self</span>):
        <span style="color: #080; font-weight: bold">return</span> <span style="color: #007020">self</span><span style="color: #333">.</span>nombre
<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">Cuenta</span>(models<span style="color: #333">.</span>Model):
    ESTADOS <span style="color: #333">=</span> [
        (<span style="background-color: #FFF0F0">&#39;activa&#39;</span>, <span style="background-color: #FFF0F0">&#39;Activa&#39;</span>),
        (<span style="background-color: #FFF0F0">&#39;bloqueada&#39;</span>, <span style="background-color: #FFF0F0">&#39;Bloqueada&#39;</span>),
        (<span style="background-color: #FFF0F0">&#39;cerrada&#39;</span>, <span style="background-color: #FFF0F0">&#39;Cerrada&#39;</span>),
    ]
    <span style="color: #007020">id</span> <span style="color: #333">=</span> models<span style="color: #333">.</span>UUIDField(primary_key<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>, default<span style="color: #333">=</span>uuid<span style="color: #333">.</span>uuid4, editable<span style="color: #333">=</span><span style="color: #080; font-weight: bold">False</span>)
    numero_cuenta <span style="color: #333">=</span> models<span style="color: #333">.</span>CharField(max_length<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">20</span>, unique<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>)
    saldo <span style="color: #333">=</span> models<span style="color: #333">.</span>DecimalField(max_digits<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">12</span>, decimal_places<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">2</span>, default<span style="color: #333">=</span><span style="color: #60E; font-weight: bold">0.00</span>)
    estado <span style="color: #333">=</span> models<span style="color: #333">.</span>CharField(max_length<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">10</span>, choices<span style="color: #333">=</span>ESTADOS, default<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;activa&#39;</span>)


    propietario <span style="color: #333">=</span> models<span style="color: #333">.</span>ForeignKey(
        Usuario,
        on_delete<span style="color: #333">=</span>models<span style="color: #333">.</span>CASCADE,
        related_name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;cuentas&#39;</span>
    )


    tipos_cuenta <span style="color: #333">=</span> models<span style="color: #333">.</span>ManyToManyField(
        TipoCuenta,
        related_name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;cuentas&#39;</span>
    )


    fecha_creacion <span style="color: #333">=</span> models<span style="color: #333">.</span>DateTimeField(auto_now_add<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>)


    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">__str__</span>(<span style="color: #007020">self</span>):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;</span><span style="background-color: #EEE">{</span><span style="color: #007020">self</span><span style="color: #333">.</span>numero_cuenta<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0"> - $</span><span style="background-color: #EEE">{</span><span style="color: #007020">self</span><span style="color: #333">.</span>saldo<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>


<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">Transaccion</span>(models<span style="color: #333">.</span>Model):
    TIPOS_TRANSACCION <span style="color: #333">=</span> [
        (<span style="background-color: #FFF0F0">&#39;deposito&#39;</span>, <span style="background-color: #FFF0F0">&#39;Depósito&#39;</span>),
        (<span style="background-color: #FFF0F0">&#39;retiro&#39;</span>, <span style="background-color: #FFF0F0">&#39;Retiro&#39;</span>),
        (<span style="background-color: #FFF0F0">&#39;transferencia&#39;</span>, <span style="background-color: #FFF0F0">&#39;Transferencia&#39;</span>),
        (<span style="background-color: #FFF0F0">&#39;pago&#39;</span>, <span style="background-color: #FFF0F0">&#39;Pago&#39;</span>),
    ]
    <span style="color: #007020">id</span> <span style="color: #333">=</span> models<span style="color: #333">.</span>UUIDField(primary_key<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>, default<span style="color: #333">=</span>uuid<span style="color: #333">.</span>uuid4, editable<span style="color: #333">=</span><span style="color: #080; font-weight: bold">False</span>)
    tipo_transaccion <span style="color: #333">=</span> models<span style="color: #333">.</span>CharField(max_length<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">20</span>, choices<span style="color: #333">=</span>TIPOS_TRANSACCION)
    descripcion <span style="color: #333">=</span> models<span style="color: #333">.</span>TextField(blank<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>)


    usuario <span style="color: #333">=</span> models<span style="color: #333">.</span>ForeignKey(
        Usuario,
        on_delete<span style="color: #333">=</span>models<span style="color: #333">.</span>CASCADE,
        related_name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;transacciones&#39;</span>
    )
    cuentas <span style="color: #333">=</span> models<span style="color: #333">.</span>ManyToManyField(
        Cuenta,
        through<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;DetalleTransaccion&#39;</span>,
        related_name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;transacciones&#39;</span>
    )
    fecha <span style="color: #333">=</span> models<span style="color: #333">.</span>DateTimeField(auto_now_add<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>)
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">__str__</span>(<span style="color: #007020">self</span>):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;</span><span style="background-color: #EEE">{</span><span style="color: #007020">self</span><span style="color: #333">.</span>tipo_transaccion<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0"> - </span><span style="background-color: #EEE">{</span><span style="color: #007020">self</span><span style="color: #333">.</span>fecha<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>
    <span style="color: #555; font-weight: bold">@property</span>
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">monto_total</span>(<span style="color: #007020">self</span>):
        <span style="color: #080; font-weight: bold">return</span> <span style="color: #007020">sum</span>(detalle<span style="color: #333">.</span>monto <span style="color: #080; font-weight: bold">for</span> detalle <span style="color: #000; font-weight: bold">in</span> <span style="color: #007020">self</span><span style="color: #333">.</span>detalletransaccion_set<span style="color: #333">.</span>all())
<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">DetalleTransaccion</span>(models<span style="color: #333">.</span>Model):
    <span style="color: #007020">id</span> <span style="color: #333">=</span> models<span style="color: #333">.</span>UUIDField(primary_key<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>, default<span style="color: #333">=</span>uuid<span style="color: #333">.</span>uuid4, editable<span style="color: #333">=</span><span style="color: #080; font-weight: bold">False</span>)
    transaccion <span style="color: #333">=</span> models<span style="color: #333">.</span>ForeignKey(Transaccion, on_delete<span style="color: #333">=</span>models<span style="color: #333">.</span>CASCADE)
    cuenta <span style="color: #333">=</span> models<span style="color: #333">.</span>ForeignKey(Cuenta, on_delete<span style="color: #333">=</span>models<span style="color: #333">.</span>CASCADE)
    monto <span style="color: #333">=</span> models<span style="color: #333">.</span>DecimalField(max_digits<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">12</span>, decimal_places<span style="color: #333">=</span><span style="color: #00D; font-weight: bold">2</span>)
    <span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">Meta</span>:
        unique_together <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;transaccion&#39;</span>, <span style="background-color: #FFF0F0">&#39;cuenta&#39;</span>)
    <span style="color: #555; font-weight: bold">@property</span>
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">monto_absoluto</span>(<span style="color: #007020">self</span>):
        <span style="color: #080; font-weight: bold">return</span> <span style="color: #007020">abs</span>(<span style="color: #007020">self</span><span style="color: #333">.</span>monto)
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">__str__</span>(<span style="color: #007020">self</span>):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;</span><span style="background-color: #EEE">{</span><span style="color: #007020">self</span><span style="color: #333">.</span>transaccion<span style="color: #333">.</span>id<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0"> - </span><span style="background-color: #EEE">{</span><span style="color: #007020">self</span><span style="color: #333">.</span>cuenta<span style="color: #333">.</span>numero_cuenta<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">: $</span><span style="background-color: #EEE">{</span><span style="color: #007020">self</span><span style="color: #333">.</span>monto<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>
</pre></div>


![Diagrama ER](https://github.com/user-attachments/assets/640c59b7-4889-4922-a5a5-9f1144cf89d9)

### 2.3 URLs (urls.py)

**Banco/urls.py:**
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%;"><span></span><span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.contrib</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> admin
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.urls</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> path, include
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.conf</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> settings
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.conf.urls.static</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> static
urlpatterns <span style="color: #333">=</span> [
    path(<span style="background-color: #FFF0F0">&#39;admin/&#39;</span>, admin<span style="color: #333">.</span>site<span style="color: #333">.</span>urls),
    path(<span style="background-color: #FFF0F0">&#39;&#39;</span>, include(<span style="background-color: #FFF0F0">&#39;core.urls&#39;</span>)),
]
<span style="color: #080; font-weight: bold">if</span> settings<span style="color: #333">.</span>DEBUG:
    urlpatterns <span style="color: #333">+=</span> static(settings<span style="color: #333">.</span>MEDIA_URL, document_root<span style="color: #333">=</span>settings<span style="color: #333">.</span>MEDIA_ROOT)
</pre></div>

**Core/urls.py:**
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%;"><span></span><span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.urls</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> path
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">.</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> views  
urlpatterns <span style="color: #333">=</span> [
    path(<span style="background-color: #FFF0F0">&#39;&#39;</span>, views<span style="color: #333">.</span>inicio, name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;inicio&#39;</span>),
    path(<span style="background-color: #FFF0F0">&#39;registro/&#39;</span>, views<span style="color: #333">.</span>registro, name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;registro&#39;</span>),
    path(<span style="background-color: #FFF0F0">&#39;iniciar-sesion/&#39;</span>, views<span style="color: #333">.</span>iniciar_sesion, name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;iniciar_sesion&#39;</span>),
    path(<span style="background-color: #FFF0F0">&#39;cerrar-sesion/&#39;</span>, views<span style="color: #333">.</span>cerrar_sesion, name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;cerrar_sesion&#39;</span>),
    path(<span style="background-color: #FFF0F0">&#39;panel/&#39;</span>, views<span style="color: #333">.</span>panel, name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;panel&#39;</span>),
    path(<span style="background-color: #FFF0F0">&#39;cuenta/crear/&#39;</span>, views<span style="color: #333">.</span>crear_cuenta, name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;crear_cuenta&#39;</span>),
    path(<span style="background-color: #FFF0F0">&#39;transferencia/&#39;</span>, views<span style="color: #333">.</span>realizar_transferencia, name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;transferencia&#39;</span>),
    path(<span style="background-color: #FFF0F0">&#39;perfil/editar/&#39;</span>, views<span style="color: #333">.</span>editar_perfil, name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;editar_perfil&#39;</span>),
    path(<span style="background-color: #FFF0F0">&#39;recargar/&lt;uuid:cuenta_id&gt;/&#39;</span>, views<span style="color: #333">.</span>recargar_saldo, name<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;recargar&#39;</span>),
]
</pre></div>

### 2.4 Formularios (forms.py)

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%;"><span></span><span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> forms
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.contrib.auth.forms</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> UserCreationForm
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">.models</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> Usuario, Cuenta
<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">FormularioRegistro</span>(UserCreationForm):
    email <span style="color: #333">=</span> forms<span style="color: #333">.</span>EmailField(required<span style="color: #333">=</span><span style="color: #080; font-weight: bold">True</span>)
    telefono <span style="color: #333">=</span> forms<span style="color: #333">.</span>CharField(required<span style="color: #333">=</span><span style="color: #080; font-weight: bold">False</span>, label<span style="color: #333">=</span><span style="background-color: #FFF0F0">&quot;Teléfono&quot;</span>)
    foto_perfil <span style="color: #333">=</span> forms<span style="color: #333">.</span>ImageField(required<span style="color: #333">=</span><span style="color: #080; font-weight: bold">False</span>, label<span style="color: #333">=</span><span style="background-color: #FFF0F0">&quot;Foto de perfil&quot;</span>)   
    <span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">Meta</span>:
        model <span style="color: #333">=</span> Usuario
        fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;username&#39;</span>, <span style="background-color: #FFF0F0">&#39;email&#39;</span>, <span style="background-color: #FFF0F0">&#39;telefono&#39;</span>, <span style="background-color: #FFF0F0">&#39;foto_perfil&#39;</span>, <span style="background-color: #FFF0F0">&#39;password1&#39;</span>, <span style="background-color: #FFF0F0">&#39;password2&#39;</span>)
<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">FormularioCuenta</span>(forms<span style="color: #333">.</span>ModelForm):
    <span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">Meta</span>:
        model <span style="color: #333">=</span> Cuenta
        fields <span style="color: #333">=</span> [<span style="background-color: #FFF0F0">&#39;numero_cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;tipos_cuenta&#39;</span>]
        widgets <span style="color: #333">=</span> {
            <span style="background-color: #FFF0F0">&#39;tipos_cuenta&#39;</span>: forms<span style="color: #333">.</span>CheckboxSelectMultiple()
        }


<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">FormularioActualizarUsuario</span>(forms<span style="color: #333">.</span>ModelForm):
    <span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">Meta</span>:
        model <span style="color: #333">=</span> Usuario
        fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;username&#39;</span>, <span style="background-color: #FFF0F0">&#39;email&#39;</span>, <span style="background-color: #FFF0F0">&#39;telefono&#39;</span>, <span style="background-color: #FFF0F0">&#39;direccion&#39;</span>, <span style="background-color: #FFF0F0">&#39;foto_perfil&#39;</span>)
</pre></div>

### 2.5 Vistas (views.py)
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%;"><span></span><span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.shortcuts</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> render, redirect, get_object_or_404
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.contrib.auth</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> login, authenticate, logout
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.contrib.auth.decorators</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> login_required
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.contrib</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> messages
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.db.models</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> Q, Sum
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.core.paginator</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> Paginator
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">decimal</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> Decimal
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">.models</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> Usuario, Cuenta, TipoCuenta, Transaccion, DetalleTransaccion
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">.forms</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> FormularioRegistro, FormularioCuenta, FormularioActualizarUsuario
<span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">inicio</span>(request):
    busqueda <span style="color: #333">=</span> request<span style="color: #333">.</span>GET<span style="color: #333">.</span>get(<span style="background-color: #FFF0F0">&#39;q&#39;</span>)
    tipo_cuenta_id <span style="color: #333">=</span> request<span style="color: #333">.</span>GET<span style="color: #333">.</span>get(<span style="background-color: #FFF0F0">&#39;tipo_cuenta&#39;</span>)   
    cuentas <span style="color: #333">=</span> Cuenta<span style="color: #333">.</span>objects<span style="color: #333">.</span>select_related(<span style="background-color: #FFF0F0">&#39;propietario&#39;</span>)<span style="color: #333">.</span>prefetch_related(<span style="background-color: #FFF0F0">&#39;tipos_cuenta&#39;</span>)<span style="color: #333">.</span>all()
    <span style="color: #080; font-weight: bold">if</span> busqueda:
        cuentas <span style="color: #333">=</span> cuentas<span style="color: #333">.</span>filter(
            Q(numero_cuenta__icontains<span style="color: #333">=</span>busqueda) <span style="color: #333">|</span>
            Q(propietario__username__icontains<span style="color: #333">=</span>busqueda)        )   
    <span style="color: #080; font-weight: bold">if</span> tipo_cuenta_id:
        cuentas <span style="color: #333">=</span> cuentas<span style="color: #333">.</span>filter(tipos_cuenta__id<span style="color: #333">=</span>tipo_cuenta_id)
    paginador <span style="color: #333">=</span> Paginator(cuentas, <span style="color: #00D; font-weight: bold">6</span>)
    numero_pagina <span style="color: #333">=</span> request<span style="color: #333">.</span>GET<span style="color: #333">.</span>get(<span style="background-color: #FFF0F0">&#39;page&#39;</span>)
    pagina_objetos <span style="color: #333">=</span> paginador<span style="color: #333">.</span>get_page(numero_pagina)
    tipos_cuenta <span style="color: #333">=</span> TipoCuenta<span style="color: #333">.</span>objects<span style="color: #333">.</span>all()   
    <span style="color: #080; font-weight: bold">return</span> render(request, <span style="background-color: #FFF0F0">&#39;core/inicio.html&#39;</span>, {
        <span style="background-color: #FFF0F0">&#39;pagina_objetos&#39;</span>: pagina_objetos,
        <span style="background-color: #FFF0F0">&#39;tipos_cuenta&#39;</span>: tipos_cuenta
    })
<span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">registro</span>(request):
    <span style="color: #080; font-weight: bold">if</span> request<span style="color: #333">.</span>method <span style="color: #333">==</span> <span style="background-color: #FFF0F0">&#39;POST&#39;</span>:
        formulario <span style="color: #333">=</span> FormularioRegistro(request<span style="color: #333">.</span>POST, request<span style="color: #333">.</span>FILES)
        <span style="color: #080; font-weight: bold">if</span> formulario<span style="color: #333">.</span>is_valid():
            usuario <span style="color: #333">=</span> formulario<span style="color: #333">.</span>save()
            login(request, usuario)
            messages<span style="color: #333">.</span>success(request, <span style="background-color: #FFF0F0">&#39;Registro exitoso. Bienvenido al Banco Digital.&#39;</span>)
            <span style="color: #080; font-weight: bold">return</span> redirect(<span style="background-color: #FFF0F0">&#39;inicio&#39;</span>)
    <span style="color: #080; font-weight: bold">else</span>:
        formulario <span style="color: #333">=</span> FormularioRegistro()
     <span style="color: #080; font-weight: bold">return</span> render(request, <span style="background-color: #FFF0F0">&#39;core/registro.html&#39;</span>, {<span style="background-color: #FFF0F0">&#39;formulario&#39;</span>: formulario})
<span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">iniciar_sesion</span>(request):
    <span style="color: #080; font-weight: bold">if</span> request<span style="color: #333">.</span>method <span style="color: #333">==</span> <span style="background-color: #FFF0F0">&#39;POST&#39;</span>:
        username <span style="color: #333">=</span> request<span style="color: #333">.</span>POST<span style="color: #333">.</span>get(<span style="background-color: #FFF0F0">&#39;username&#39;</span>)
        password <span style="color: #333">=</span> request<span style="color: #333">.</span>POST<span style="color: #333">.</span>get(<span style="background-color: #FFF0F0">&#39;password&#39;</span>)
        usuario <span style="color: #333">=</span> authenticate(request, username<span style="color: #333">=</span>username, password<span style="color: #333">=</span>password)       
        <span style="color: #080; font-weight: bold">if</span> usuario:
            login(request, usuario)
            <span style="color: #080; font-weight: bold">return</span> redirect(<span style="background-color: #FFF0F0">&#39;inicio&#39;</span>)
        <span style="color: #080; font-weight: bold">else</span>:
            messages<span style="color: #333">.</span>error(request, <span style="background-color: #FFF0F0">&#39;Usuario o contraseña incorrectos&#39;</span>)   
    <span style="color: #080; font-weight: bold">return</span> render(request, <span style="background-color: #FFF0F0">&#39;core/iniciar_sesion.html&#39;</span>)
<span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">cerrar_sesion</span>(request):
    logout(request)
    <span style="color: #080; font-weight: bold">return</span> redirect(<span style="background-color: #FFF0F0">&#39;inicio&#39;</span>)
<span style="color: #555; font-weight: bold">@login_required</span>
<span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">panel</span>(request):
    cuentas <span style="color: #333">=</span> Cuenta<span style="color: #333">.</span>objects<span style="color: #333">.</span>filter(propietario<span style="color: #333">=</span>request<span style="color: #333">.</span>user)
    saldo_total <span style="color: #333">=</span> cuentas<span style="color: #333">.</span>aggregate(Sum(<span style="background-color: #FFF0F0">&#39;saldo&#39;</span>))[<span style="background-color: #FFF0F0">&#39;saldo__sum&#39;</span>] <span style="color: #000; font-weight: bold">or</span> <span style="color: #00D; font-weight: bold">0</span>
    transacciones_recientes <span style="color: #333">=</span> Transaccion<span style="color: #333">.</span>objects<span style="color: #333">.</span>filter(usuario<span style="color: #333">=</span>request<span style="color: #333">.</span>user)<span style="color: #333">.</span>order_by(<span style="background-color: #FFF0F0">&#39;-fecha&#39;</span>)[:<span style="color: #00D; font-weight: bold">5</span>]   
    <span style="color: #080; font-weight: bold">return</span> render(request, <span style="background-color: #FFF0F0">&#39;core/panel.html&#39;</span>, {
        <span style="background-color: #FFF0F0">&#39;cuentas&#39;</span>: cuentas,
        <span style="background-color: #FFF0F0">&#39;saldo_total&#39;</span>: saldo_total,
        <span style="background-color: #FFF0F0">&#39;transacciones_recientes&#39;</span>: transacciones_recientes
    })
<span style="color: #555; font-weight: bold">@login_required</span>
<span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">crear_cuenta</span>(request):
    <span style="color: #080; font-weight: bold">if</span> request<span style="color: #333">.</span>method <span style="color: #333">==</span> <span style="background-color: #FFF0F0">&#39;POST&#39;</span>:
        formulario <span style="color: #333">=</span> FormularioCuenta(request<span style="color: #333">.</span>POST)
        <span style="color: #080; font-weight: bold">if</span> formulario<span style="color: #333">.</span>is_valid():
            cuenta <span style="color: #333">=</span> formulario<span style="color: #333">.</span>save(commit<span style="color: #333">=</span><span style="color: #080; font-weight: bold">False</span>)
            cuenta<span style="color: #333">.</span>propietario <span style="color: #333">=</span> request<span style="color: #333">.</span>user
            cuenta<span style="color: #333">.</span>saldo <span style="color: #333">=</span> <span style="color: #00D; font-weight: bold">0</span>
            cuenta<span style="color: #333">.</span>save()
            formulario<span style="color: #333">.</span>save_m2m()
            messages<span style="color: #333">.</span>success(request, <span style="background-color: #FFF0F0">&#39;Cuenta creada exitosamente&#39;</span>)
            <span style="color: #080; font-weight: bold">return</span> redirect(<span style="background-color: #FFF0F0">&#39;panel&#39;</span>)
    <span style="color: #080; font-weight: bold">else</span>:
        formulario <span style="color: #333">=</span> FormularioCuenta()   
    <span style="color: #080; font-weight: bold">return</span> render(request, <span style="background-color: #FFF0F0">&#39;core/crear_cuenta.html&#39;</span>, {<span style="background-color: #FFF0F0">&#39;formulario&#39;</span>: formulario})
<span style="color: #555; font-weight: bold">@login_required</span>
<span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">realizar_transferencia</span>(request):
    <span style="color: #080; font-weight: bold">if</span> request<span style="color: #333">.</span>method <span style="color: #333">==</span> <span style="background-color: #FFF0F0">&#39;POST&#39;</span>:
        cuenta_origen_id <span style="color: #333">=</span> request<span style="color: #333">.</span>POST<span style="color: #333">.</span>get(<span style="background-color: #FFF0F0">&#39;cuenta_origen&#39;</span>)
        numero_cuenta_destino <span style="color: #333">=</span> request<span style="color: #333">.</span>POST<span style="color: #333">.</span>get(<span style="background-color: #FFF0F0">&#39;cuenta_destino&#39;</span>)
        monto <span style="color: #333">=</span> Decimal(request<span style="color: #333">.</span>POST<span style="color: #333">.</span>get(<span style="background-color: #FFF0F0">&#39;monto&#39;</span>))       
        cuenta_origen <span style="color: #333">=</span> get_object_or_404(Cuenta, <span style="color: #007020">id</span><span style="color: #333">=</span>cuenta_origen_id, propietario<span style="color: #333">=</span>request<span style="color: #333">.</span>user)      
        <span style="color: #080; font-weight: bold">try</span>:
            cuenta_destino <span style="color: #333">=</span> Cuenta<span style="color: #333">.</span>objects<span style="color: #333">.</span>get(numero_cuenta<span style="color: #333">=</span>numero_cuenta_destino)
        <span style="color: #080; font-weight: bold">except</span> Cuenta<span style="color: #333">.</span>DoesNotExist:
            messages<span style="color: #333">.</span>error(request, <span style="background-color: #FFF0F0">&#39;La cuenta destino no existe&#39;</span>)
            <span style="color: #080; font-weight: bold">return</span> redirect(<span style="background-color: #FFF0F0">&#39;transferencia&#39;</span>)       
        <span style="color: #080; font-weight: bold">if</span> monto <span style="color: #333">&lt;=</span> <span style="color: #00D; font-weight: bold">0</span>:
            messages<span style="color: #333">.</span>error(request, <span style="background-color: #FFF0F0">&#39;El monto debe ser mayor a cero&#39;</span>)
        <span style="color: #080; font-weight: bold">elif</span> cuenta_origen<span style="color: #333">.</span>saldo <span style="color: #333">&lt;</span> monto:
            messages<span style="color: #333">.</span>error(request, <span style="background-color: #FFF0F0">&#39;Saldo insuficiente&#39;</span>)
        <span style="color: #080; font-weight: bold">elif</span> cuenta_origen<span style="color: #333">.</span>id <span style="color: #333">==</span> cuenta_destino<span style="color: #333">.</span>id:
            messages<span style="color: #333">.</span>error(request, <span style="background-color: #FFF0F0">&#39;No puedes transferir a la misma cuenta&#39;</span>)
        <span style="color: #080; font-weight: bold">else</span>:
            transaccion <span style="color: #333">=</span> Transaccion<span style="color: #333">.</span>objects<span style="color: #333">.</span>create(
                usuario<span style="color: #333">=</span>request<span style="color: #333">.</span>user,
                tipo_transaccion<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;transferencia&#39;</span>,
                descripcion<span style="color: #333">=</span><span style="background-color: #FFF0F0">f&quot;Transferencia a </span><span style="background-color: #EEE">{</span>cuenta_destino<span style="color: #333">.</span>numero_cuenta<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>
            )           
            DetalleTransaccion<span style="color: #333">.</span>objects<span style="color: #333">.</span>create(
                transaccion<span style="color: #333">=</span>transaccion,
                cuenta<span style="color: #333">=</span>cuenta_origen,
                monto<span style="color: #333">=-</span>monto            )           
            DetalleTransaccion<span style="color: #333">.</span>objects<span style="color: #333">.</span>create(
                transaccion<span style="color: #333">=</span>transaccion,
                cuenta<span style="color: #333">=</span>cuenta_destino,
                monto<span style="color: #333">=</span>monto
            )          
            cuenta_origen<span style="color: #333">.</span>saldo <span style="color: #333">-=</span> monto
            cuenta_origen<span style="color: #333">.</span>save()
            cuenta_destino<span style="color: #333">.</span>saldo <span style="color: #333">+=</span> monto
            cuenta_destino<span style="color: #333">.</span>save()           
            messages<span style="color: #333">.</span>success(request, <span style="background-color: #FFF0F0">f&#39;Transferencia de $</span><span style="background-color: #EEE">{</span>monto<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0"> realizada con éxito&#39;</span>)
            <span style="color: #080; font-weight: bold">return</span> redirect(<span style="background-color: #FFF0F0">&#39;panel&#39;</span>)   
    cuentas <span style="color: #333">=</span> Cuenta<span style="color: #333">.</span>objects<span style="color: #333">.</span>filter(propietario<span style="color: #333">=</span>request<span style="color: #333">.</span>user, estado<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;activa&#39;</span>)
    <span style="color: #080; font-weight: bold">return</span> render(request, <span style="background-color: #FFF0F0">&#39;core/transferencia.html&#39;</span>, {<span style="background-color: #FFF0F0">&#39;cuentas&#39;</span>: cuentas})
<span style="color: #555; font-weight: bold">@login_required</span>
<span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">editar_perfil</span>(request):
    <span style="color: #080; font-weight: bold">if</span> request<span style="color: #333">.</span>method <span style="color: #333">==</span> <span style="background-color: #FFF0F0">&#39;POST&#39;</span>:
        formulario <span style="color: #333">=</span> FormularioActualizarUsuario(request<span style="color: #333">.</span>POST, request<span style="color: #333">.</span>FILES, instance<span style="color: #333">=</span>request<span style="color: #333">.</span>user)
        <span style="color: #080; font-weight: bold">if</span> formulario<span style="color: #333">.</span>is_valid():
            formulario<span style="color: #333">.</span>save()
            messages<span style="color: #333">.</span>success(request, <span style="background-color: #FFF0F0">&#39;Perfil actualizado correctamente&#39;</span>)
            <span style="color: #080; font-weight: bold">return</span> redirect(<span style="background-color: #FFF0F0">&#39;panel&#39;</span>)
   
 <span style="color: #080; font-weight: bold">else</span>:
        formulario <span style="color: #333">=</span> FormularioActualizarUsuario(instance<span style="color: #333">=</span>request<span style="color: #333">.</span>user)   
    <span style="color: #080; font-weight: bold">return</span> render(request, <span style="background-color: #FFF0F0">&#39;core/editar_perfil.html&#39;</span>, {<span style="background-color: #FFF0F0">&#39;formulario&#39;</span>: formulario})
<span style="color: #555; font-weight: bold">@login_required</span>
<span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">recargar_saldo</span>(request, cuenta_id):
    cuenta <span style="color: #333">=</span> get_object_or_404(Cuenta, <span style="color: #007020">id</span><span style="color: #333">=</span>cuenta_id, propietario<span style="color: #333">=</span>request<span style="color: #333">.</span>user)   
    <span style="color: #080; font-weight: bold">if</span> request<span style="color: #333">.</span>method <span style="color: #333">==</span> <span style="background-color: #FFF0F0">&#39;POST&#39;</span>:
        monto <span style="color: #333">=</span> Decimal(request<span style="color: #333">.</span>POST<span style="color: #333">.</span>get(<span style="background-color: #FFF0F0">&#39;monto&#39;</span>))       
        <span style="color: #080; font-weight: bold">if</span> monto <span style="color: #333">&lt;=</span> <span style="color: #00D; font-weight: bold">0</span>:
            messages<span style="color: #333">.</span>error(request, <span style="background-color: #FFF0F0">&#39;El monto debe ser mayor a cero&#39;</span>)
        <span style="color: #080; font-weight: bold">else</span>:
            transaccion <span style="color: #333">=</span> Transaccion<span style="color: #333">.</span>objects<span style="color: #333">.</span>create(
                usuario<span style="color: #333">=</span>request<span style="color: #333">.</span>user,
                tipo_transaccion<span style="color: #333">=</span><span style="background-color: #FFF0F0">&#39;deposito&#39;</span>,
                descripcion<span style="color: #333">=</span><span style="background-color: #FFF0F0">f&quot;Recarga a cuenta </span><span style="background-color: #EEE">{</span>cuenta<span style="color: #333">.</span>numero_cuenta<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>
            )         
            DetalleTransaccion<span style="color: #333">.</span>objects<span style="color: #333">.</span>create(
                transaccion<span style="color: #333">=</span>transaccion,
                cuenta<span style="color: #333">=</span>cuenta,
                monto<span style="color: #333">=</span>monto
            )           
            cuenta<span style="color: #333">.</span>saldo <span style="color: #333">+=</span> monto
            cuenta<span style="color: #333">.</span>save()           
            messages<span style="color: #333">.</span>success(request, <span style="background-color: #FFF0F0">f&#39;¡Recarga exitosa! Se añadieron $</span><span style="background-color: #EEE">{</span>monto<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0"> a tu cuenta&#39;</span>)
            <span style="color: #080; font-weight: bold">return</span> redirect(<span style="background-color: #FFF0F0">&#39;panel&#39;</span>)
   
    <span style="color: #080; font-weight: bold">return</span> render(request, <span style="background-color: #FFF0F0">&#39;core/recargar.html&#39;</span>, {<span style="background-color: #FFF0F0">&#39;cuenta&#39;</span>: cuenta})
</pre></div>

### 2.6 Panel de administración (admin.py)
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%;"><span></span><span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">django.contrib</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> admin
<span style="color: #080; font-weight: bold">from</span><span style="color: #BBB"> </span><span style="color: #0E84B5; font-weight: bold">.models</span><span style="color: #BBB"> </span><span style="color: #080; font-weight: bold">import</span> Usuario, TipoCuenta, Cuenta, Transaccion, DetalleTransaccion

<span style="color: #555; font-weight: bold">@admin</span><span style="color: #333">.</span>register(Usuario)
<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">UsuarioAdmin</span>(admin<span style="color: #333">.</span>ModelAdmin):
    list_display <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;username&#39;</span>, <span style="background-color: #FFF0F0">&#39;email&#39;</span>, <span style="background-color: #FFF0F0">&#39;telefono&#39;</span>, <span style="background-color: #FFF0F0">&#39;fecha_registro&#39;</span>, <span style="background-color: #FFF0F0">&#39;activo&#39;</span>)
    list_filter <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;is_active&#39;</span>, <span style="background-color: #FFF0F0">&#39;is_staff&#39;</span>, <span style="background-color: #FFF0F0">&#39;date_joined&#39;</span>)
    search_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;username&#39;</span>, <span style="background-color: #FFF0F0">&#39;email&#39;</span>, <span style="background-color: #FFF0F0">&#39;telefono&#39;</span>)
    readonly_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;id&#39;</span>, <span style="background-color: #FFF0F0">&#39;date_joined&#39;</span>, <span style="background-color: #FFF0F0">&#39;last_login&#39;</span>)
    
    fieldsets <span style="color: #333">=</span> (
        (<span style="background-color: #FFF0F0">&#39;Información Personal&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;username&#39;</span>, <span style="background-color: #FFF0F0">&#39;email&#39;</span>, <span style="background-color: #FFF0F0">&#39;telefono&#39;</span>, <span style="background-color: #FFF0F0">&#39;direccion&#39;</span>, <span style="background-color: #FFF0F0">&#39;foto_perfil&#39;</span>)
        }),
        (<span style="background-color: #FFF0F0">&#39;Permisos&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;is_active&#39;</span>, <span style="background-color: #FFF0F0">&#39;is_staff&#39;</span>, <span style="background-color: #FFF0F0">&#39;is_superuser&#39;</span>, <span style="background-color: #FFF0F0">&#39;groups&#39;</span>, <span style="background-color: #FFF0F0">&#39;user_permissions&#39;</span>)
        }),
        (<span style="background-color: #FFF0F0">&#39;Información del Sistema&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;id&#39;</span>, <span style="background-color: #FFF0F0">&#39;date_joined&#39;</span>, <span style="background-color: #FFF0F0">&#39;last_login&#39;</span>),
            <span style="background-color: #FFF0F0">&#39;classes&#39;</span>: (<span style="background-color: #FFF0F0">&#39;collapse&#39;</span>,)
        }),
    )
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">telefono</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> obj<span style="color: #333">.</span>telefono <span style="color: #000; font-weight: bold">or</span> <span style="background-color: #FFF0F0">&#39;No registrado&#39;</span>
    telefono<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Teléfono&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">fecha_registro</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> obj<span style="color: #333">.</span>date_joined<span style="color: #333">.</span>strftime(<span style="background-color: #FFF0F0">&#39;</span><span style="background-color: #EEE">%d</span><span style="background-color: #FFF0F0">/%m/%Y %H:%M&#39;</span>)
    fecha_registro<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Fecha de Registro&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">activo</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> obj<span style="color: #333">.</span>is_active
    activo<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Activo&#39;</span>
    activo<span style="color: #333">.</span>boolean <span style="color: #333">=</span> <span style="color: #080; font-weight: bold">True</span>

<span style="color: #555; font-weight: bold">@admin</span><span style="color: #333">.</span>register(TipoCuenta)
<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">TipoCuentaAdmin</span>(admin<span style="color: #333">.</span>ModelAdmin):
    list_display <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;nombre&#39;</span>, <span style="background-color: #FFF0F0">&#39;tasa_interes&#39;</span>, <span style="background-color: #FFF0F0">&#39;cuota_mensual&#39;</span>, <span style="background-color: #FFF0F0">&#39;descripcion_corta&#39;</span>)
    search_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;nombre&#39;</span>, <span style="background-color: #FFF0F0">&#39;descripcion&#39;</span>)
    readonly_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;id&#39;</span>,)
    
    fieldsets <span style="color: #333">=</span> (
        (<span style="background-color: #FFF0F0">&#39;Información del Tipo de Cuenta&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;nombre&#39;</span>, <span style="background-color: #FFF0F0">&#39;descripcion&#39;</span>, <span style="background-color: #FFF0F0">&#39;tasa_interes&#39;</span>, <span style="background-color: #FFF0F0">&#39;cuota_mensual&#39;</span>)
        }),
        (<span style="background-color: #FFF0F0">&#39;Información del Sistema&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;id&#39;</span>,),
            <span style="background-color: #FFF0F0">&#39;classes&#39;</span>: (<span style="background-color: #FFF0F0">&#39;collapse&#39;</span>,)
        }),
    )
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">nombre</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> obj<span style="color: #333">.</span>nombre
    nombre<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Nombre del Tipo&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">tasa_interes</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;</span><span style="background-color: #EEE">{</span>obj<span style="color: #333">.</span>tasa_interes<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">%&quot;</span>
    tasa_interes<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Tasa de Interés&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">cuota_mensual</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;$</span><span style="background-color: #EEE">{</span>obj<span style="color: #333">.</span>cuota_mensual<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>
    cuota_mensual<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Cuota Mensual&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">descripcion_corta</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> obj<span style="color: #333">.</span>descripcion[:<span style="color: #00D; font-weight: bold">50</span>] <span style="color: #333">+</span> <span style="background-color: #FFF0F0">&#39;...&#39;</span> <span style="color: #080; font-weight: bold">if</span> <span style="color: #007020">len</span>(obj<span style="color: #333">.</span>descripcion) <span style="color: #333">&gt;</span> <span style="color: #00D; font-weight: bold">50</span> <span style="color: #080; font-weight: bold">else</span> obj<span style="color: #333">.</span>descripcion
    descripcion_corta<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Descripción&#39;</span>

<span style="color: #555; font-weight: bold">@admin</span><span style="color: #333">.</span>register(Cuenta)
<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">CuentaAdmin</span>(admin<span style="color: #333">.</span>ModelAdmin):
    list_display <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;numero_cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;propietario&#39;</span>, <span style="background-color: #FFF0F0">&#39;saldo&#39;</span>, <span style="background-color: #FFF0F0">&#39;estado&#39;</span>, <span style="background-color: #FFF0F0">&#39;tipos_cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;fecha_creacion&#39;</span>)
    list_filter <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;estado&#39;</span>, <span style="background-color: #FFF0F0">&#39;tipos_cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;fecha_creacion&#39;</span>)
    search_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;numero_cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;propietario__username&#39;</span>, <span style="background-color: #FFF0F0">&#39;propietario__email&#39;</span>)
    filter_horizontal <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;tipos_cuenta&#39;</span>,)
    readonly_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;id&#39;</span>, <span style="background-color: #FFF0F0">&#39;fecha_creacion&#39;</span>)
    
    fieldsets <span style="color: #333">=</span> (
        (<span style="background-color: #FFF0F0">&#39;Información de la Cuenta&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;numero_cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;propietario&#39;</span>, <span style="background-color: #FFF0F0">&#39;tipos_cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;saldo&#39;</span>, <span style="background-color: #FFF0F0">&#39;estado&#39;</span>)
        }),
        (<span style="background-color: #FFF0F0">&#39;Información del Sistema&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;id&#39;</span>, <span style="background-color: #FFF0F0">&#39;fecha_creacion&#39;</span>),
            <span style="background-color: #FFF0F0">&#39;classes&#39;</span>: (<span style="background-color: #FFF0F0">&#39;collapse&#39;</span>,),
        }),
    )
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">numero_cuenta</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> obj<span style="color: #333">.</span>numero_cuenta
    numero_cuenta<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Número de Cuenta&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">propietario</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;</span><span style="background-color: #EEE">{</span>obj<span style="color: #333">.</span>propietario<span style="color: #333">.</span>username<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0"> (</span><span style="background-color: #EEE">{</span>obj<span style="color: #333">.</span>propietario<span style="color: #333">.</span>email<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">)&quot;</span>
    propietario<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Propietario&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">saldo</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;$</span><span style="background-color: #EEE">{</span>obj<span style="color: #333">.</span>saldo<span style="background-color: #EEE">:</span><span style="background-color: #FFF0F0">,.2f</span><span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>
    saldo<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Saldo Actual&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">estado</span>(<span style="color: #007020">self</span>, obj):
        estados <span style="color: #333">=</span> {
            <span style="background-color: #FFF0F0">&#39;activa&#39;</span>: <span style="background-color: #FFF0F0">&#39;Activa&#39;</span>,
            <span style="background-color: #FFF0F0">&#39;bloqueada&#39;</span>: <span style="background-color: #FFF0F0">&#39;Bloqueada&#39;</span>,
            <span style="background-color: #FFF0F0">&#39;cerrada&#39;</span>: <span style="background-color: #FFF0F0">&#39;Cerrada&#39;</span>
        }
        <span style="color: #080; font-weight: bold">return</span> estados<span style="color: #333">.</span>get(obj<span style="color: #333">.</span>estado, obj<span style="color: #333">.</span>estado)
    estado<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Estado&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">tipos_cuenta</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">&#39;, &#39;</span><span style="color: #333">.</span>join([t<span style="color: #333">.</span>nombre <span style="color: #080; font-weight: bold">for</span> t <span style="color: #000; font-weight: bold">in</span> obj<span style="color: #333">.</span>tipos_cuenta<span style="color: #333">.</span>all()])
    tipos_cuenta<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Tipos de Cuenta&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">fecha_creacion</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> obj<span style="color: #333">.</span>fecha_creacion<span style="color: #333">.</span>strftime(<span style="background-color: #FFF0F0">&#39;</span><span style="background-color: #EEE">%d</span><span style="background-color: #FFF0F0">/%m/%Y %H:%M&#39;</span>)
    fecha_creacion<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Fecha de Creación&#39;</span>

<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">DetalleTransaccionInline</span>(admin<span style="color: #333">.</span>TabularInline):
    model <span style="color: #333">=</span> DetalleTransaccion
    extra <span style="color: #333">=</span> <span style="color: #00D; font-weight: bold">1</span>
    readonly_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;id&#39;</span>,)
    fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;monto&#39;</span>)

<span style="color: #555; font-weight: bold">@admin</span><span style="color: #333">.</span>register(Transaccion)
<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">TransaccionAdmin</span>(admin<span style="color: #333">.</span>ModelAdmin):
    list_display <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;id_corto&#39;</span>, <span style="background-color: #FFF0F0">&#39;tipo_transaccion&#39;</span>, <span style="background-color: #FFF0F0">&#39;cliente&#39;</span>, <span style="background-color: #FFF0F0">&#39;fecha&#39;</span>, <span style="background-color: #FFF0F0">&#39;monto_total&#39;</span>)
    list_filter <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;tipo_transaccion&#39;</span>, <span style="background-color: #FFF0F0">&#39;fecha&#39;</span>, <span style="background-color: #FFF0F0">&#39;usuario&#39;</span>)
    search_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;usuario__username&#39;</span>, <span style="background-color: #FFF0F0">&#39;usuario__email&#39;</span>, <span style="background-color: #FFF0F0">&#39;descripcion&#39;</span>)
    readonly_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;id&#39;</span>, <span style="background-color: #FFF0F0">&#39;fecha&#39;</span>)
    inlines <span style="color: #333">=</span> [DetalleTransaccionInline]
    
    fieldsets <span style="color: #333">=</span> (
        (<span style="background-color: #FFF0F0">&#39;Información de la Transacción&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;tipo_transaccion&#39;</span>, <span style="background-color: #FFF0F0">&#39;usuario&#39;</span>, <span style="background-color: #FFF0F0">&#39;descripcion&#39;</span>)
        }),
        (<span style="background-color: #FFF0F0">&#39;Información del Sistema&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;id&#39;</span>, <span style="background-color: #FFF0F0">&#39;fecha&#39;</span>),
            <span style="background-color: #FFF0F0">&#39;classes&#39;</span>: (<span style="background-color: #FFF0F0">&#39;collapse&#39;</span>,),
        }),
    )
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">id_corto</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> <span style="color: #007020">str</span>(obj<span style="color: #333">.</span>id)<span style="color: #333">.</span>split(<span style="background-color: #FFF0F0">&#39;-&#39;</span>)[<span style="color: #00D; font-weight: bold">0</span>]
    id_corto<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;ID&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">tipo_transaccion</span>(<span style="color: #007020">self</span>, obj):
        tipos <span style="color: #333">=</span> {
            <span style="background-color: #FFF0F0">&#39;deposito&#39;</span>: <span style="background-color: #FFF0F0">&#39;Depósito&#39;</span>,
            <span style="background-color: #FFF0F0">&#39;retiro&#39;</span>: <span style="background-color: #FFF0F0">&#39;Retiro&#39;</span>,
            <span style="background-color: #FFF0F0">&#39;transferencia&#39;</span>: <span style="background-color: #FFF0F0">&#39;Transferencia&#39;</span>,
            <span style="background-color: #FFF0F0">&#39;pago&#39;</span>: <span style="background-color: #FFF0F0">&#39;Pago&#39;</span>
        }
        <span style="color: #080; font-weight: bold">return</span> tipos<span style="color: #333">.</span>get(obj<span style="color: #333">.</span>tipo_transaccion, obj<span style="color: #333">.</span>tipo_transaccion)
    tipo_transaccion<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Tipo de Transacción&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">cliente</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;</span><span style="background-color: #EEE">{</span>obj<span style="color: #333">.</span>usuario<span style="color: #333">.</span>username<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0"> (</span><span style="background-color: #EEE">{</span>obj<span style="color: #333">.</span>usuario<span style="color: #333">.</span>email<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">)&quot;</span>
    cliente<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Cliente&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">fecha</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> obj<span style="color: #333">.</span>fecha<span style="color: #333">.</span>strftime(<span style="background-color: #FFF0F0">&#39;</span><span style="background-color: #EEE">%d</span><span style="background-color: #FFF0F0">/%m/%Y %H:%M:%S&#39;</span>)
    fecha<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Fecha y Hora&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">monto_total</span>(<span style="color: #007020">self</span>, obj):
        total <span style="color: #333">=</span> <span style="color: #007020">sum</span>(detalle<span style="color: #333">.</span>monto <span style="color: #080; font-weight: bold">for</span> detalle <span style="color: #000; font-weight: bold">in</span> obj<span style="color: #333">.</span>detalletransaccion_set<span style="color: #333">.</span>all())
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;$</span><span style="background-color: #EEE">{</span><span style="color: #007020">abs</span>(total)<span style="background-color: #EEE">:</span><span style="background-color: #FFF0F0">,.2f</span><span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>
    monto_total<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Monto Total&#39;</span>

<span style="color: #555; font-weight: bold">@admin</span><span style="color: #333">.</span>register(DetalleTransaccion)
<span style="color: #080; font-weight: bold">class</span><span style="color: #BBB"> </span><span style="color: #B06; font-weight: bold">DetalleTransaccionAdmin</span>(admin<span style="color: #333">.</span>ModelAdmin):
    list_display <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;transaccion_id&#39;</span>, <span style="background-color: #FFF0F0">&#39;cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;monto&#39;</span>, <span style="background-color: #FFF0F0">&#39;monto_absoluto&#39;</span>)
    list_filter <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;transaccion__tipo_transaccion&#39;</span>, <span style="background-color: #FFF0F0">&#39;cuenta__estado&#39;</span>)
    search_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;transaccion__id&#39;</span>, <span style="background-color: #FFF0F0">&#39;cuenta__numero_cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;cuenta__propietario__username&#39;</span>)
    readonly_fields <span style="color: #333">=</span> (<span style="background-color: #FFF0F0">&#39;id&#39;</span>,)
    
    fieldsets <span style="color: #333">=</span> (
        (<span style="background-color: #FFF0F0">&#39;Información del Detalle&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;transaccion&#39;</span>, <span style="background-color: #FFF0F0">&#39;cuenta&#39;</span>, <span style="background-color: #FFF0F0">&#39;monto&#39;</span>)
        }),
        (<span style="background-color: #FFF0F0">&#39;Información del Sistema&#39;</span>, {
            <span style="background-color: #FFF0F0">&#39;fields&#39;</span>: (<span style="background-color: #FFF0F0">&#39;id&#39;</span>,),
            <span style="background-color: #FFF0F0">&#39;classes&#39;</span>: (<span style="background-color: #FFF0F0">&#39;collapse&#39;</span>,),
        }),
    )
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">transaccion_id</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> <span style="color: #007020">str</span>(obj<span style="color: #333">.</span>transaccion<span style="color: #333">.</span>id)<span style="color: #333">.</span>split(<span style="background-color: #FFF0F0">&#39;-&#39;</span>)[<span style="color: #00D; font-weight: bold">0</span>]
    transaccion_id<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;ID Transacción&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">cuenta</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;</span><span style="background-color: #EEE">{</span>obj<span style="color: #333">.</span>cuenta<span style="color: #333">.</span>numero_cuenta<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0"> (</span><span style="background-color: #EEE">{</span>obj<span style="color: #333">.</span>cuenta<span style="color: #333">.</span>propietario<span style="color: #333">.</span>username<span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">)&quot;</span>
    cuenta<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Cuenta&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">monto</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">if</span> obj<span style="color: #333">.</span>monto <span style="color: #333">&lt;</span> <span style="color: #00D; font-weight: bold">0</span>:
            <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;-$</span><span style="background-color: #EEE">{</span><span style="color: #007020">abs</span>(obj<span style="color: #333">.</span>monto)<span style="background-color: #EEE">:</span><span style="background-color: #FFF0F0">,.2f</span><span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;+$</span><span style="background-color: #EEE">{</span>obj<span style="color: #333">.</span>monto<span style="background-color: #EEE">:</span><span style="background-color: #FFF0F0">,.2f</span><span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>
    monto<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Monto&#39;</span>
    
    <span style="color: #080; font-weight: bold">def</span><span style="color: #BBB"> </span><span style="color: #06B; font-weight: bold">monto_absoluto</span>(<span style="color: #007020">self</span>, obj):
        <span style="color: #080; font-weight: bold">return</span> <span style="background-color: #FFF0F0">f&quot;$</span><span style="background-color: #EEE">{</span><span style="color: #007020">abs</span>(obj<span style="color: #333">.</span>monto)<span style="background-color: #EEE">:</span><span style="background-color: #FFF0F0">,.2f</span><span style="background-color: #EEE">}</span><span style="background-color: #FFF0F0">&quot;</span>
    monto_absoluto<span style="color: #333">.</span>short_description <span style="color: #333">=</span> <span style="background-color: #FFF0F0">&#39;Monto Absoluto&#39;</span>
</pre></div>

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

