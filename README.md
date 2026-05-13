

# 📄 `README.md` (con Sprints)

```markdown
# 🏦 Banco Digital - Django 5 Application

Sistema bancario completo desarrollado con Django 5 y SQLite que permite gestión de cuentas, transferencias y dashboard financiero con relaciones de base de datos 1:N y N:M.

---

## 🚀 SPRINT 1 — Setup + Modelado Base

### 🎯 Objetivo

Tener:
- Proyecto Django funcionando
- App core (banco)
- Modelos con relaciones:
  - 1:N → Usuario → Cuenta
  - N:M → Cuenta ↔ TipoCuenta
  - N:M → Transacción ↔ Cuenta (con tabla intermedia)
- Admin operativo

### 1. Crear proyecto en django
```bash
django-admin startproject banco
cd banco
python manage.py startapp core
```

### 2. Configurar settings.py
```python
INSTALLED_APPS = [
    ...
    'core',
]

AUTH_USER_MODEL = 'core.Usuario'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### 3. MODELOS (CLAVE DEL PROYECTO)

**core/modelos.py:**
```python
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

class TipoCuenta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cuota_mensual = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Cuenta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_cuenta = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=10, default='activa')
    
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cuentas')  # 1:N
    tipos_cuenta = models.ManyToManyField(TipoCuenta, related_name='cuentas')  # N:M

class Transaccion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_transaccion = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cuentas = models.ManyToManyField(Cuenta, through='DetalleTransaccion')  # N:M

class DetalleTransaccion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
```

### 4. Admin de django (en español)
- Panel administrativo completamente traducido
- Campos personalizados: teléfono, fecha registro, saldo, estado
- Filtros y búsqueda por todos los campos

### 5. Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 🚀 SPRINT 2 — Autenticación + UI Base

### 🎯 Objetivo
- Registro, login, logout
- Layout base con CSS puro
- Navbar dinámica
- Listado de cuentas
- Home pública

### URLs principales
```python
urlpatterns = [
    path('', vistas.inicio, name='inicio'),
    path('registro/', vistas.registro, name='registro'),
    path('iniciar-sesion/', vistas.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', vistas.cerrar_sesion, name='cerrar_sesion'),
]
```

### Formularios
- FormularioRegistro con email, teléfono y foto de perfil
- Bootstrap reemplazado por CSS personalizado

### Templates
- base.html (nav, footer, estilos)
- inicio.html (listado de cuentas)
- registro.html
- iniciar_sesion.html

---

## 🚀 SPRINT 3 — Gestión de Cuentas + Dashboard

### 🎯 Objetivo
- CRUD completo de cuentas
- Dashboard para clientes
- Control de permisos (solo dueño)
- UI tipo panel bancario

### URLs agregadas
```python
path('panel/', vistas.panel, name='panel'),
path('cuenta/crear/', vistas.crear_cuenta, name='crear_cuenta'),
```

### Dashboard features
- Credencial bancaria con foto de perfil
- Saldo total de todas las cuentas
- Listado de cuentas del usuario
- Últimos movimientos recientes

---

## 🚀 SPRINT 4 — Transferencias + Movimientos

### 🎯 Objetivo
- Sistema de transferencias entre cuentas
- Validación de saldo suficiente
- Registro de transacciones
- Actualización atómica de saldos

### URLs agregadas
```python
path('transferencia/', vistas.realizar_transferencia, name='transferencia'),
```

### Lógica de transferencia
```python
# Validaciones
- Monto mayor a cero
- Saldo suficiente
- Cuenta destino existe
- No transferir a misma cuenta

# Actualizaciones
- Restar saldo a cuenta origen
- Sumar saldo a cuenta destino
- Registrar transacción con detalles
```

---

## 🚀 SPRINT 5 — Optimización + UX

### 🎯 Objetivo
- Búsqueda de cuentas
- Filtros por tipo de cuenta
- Paginación
- Mensajes dinámicos
- Optimización ORM
- Edición de perfil con foto

### Mejoras implementadas
```python
# Búsqueda con Q
cuentas.filter(Q(numero_cuenta__icontains=query) | Q(propietario__username__icontains=query))

# Filtros
cuentas.filter(tipos_cuenta__id=tipo_cuenta_id)

# Paginación
Paginator(cuentas, 6)

# Optimización
select_related('propietario').prefetch_related('tipos_cuenta')
```

### URLs agregadas
```python
path('perfil/editar/', vistas.editar_perfil, name='editar_perfil'),
```

---

## 📊 Diagrama de Relaciones

```
Usuario (1) ──────→ (N) Cuenta
                           │
                           │ (N:M)
                           ↓
                     TipoCuenta

Transacción (N) ←──→ (N) Cuenta (a través de DetalleTransaccion)
```

## 🛠️ Tecnologías

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.13+ | Lenguaje principal |
| Django | 5.2+ | Framework web |
| SQLite | - | Base de datos |
| Pillow | 10.3+ | Manejo de imágenes |
| HTML5/CSS3 | - | Interfaz de usuario |

## 📦 Instalación

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

## 🧪 Flujo de prueba

1. Ir a /registro/ y crear usuario con foto
2. Ir a /admin/ y crear Tipos de Cuenta (Ahorro, Corriente, Nómina, Inversión)
3. Ir a /cuenta/crear/ y abrir cuenta con saldo inicial
4. Ir a /panel/ y ver dashboard
5. Ir a /transferencia/ y transferir a otra cuenta
6. Ver movimientos reflejados en panel

## ✅ Resultado Final

El Banco Digital ya tiene:
- ✔ Autenticación con foto de perfil
- ✔ Roles de usuario
- ✔ CRUD de cuentas
- ✔ Dashboard financiero
- ✔ Transferencias bancarias
- ✔ Filtros y búsqueda
- ✔ Paginación
- ✔ Panel admin en español

## 👤 Autor

- **Anita Susana** - [@anitaanita-jpg](https://github.com/anitaanita-jpg)

## 📄 Licencia

MIT License
```

## 📝 Guardar y subir:

```bash
git add README.md
git commit -m "actualizado readme con estructura de sprints como el marketplace original"
git push
```

