# banco/core/views.py
import json
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Sum
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Usuario, Cuenta, TipoCuenta, Transaccion, DetalleTransaccion
from .forms import FormularioRegistro, FormularioCuenta, FormularioActualizarUsuario

# ==========================================
# 🪓 IMPORTACIÓN DEL ASISTENTE FINANCIERO 24/7
# ==========================================
from .asistente import generar_tips_financieros, responder_pregunta_chat


def inicio(request):
    busqueda = request.GET.get('q')
    tipo_cuenta_id = request.GET.get('tipo_cuenta')
    
    # 🛠️ Se agrega .order_by('-id') para solucionar el UnorderedObjectListWarning en la paginación
    cuentas = Cuenta.objects.select_related('propietario').prefetch_related('tipos_cuenta').all().order_by('-id')
    
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


# ==========================================
# 🪓 VISTA PRINCIPAL DEL PANEL BANCARIO
# ==========================================
@login_required
def panel(request):
    cuentas = Cuenta.objects.filter(propietario=request.user)
    saldo_total = cuentas.aggregate(Sum('saldo'))['saldo__sum'] or 0
    transacciones_recientes = Transaccion.objects.filter(usuario=request.user).order_by('-fecha')[:5]
    
    # ⚙️ Capturar si el usuario decide cambiar de asistente al dar un clic veloz
    if 'cambiar_asistente' in request.GET:
        request.session['tipo_asistente'] = request.GET.get('cambiar_asistente')
    
    # 🧠 Recuperar la personalidad guardada en la sesión actual (por defecto: moderador)
    tipo_actual = request.session.get('tipo_asistente', 'moderador')
    
    # 🤖 Correr el motor del asistente analizando los datos reales actuales
    datos_asistente = generar_tips_financieros(tipo_actual, saldo_total, transacciones_recientes)
    
    return render(request, 'core/panel.html', {
        'cuentas': cuentas,
        'saldo_total': saldo_total,
        'transacciones_recientes': transacciones_recientes,
        'asistente': datos_asistente, # <-- Pasado al HTML del panel
        'tipo_actual': tipo_actual     # <-- Control de estilo activo
    })


# ========================================================================
# 🪓 API ASÍNCRONA PARA EL CHAT INTERACTIVO (AJAX/FETCH)
# ========================================================================
@login_required
def asistente_chat_api(request):
    """Procesa los mensajes enviados desde el chat del panel en tiempo real"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            mensaje_usuario = data.get('mensaje', '')
            
            # Recalcular el saldo acumulado en tiempo real
            cuentas = Cuenta.objects.filter(propietario=request.user)
            saldo_total = cuentas.aggregate(Sum('saldo'))['saldo__sum'] or 0
            
            # Consultar al motor lógico la respuesta idónea
            respuesta = responder_pregunta_chat(mensaje_usuario, saldo_total)
            return JsonResponse({'respuesta': respuesta})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
            
    return JsonResponse({'error': 'Método no permitido'}, status=400)


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