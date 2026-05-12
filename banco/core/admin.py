from django.contrib import admin
from .modelos import Usuario, TipoCuenta, Cuenta, Transaccion, DetalleTransaccion

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
        return 'Sí' if obj.is_active else 'No'
    activo.short_description = 'Activo'
    activo.boolean = True

@admin.register(TipoCuenta)
class TipoCuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tasa_interes', 'cuota_mensual', 'descripcion_corta')
    search_fields = ('nombre', 'descripcion')
    
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
    readonly_fields = ('id', 'fecha', 'usuario')
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