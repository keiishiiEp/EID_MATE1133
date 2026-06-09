import customtkinter as ctk
import matplotlib.pyplot as plt
import math

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from logica import procesar_limite

# Crea la pantalla donde el usuario ingresa una función, calcula su límite y visualiza la gráfica resultante.
def crear_pantalla_graficadora(ventana_maestra, comando_volver, estilo_frame, estilo_entrada, estilo_boton, fuente_retro):
    frame = ctk.CTkFrame(ventana_maestra, **estilo_frame)

    # --- Barra superior---
    frame_barra = ctk.CTkFrame(frame, fg_color="black", corner_radius=0, height=30)
    frame_barra.pack(fill="x", padx=2, pady=2)

    # Título de la barra
    lbl_barra = ctk.CTkLabel(frame_barra, text=" Graficar_Limites.exe", font=("Courier New", 12, "bold"), text_color="white")
    lbl_barra.pack(side="left", padx=10)

    # Botón para cerrar o volver a la pantalla anterior
    boton_volver = ctk.CTkButton(frame_barra, text="[X] Cerrar", fg_color="black", text_color="white", hover_color="red", corner_radius=0, border_width=0, font=("Courier New", 12, "bold"), width=80, command=comando_volver)
    boton_volver.pack(side="right")

    
    # =========================================================
    # Función ventana flotante- control de instancia
    # =========================================================
    ventana_guia = None  # Variable rastreadora, guarda la referencia de la ventana guia. 

    # Abre una ventana emergente con ayuda sobre la sintaxis matemática permitida
    def abrir_guia():
        nonlocal ventana_guia # Le dice a Python que use la variable de arriba
        
        # Condición: Si la ventana NO existe o si el usuario ya la cerró...
        if ventana_guia is None or not ventana_guia.winfo_exists():
            # ...entonces la creamos desde cero
            ventana_guia = ctk.CTkToplevel(ventana_maestra)
            ventana_guia.title("guia_sintaxis.txt")
            ventana_guia.geometry("380x360")
            ventana_guia.configure(fg_color="#D1D1D0")
            ventana_guia.attributes('-topmost', True) 

            frame_guia = ctk.CTkFrame(ventana_guia, fg_color="#F4F0E6", border_width=3, border_color="black", corner_radius=0)
            frame_guia.pack(pady=15, padx=15, fill="both", expand=True)

            # Título de la guía
            lbl_tit = ctk.CTkLabel(frame_guia, text="> SINTAXIS MATEMÁTICA", font=("Courier New", 15, "bold"), text_color="black")
            lbl_tit.pack(pady=(15, 10))

            # Texto con ejemplos de funciones y símbolos aceptados
            texto_ayuda = (
                " * Potencia     : ** (Ej: x**2)\n"
                " * Raíz cuad.   : sqrt() (Ej: sqrt(x))\n"
                " * Infinito     : oo     (Letra 'o' x2)\n"
                " * Menos inf.   : -oo\n"
                " * Seno         : sin(x)\n"
                " * Coseno       : cos(x)\n"
                " * Tangente     : tan(x)\n"
                " * Exponencial  : exp(x)\n"
                " * Logaritmo    : log(x)\n"
                " * V. Absoluto  : abs(x)\n"
                " * Número Pi    : pi\n"
            )

            lbl_texto = ctk.CTkLabel(frame_guia, text=texto_ayuda, font=("Courier New", 13), text_color="black", justify="left")
            lbl_texto.pack(pady=5, padx=20, anchor="w")

            # Botón para cerrar la guía
            btn_ok = ctk.CTkButton(frame_guia, text="ENTENDIDO", **estilo_boton, command=ventana_guia.destroy)
            btn_ok.pack(pady=(15, 20))
            
        else:
            # Si la ventana ya existe, simplemente le damos el foco (la iluminamos)
            ventana_guia.focus()

    # Botón Guía en la barra superior
    boton_guia = ctk.CTkButton(frame_barra, text="[?] Guía", fg_color="black", text_color="white", hover_color="#555555", corner_radius=0, border_width=0, font=("Courier New", 12, "bold"), width=80, command=abrir_guia)
    boton_guia.pack(side="right", padx=(0, 5))
    
    
    # =========================================================
    # --- Controles ---

    # Contenedor de los controles de entrada
    frame_controles = ctk.CTkFrame(frame, fg_color="transparent")
    frame_controles.pack(pady=20, padx=20, fill="x")

    # Entrada para la función matemática
    entrada_funcion = ctk.CTkEntry(frame_controles, placeholder_text="f(x)", **estilo_entrada)
    entrada_funcion.pack(side="left", padx=10, expand=True, fill="x")

    # Entrada para el punto h donde se evaluará el límite
    entrada_h = ctk.CTkEntry(frame_controles, placeholder_text="h", width=100, **estilo_entrada)
    entrada_h.pack(side="left", padx=10)

    # Botón que ejecuta el cálculo del límite
    boton_calcular = ctk.CTkButton(frame_controles, text="Ejecutar", **estilo_boton)
    boton_calcular.pack(side="left", padx=10)

    # Etiqueta donde se muestra el resultado o mensajes de error
    etiqueta_resultado = ctk.CTkLabel(frame, text="> Esperando parámetros...", font=fuente_retro, text_color="black")
    etiqueta_resultado.pack(pady=5, anchor="w", padx=30)

    # --- Área gráfico ---
    frame_canvas = ctk.CTkFrame(frame, border_width=3, border_color="black", corner_radius=0)
    frame_canvas.pack(pady=15, padx=30, expand=True, fill="both")

    # Creación de la figura y los ejes del gráfico
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    fig.patch.set_facecolor("#F4F0E6")
    ax.set_facecolor("#F4F0E6")

    # Inserta la figura dentro de la interfaz Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_canvas)
    canvas.get_tk_widget().pack(expand=True, fill="both", padx=2, pady=2)

    # Barra de herramientas de matplotlib para zoom, mover, guardar, etc.
    toolbar = NavigationToolbar2Tk(canvas, frame_canvas)
    toolbar.update()

    # Función interna que procesa los datos ingresados y actualiza la gráfica
    def accion_calcular():  
        h_str = entrada_h.get()
        resultado = procesar_limite(func_str, h_str)
        
        # Si el cálculo fue exitoso, muestra resultado y grafica la función
        if resultado["exito"]:
            etiqueta_resultado.configure(text=f"> Resultado del límite: {resultado['limite']}")
            
            # Limpia el gráfico anterior
            ax.clear()
            ax.set_facecolor("#F4F0E6") 
            fig.patch.set_facecolor("#F4F0E6")
            
            # Dibuja la función
            ax.plot(resultado["x_vals"], resultado["y_vals"], color='black', linewidth=2, label=f'f(x) = {func_str}')
            
            # Si corresponde, marca la recta vertical en x = h
            if resultado["marcar_asintota"]:
                ax.axvline(x=resultado["h_float"], color='red', linestyle='--', linewidth=2, label=f'h = {resultado["h_float"]}')
                
                # Si hay salto, se marcan los límites laterales y el valor exacto si existe
                if resultado["salto"]:
                    ax.plot(resultado["h_float"], resultado["lim_izq"], marker='o', markersize=8, markerfacecolor='#F4F0E6', markeredgecolor='black', linestyle='None')
                    ax.plot(resultado["h_float"], resultado["lim_der"], marker='o', markersize=8, markerfacecolor='#F4F0E6', markeredgecolor='black', linestyle='None')
                    if resultado["punto_exacto"] is not None:
                        ax.plot(resultado["h_float"], resultado["punto_exacto"], marker='o', markersize=8, color='black', linestyle='None')
            
            # Agrega a la leyenda el tipo de límite detectado
            ax.plot([], [], ' ', label=f'Tipo: {resultado["tipo_limite"]}')
            
            # Recorte dinámico
            y_validos = sorted([y for y in resultado["y_vals"] if not math.isnan(y)])
            if y_validos:
                idx_min = int(len(y_validos) * 0.05)
                idx_max = int(len(y_validos) * 0.95)
                y_piso = y_validos[idx_min]
                y_techo = y_validos[idx_max]
                margen = (y_techo - y_piso) * 0.5
                if margen == 0: margen = 10
                ax.set_ylim([y_piso - margen, y_techo + margen])

            # Personalización visual del gráfico
            ax.set_title("COMPORTAMIENTO DE LA FUNCIÓN", fontname="Courier New", fontweight="bold")
            ax.set_xlabel("Eje X", fontname="Courier New")
            ax.set_ylabel("Eje Y", fontname="Courier New")
            
            legend = ax.legend()
            legend.get_frame().set_edgecolor('black')
            legend.get_frame().set_linewidth(2)
            legend.get_frame().set_facecolor('white')
            
            ax.grid(True, color="black", linestyle=":", linewidth=1)
            canvas.draw()
        else:
            # Mensaje mostrado si la expresión ingresada no es válida
            etiqueta_resultado.configure(text="> ERROR: Revisa la expresión.")

    # Asocia el botón con la función de cálculo
    boton_calcular.configure(command=accion_calcular)

    # Retorna el frame completo para ser usado en la ventana principal
    return frame    