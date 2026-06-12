import sympy as sp # Importamos SymPy para trabajar con expresiones matemáticas simbólicas.
import math # Importamos math para usar herramientas numéricas.

# Esta función recibe:la función escrita como texto y el punto al que x tiende tambien como texto.
def procesar_limite(func_str, h_str):
    try:
        x = sp.symbols('x')# Creamos la variable simbólica x para trabajar con SymPy.
        funcion = sp.sympify(func_str) # Convertimos el texto de la función en una expresión matemática.
        h_val = sp.sympify(h_str) # Convertimos el texto del punto h en un valor simbólico.
        
        # 1. Lógica manual
        # Esta función interna aproxima el límite por izquierda o por derecha evaluando la función en un punto muy cercano a h.
        def calcular_limite_manual(direccion):
            delta = 1e-7 # Delta es una distancia muy pequeña para acercarnos al punto 
            punto = float(h_val) - delta if direccion == '-' else float(h_val) + delta # Si la dirección es '-', nos acercamos por la izquierda, si no, nos acercamos por la derecha.  
            try:
                return float(funcion.subs(x, punto).evalf())# Evaluamos la función en el punto cercano y devolvemos el resultado como float.
            except:
                return None # Si no se puede evaluar, devolvemos None.

        # Calculamos una aproximación del límite por la izquierda.
        lim_izq = calcular_limite_manual('-')
        # Calculamos una aproximación del límite por la derecha.
        lim_der = calcular_limite_manual('+')
        # Calculamos el límite simbólicamente con SymPy.
        limite_resultado = sp.limit(funcion, x, h_val) #validar 
        

        # 2. Deteccion de tipo
        # Por defecto asumimos que el límite se puede evaluar normalmente.
        tipo_limite = "Evaluación Directa"
        salto = False # Esta variable indica si hay discontinuidad de salto.

        # Si ambos límites laterales existen y son suficientemente distintos, consideramos que hay salto.
        if lim_izq is not None and lim_der is not None and abs(lim_izq - lim_der) > 0.1:
            tipo_limite = "Discontinuidad de Salto"
            salto = True
            # Si hay salto, decimos que el límite no existe.
            limite_resultado = "No existe (Saltos distintos)"

        # Si el punto h es infinito, clasificamos el caso como límite al infinito.
        elif h_val.is_infinite:
            tipo_limite = "Límite al Infinito"

        # Si SymPy devuelve oo, -oo o zoo, interpretamos que el límite diverge.
        elif str(limite_resultado) in ['oo', '-oo', 'zoo']:
            tipo_limite = "Límite Infinito (Diverge)"
        

        # 3. Graficación
        x_vals, y_vals = [], [] # Creamos listas vacías para guardar valores de x e y.
        
        # Si el límite es al infinito, usamos un rango especial para graficar.
        if h_val.is_infinite:
            # Si h es positivo, partimos desde 0, si es negativo, partimos desde -50.
            inicio, paso, puntos = (0, 0.1, 500) if h_val > 0 else (-50, 0.1, 500)
            # En este caso no se marca asíntota vertical en un punto específico.
            marcar_asintota, h_float = False, None
   
        else:
            h_float = float(h_val) # Convertimos h a float para usarlo numéricamente en la gráfica.
            inicio, paso, puntos = h_float - 5, 0.02, 500 # Definimos un intervalo centrado alrededor de h.
            marcar_asintota = True # Indicamos que sí se debe marcar una asíntota vertical cerca de h.

        # Recorremos la cantidad de puntos que tendrá la gráfica.
        for i in range(puntos + 1):
            val_x = inicio + (i * paso)# Calculamos el valor actual de x.

            # Si estamos muy cerca del punto h y queremos marcar asíntota, agregamos un NaN para cortar la línea de la gráfica.
            if marcar_asintota and abs(val_x - h_float) < 0.01:
                x_vals.append(val_x)
                y_vals.append(math.nan)
                continue

            try:
                # Evaluamos la función en val_x.
                y = float(funcion.subs(x, val_x).evalf())

                 # Guardamos los valores en las listas.
                x_vals.append(val_x)
                y_vals.append(y)

            # Si no se puede evaluar en ese punto, simplemente lo omitimos.
            except:
                continue 

        # 4. Validación final
        # Verificamos que exista al menos un valor válido en y_vals, que no sea NaN.
        if not [y for y in y_vals if not math.isnan(y)]:
            raise ValueError("Expresión no válida.")

        # Si todo sale bien, devolvemos un diccionario con toda la información.
        return {
            "exito": True, "limite": str(limite_resultado), "x_vals": x_vals, "y_vals": y_vals,
            "marcar_asintota": marcar_asintota, "h_float": h_float, "tipo_limite": tipo_limite,
            "salto": salto, "lim_izq": lim_izq, "lim_der": lim_der, "punto_exacto": None
        }

    # Si ocurre un error, devolvemos un diccionario indicando fallo y guardando el mensaje del error. 
    except Exception as e:
        return {"exito": False, "error": str(e)}