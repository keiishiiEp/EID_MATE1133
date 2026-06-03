import sympy as sp
import math 

def procesar_limite(func_str, h_str):
    try:
        x = sp.symbols('x')
        funcion = sp.sympify(func_str)
        h_val = sp.sympify(h_str)
        
        # Calcular el límite general y laterales
        limite_resultado = sp.limit(funcion, x, h_val)
        lim_izq = sp.limit(funcion, x, h_val, dir='-')
        lim_der = sp.limit(funcion, x, h_val, dir='+')
        
        tipo_limite = "Evaluación Directa"
        salto = False
        
        # Detecta tipo de limite
        if lim_izq != lim_der and lim_izq.is_real and lim_der.is_real:
            tipo_limite = "Discontinuidad de Salto"
            salto = True
            limite_resultado = "No existe (Saltos distintos)"
        elif h_val == sp.oo or h_val == -sp.oo:
            tipo_limite = "Límite al Infinito"
        elif limite_resultado == sp.oo or limite_resultado == -sp.oo or limite_resultado == sp.zoo:
            tipo_limite = "Límite Infinito (Diverge)"
        else:
            try:
                eval_directa = funcion.subs('x', h_val)
                if eval_directa == sp.nan or eval_directa == sp.zoo:
                    tipo_limite = "Indeterminación"
            except Exception:
                tipo_limite = "Indeterminación"
        
        x_vals = []
        y_vals = []
        
        if h_val == sp.oo:
            inicio, paso, puntos = 0, 1.0, 50
            marcar_asintota, h_float = False, None
        elif h_val == -sp.oo:
            inicio, paso, puntos = -50, 1.0, 50
            marcar_asintota, h_float = False, None
        else:
            h_float = float(h_val)
            inicio, paso, puntos = h_float - 5, 0.2, 500
            marcar_asintota = True

        for i in range(puntos + 1):
            val_x = inicio + (i * paso)
            
            # Si estamos en el punto h y hay un salto, insertamos un pequeño vacío
            if marcar_asintota and abs(val_x - h_float) < 1e-9:
                x_vals.append(val_x)
                y_vals.append(math.nan) # Rompe la línea
                continue
                
            try:
                resultado_eval = funcion.subs('x', val_x).evalf()
                val_y = float(resultado_eval)
                x_vals.append(val_x)
                y_vals.append(val_y)
            except Exception:
                continue 

        # Evaluamos si el punto exacto f(h) existe
        punto_exacto = None
        try:
            eval_h = funcion.subs('x', h_float).evalf()
            if eval_h.is_real:
                punto_exacto = float(eval_h)
        except Exception:
            pass

        return {
            "exito": True,
            "limite": limite_resultado,
            "x_vals": x_vals,
            "y_vals": y_vals,
            "marcar_asintota": marcar_asintota,
            "h_float": h_float,
            "tipo_limite": tipo_limite,
            "salto": salto,
            "lim_izq": float(lim_izq) if lim_izq.is_real else None,
            "lim_der": float(lim_der) if lim_der.is_real else None,
            "punto_exacto": punto_exacto
        }
        
    except Exception as e:
        return {"exito": False, "error": str(e)}