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