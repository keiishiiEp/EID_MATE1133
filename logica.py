import sympy as sp
import math 

def procesar_limite(func_str, h_str):
    try:
        x = sp.symbols('x')
        funcion = sp.sympify(func_str)
        h_val = sp.sympify(h_str)
        
        # 1. Lógica manual
        def calcular_limite_manual(direccion):
            delta = 1e-7
            punto = float(h_val) - delta if direccion == '-' else float(h_val) + delta
            try:
                return float(funcion.subs(x, punto).evalf())
            except:
                return None

        lim_izq = calcular_limite_manual('-')
        lim_der = calcular_limite_manual('+')
        limite_resultado = sp.limit(funcion, x, h_val) #validar 
        
        # 2. Deteccion de tipo
        tipo_limite = "Evaluación Directa"
        salto = False
        if lim_izq is not None and lim_der is not None and abs(lim_izq - lim_der) > 0.1:
            tipo_limite = "Discontinuidad de Salto"
            salto = True
            limite_resultado = "No existe (Saltos distintos)"
        elif h_val.is_infinite:
            tipo_limite = "Límite al Infinito"
        elif str(limite_resultado) in ['oo', '-oo', 'zoo']:
            tipo_limite = "Límite Infinito (Diverge)"
        
        # 3. Graficación
        x_vals, y_vals = [], []
        if h_val.is_infinite:
            inicio, paso, puntos = (0, 0.1, 500) if h_val > 0 else (-50, 0.1, 500)
            marcar_asintota, h_float = False, None
        else:
            h_float = float(h_val)
            inicio, paso, puntos = h_float - 5, 0.02, 500
            marcar_asintota = True

        for i in range(puntos + 1):
            val_x = inicio + (i * paso)
            if marcar_asintota and abs(val_x - h_float) < 0.01:
                x_vals.append(val_x)
                y_vals.append(math.nan)
                continue
            try:
                y = float(funcion.subs(x, val_x).evalf())
                x_vals.append(val_x)
                y_vals.append(y)
            except:
                continue 

        # 4. Validación final
        if not [y for y in y_vals if not math.isnan(y)]:
            raise ValueError("Expresión no válida.")

        return {
            "exito": True, "limite": str(limite_resultado), "x_vals": x_vals, "y_vals": y_vals,
            "marcar_asintota": marcar_asintota, "h_float": h_float, "tipo_limite": tipo_limite,
            "salto": salto, "lim_izq": lim_izq, "lim_der": lim_der, "punto_exacto": None
        }
    except Exception as e:
        return {"exito": False, "error": str(e)}