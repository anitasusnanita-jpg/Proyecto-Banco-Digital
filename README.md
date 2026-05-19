# 🏦 Banco Digital - Django 
Banco Digital es una plataforma bancaria simulada construida con Django que permite a los usuarios gestionar múltiples cuentas bancarias, realizar transferencias, consultar movimientos y administrar su perfil de forma intuitiva y segura.

El sistema incluye autenticación completa (registro, login, logout), un panel de control personal con saldo total agregado, listado de cuentas propias y últimos movimientos recientes. Los usuarios pueden abrir nuevas cuentas asociadas a diferentes tipos (ahorro, corriente, inversión), recargar saldo, transferir dinero entre cuentas con validación de saldo suficiente, y editar su perfil incluyendo foto, teléfono y dirección.

La plataforma también ofrece un listado público de cuentas con búsqueda por número o nombre de usuario, filtros por tipo de cuenta y paginación. Cada transacción queda registrada automáticamente con fecha, tipo, monto y descripción, manteniendo un historial completo de movimientos.

El proyecto utiliza UUID como identificador principal para evitar enumeración de recursos, relaciones 1:N entre usuario y cuentas, y relaciones N:M entre cuentas y tipos de cuenta. La interfaz es responsive, usa CSS puro e incluye mensajes flash de éxito o error para cada operación. Banco Digital es ideal como proyecto de portafolio, base para productos reales o material educativo sobre Django.

---


## 🚀 SPRINT 1 — Setup + Modelado Base

### 🎯 Objetivo
- Proyecto Django funcionando
- App core (banco)
- Modelos con relaciones 1:N y N:M
- Admin operativo

### 📁 Estructura inicial
```bash
django-admin startproject banco
cd banco
python manage.py startapp core
```

### 🗄️ Modelos creados
- `Usuario` (con foto_perfil, teléfono, dirección)
- `TipoCuenta` (nombre, tasa_interés, cuota_mensual)
- `Cuenta` (numero_cuenta, saldo, estado)
- `Transaccion` (tipo, descripción, fecha)
- `DetalleTransaccion` (monto, tabla intermedia)

# 🗄️Diseño del modelo

Diseño de la Base De Datos Relacional en Diagrama Entidad-Relacion que contine de uno a muchos y de muchos a muchos.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/640c59b7-4889-4922-a5a5-9f1144cf89d9" />



### Relaciones implementadas
| Relación | Tipo |
|----------|------|
| Usuario → Cuenta | 1:N |
| Cuenta ↔ TipoCuenta | N:M |
| Transacción ↔ Cuenta | N:M (vía DetalleTransaccion) |

### ✅ Sprint 1 entregables
- [x] Proyecto Django creado
- [x] App core registrada
- [x] Modelos con relaciones 1:N y N:M
- [x] UUID como primary key
- [x] Panel admin configurado
- [x] Migraciones aplicadas

---

## 🚀 SPRINT 2 — Autenticación + UI Base

### 🎯 Objetivo
- Sistema de registro y login
- Layout base con CSS puro
- Navbar dinámica
- Home pública

### URLs de autenticación
```python
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
```

### Templates creados en este sprint

| # | Template | Función |
|---|----------|---------|
| 1 | `base.html` | Plantilla principal con navegación y estilos CSS |
| 2 | `inicio.html` | Listado de cuentas públicas con búsqueda y filtros |
| 3 | `registro.html` | Formulario de registro con foto de perfil |
| 4 | `iniciar_sesion.html` | Formulario de inicio de sesión |

### ✅ Sprint 2 entregables
- [x] Registro de usuarios con foto
- [x] Login/logout funcional
- [x] Navbar dinámica
- [x] CSS personalizado
- [x] Mensajes flash de éxito/error
- [x] 4 templates creados

---

## 🚀 SPRINT 3 — Gestión de Cuentas + Dashboard

### 🎯 Objetivo
- CRUD de cuentas bancarias
- Dashboard personal para clientes
- Control de permisos

### URLs agregadas
```python
path('panel/', views.panel, name='panel'),
path('cuenta/crear/', views.crear_cuenta, name='crear_cuenta'),
```

### Templates creados en este sprint

| # | Template | Función |
|---|----------|---------|
| 5 | `panel.html` | Dashboard con saldo total, cuentas y movimientos |
| 6 | `crear_cuenta.html` | Formulario para abrir nueva cuenta |

### Dashboard features
- Credencial bancaria con foto de perfil
- Saldo total de todas las cuentas
- Listado de cuentas del usuario
- Últimos movimientos recientes

### ✅ Sprint 3 entregables
- [x] Dashboard con resumen financiero
- [x] Crear nuevas cuentas
- [x] Listado de cuentas del usuario
- [x] Control de permisos
- [x] 2 nuevos templates (total: 6)

---

## 🚀 SPRINT 4 — Transferencias + Movimientos

### 🎯 Objetivo
- Sistema de transferencias entre cuentas
- Validación de saldo suficiente
- Registro de transacciones

### URL agregada
```python
path('transferencia/', views.realizar_transferencia, name='transferencia'),
```

### Template creado en este sprint

| # | Template | Función |
|---|----------|---------|
| 7 | `transferencia.html` | Formulario para transferir dinero entre cuentas |

### Lógica de transferencia
- Monto mayor a cero
- Saldo suficiente
- Cuenta destino existe
- No transferir a misma cuenta
- Restar saldo a cuenta origen
- Sumar saldo a cuenta destino

### ✅ Sprint 4 entregables
- [x] Transferencias entre cuentas
- [x] Validación de saldo insuficiente
- [x] Registro automático de transacciones
- [x] 1 nuevo template (total: 7)

---

## 🚀 SPRINT 5 — Optimización + UX + Recarga + Edición

### 🎯 Objetivo
- Búsqueda y filtros
- Paginación
- Edición de perfil
- Recarga de saldo desde página web

### URLs agregadas
```python
path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
path('recargar/<uuid:cuenta_id>/', views.recargar_saldo, name='recargar'),
```

### Templates creados en este sprint

| # | Template | Función |
|---|----------|---------|
| 8 | `editar_perfil.html` | Formulario para actualizar datos personales y foto |
| 9 | `recargar.html` | Formulario para recargar saldo a una cuenta |

### Mejoras implementadas
```python
# Búsqueda con Q
cuentas.filter(Q(numero_cuenta__icontains=query) | Q(propietario__username__icontains=query))

# Filtros por tipo de cuenta
cuentas.filter(tipos_cuenta__id=tipo_cuenta_id)

# Paginación (6 cuentas por página)
Paginator(cuentas, 6)

# Optimización ORM
select_related('propietario').prefetch_related('tipos_cuenta')
```

### ✅ Sprint 5 entregables
- [x] Búsqueda de cuentas
- [x] Filtros por tipo de cuenta
- [x] Paginación en listado
- [x] Edición de perfil con foto
- [x] Recarga de saldo desde página web
- [x] Botón de recarga en cada cuenta
- [x] 2 nuevos templates (total: 9)

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

## 🛠️ Tecnologías utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.13+ | Lenguaje principal |
| Django | 5.2+ | Framework web |
| SQLite | - | Base de datos |
| Pillow | 10.3+ | Manejo de imágenes |
| HTML5/CSS3 | - | Interfaz de usuario |

## 📦 Instalación rápida

```bash
git clone https://github.com/-jpg/Proyecto-Banco-Digital.git
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

# 🏦 Conclusion
El desarrollo de Banco Digital ha demostrado ser un ejercicio completo y exitoso en la construcción de una aplicación web funcional utilizando el framework Django. A lo largo de 5 sprints, se implementó un sistema bancario simulado que integra autenticación de usuarios, gestión de cuentas, transferencias, recargas de saldo, edición de perfil y un dashboard financiero personalizado.

Se cumplieron todos los objetivos planteados inicialmente: modelado de datos con relaciones 1:N y N:M, panel de administración funcional, sistema de registro y login con foto de perfil, navegación dinámica, CRUD de cuentas, transferencias seguras con validación de saldo, paginación, búsqueda con filtros y edición de perfil. El proyecto cuenta con 9 templates completamente integrados y una interfaz responsive con CSS puro.

Las decisiones técnicas adoptadas resultaron acertadas. El uso de UUID como clave primaria mejora la seguridad al evitar la enumeración de recursos. La tabla intermedia DetalleTransaccion permite mayor flexibilidad para futuros tipos de operaciones. La optimización con select_related y prefetch_related reduce drásticamente el número de consultas a la base de datos. Las validaciones del lado del servidor garantizan la integridad de las operaciones financieras.

Banco Digital es un proyecto funcional, extensible y bien documentado que sirve como base sólida para agregar nuevas características como notificaciones por correo, reportes en PDF, gráficos de gastos, autenticación con redes sociales o integración con pasarelas de pago reales. Es ideal para portafolio profesional, material educativo o punto de partida para un producto financiero real.
---------------------------------------------------------------------------
