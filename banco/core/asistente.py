# banco/core/asistente.py

def generar_tips_financieros(tipo_asistente, saldo_total, transacciones_recientes):
    """
    Genera el bloque inicial de consejos dinámicos en el panel
    dependiendo de la personalidad seleccionada y los fondos reales.
    """
    if tipo_asistente == 'ahorrador':
        nombre = "AhorraBot"
        estado = "Optimizado para guardar"
        consejos = [
            "Guarda el 20% de tus ingresos de inmediato antes de gastar.",
            "Detectamos movimientos frecuentes. Intenta reducir los gastos hormiga esta semana."
        ]
    elif tipo_asistente == 'inversionista':
        nombre = "MidasBot"
        estado = "Buscando rendimientos"
        consejos = [
            "El dinero estático pierde valor frente a la inflación. Revisa opciones de inversión.",
            "Cuentas con capital libre que podría estar generando rendimientos a plazo fijo."
        ]
    else:  # 'moderador' por defecto
        nombre = "GastoBot"
        estado = "Moderado y Equilibrado"
        consejos = [
            "Aplica la regla 50/30/20: 50% para necesidades, 30% para gustos y 20% para el colchón financiero.",
            "Mantén un ojo firme sobre las últimas transferencias salientes para no desbalancearte."
        ]
        
    return {
        'nombre': nombre,
        'estado': estado,
        'consejos': consejos
    }

def responder_pregunta_chat(mensaje_usuario, saldo_total):
    """
    Procesa los mensajes enviados por el usuario desde la caja de chat interactiva
    y genera respuestas dinámicas analizando palabras clave.
    """
    mensaje = mensaje_usuario.lower()
    
    if "hola" in mensaje or "buenos dias" in mensaje or "buenas tardes" in mensaje:
        return "¡Hola! Soy tu asistente financiero personalizado. ¿En qué puedo ayudarte a gestionar tus cuentas hoy?"
        
    elif "saldo" in mensaje or "dinero" in mensaje or "tengo" in mensaje:
        if saldo_total <= 0:
            return f"Actualmente tu saldo total está en $0. ¡Zona de riesgo! Te sugiero realizar una recarga pronto para activar tus movimientos."
        elif saldo_total < 1000:
            return f"Tu saldo acumulado es de ${saldo_total}. Es un presupuesto ajustado; intenta priorizar únicamente compras indispensables."
        else:
            return f"Cuentas con un excelente saldo total de ${saldo_total}. Tienes buen margen para cubrir tus responsabilidades y destinar un porcentaje al ahorro."
            
    elif "ahorrar" in mensaje or "ahorro" in mensaje:
        meta_sugerida = saldo_total * 0.20
        return f"Con tu balance de ${saldo_total}, lo ideal sería congelar ${meta_sugerida:.2f} (el 20%). Te recomiendo abrir una cuenta secundaria destinada únicamente a emergencias."
        
    elif "invertir" in mensaje or "inversión" in mensaje or "inversion" in mensaje:
        if saldo_total > 5000:
            return "Tu nivel de fondos es óptimo para comenzar. Podrías mover un porcentaje a un fondo de inversión de bajo riesgo o renta fija para generar rendimientos pasivos."
        else:
            return "Antes de invertir, es vital establecer un fondo de emergencia sólido equivalente a 3 meses de tus gastos corrientes. ¡Asegura tu base primero!"
            
    elif "consejo" in mensaje or "tip" in mensaje:
        return "El consejo de oro hoy: No gastes dinero esperando ingresos futuros. Asegura primero lo que tienes en tu saldo real."
        
    else:
        return "Entiendo tu punto, pero recuerda que soy un asesor enfocado en tus finanzas. Pregúntame sobre tu 'saldo actual', estrategias de 'ahorro' o planes de 'inversión' para ayudarte mejor."