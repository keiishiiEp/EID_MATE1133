import customtkinter as ctk
import matplotlib.pyplot as plt
import math

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from logica import procesar_limite

def crear_pantalla_graficadora(ventana_maestra, comando_volver, estilo_frame, estilo_entrada, estilo_boton, fuente_retro):
    frame = ctk.CTkFrame(ventana_maestra, **estilo_frame)

    # --- Barra sup---
    frame_barra = ctk.CTkFrame(frame, fg_color="black", corner_radius=0, height=30)
    frame_barra.pack(fill="x", padx=2, pady=2)

    lbl_barra = ctk.CTkLabel(frame_barra, text=" Graficar_Limites.exe", font=("Courier New", 12, "bold"), text_color="white")
    lbl_barra.pack(side="left", padx=10)

    boton_volver = ctk.CTkButton(frame_barra, text="[X] Cerrar", fg_color="black", text_color="white", hover_color="red", corner_radius=0, border_width=0, font=("Courier New", 12, "bold"), width=80, command=comando_volver)
    boton_volver.pack(side="right")

    # --- CONTROLES ---
    frame_controles = ctk.CTkFrame(frame, fg_color="transparent")
    frame_controles.pack(pady=20, padx=20, fill="x")

    entrada_funcion = ctk.CTkEntry(frame_controles, placeholder_text="f(x)", **estilo_entrada)
    entrada_funcion.pack(side="left", padx=10, expand=True, fill="x")

    entrada_h = ctk.CTkEntry(frame_controles, placeholder_text="h", width=100, **estilo_entrada)
    entrada_h.pack(side="left", padx=10)

    boton_calcular = ctk.CTkButton(frame_controles, text="Ejecutar", **estilo_boton)
    boton_calcular.pack(side="left", padx=10)

    etiqueta_resultado = ctk.CTkLabel(frame, text="> Esperando parámetros...", font=fuente_retro, text_color="black")
    etiqueta_resultado.pack(pady=5, anchor="w", padx=30)

    # --- Área gráfico ---
    frame_canvas = ctk.CTkFrame(frame, border_width=3, border_color="black", corner_radius=0)
    frame_canvas.pack(pady=15, padx=30, expand=True, fill="both")

    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    fig.patch.set_facecolor("#F4F0E6")
    ax.set_facecolor("#F4F0E6")

    canvas = FigureCanvasTkAgg(fig, master=frame_canvas)
    canvas.get_tk_widget().pack(expand=True, fill="both", padx=2, pady=2)

    toolbar = NavigationToolbar2Tk(canvas, frame_canvas)
    toolbar.update()

    # --- F interna de cálculo ---
    def accion_calcular():
        func_str = entrada_funcion.get()
        h_str = entrada_h.get()
        resultado = procesar_limite(func_str, h_str)
        
        if resultado["exito"]:
            etiqueta_resultado.configure(text=f"> Resultado del límite: {resultado['limite']}")
            
            ax.clear()
            ax.set_facecolor("#F4F0E6") 
            fig.patch.set_facecolor("#F4F0E6")
            
            ax.plot(resultado["x_vals"], resultado["y_vals"], color='black', linewidth=2, label=f'f(x) = {func_str}')
            
            if resultado["marcar_asintota"]:
                ax.axvline(x=resultado["h_float"], color='red', linestyle='--', linewidth=2, label=f'h = {resultado["h_float"]}')
                
                if resultado["salto"]:
                    ax.plot(resultado["h_float"], resultado["lim_izq"], marker='o', markersize=8, markerfacecolor='#F4F0E6', markeredgecolor='black', linestyle='None')
                    ax.plot(resultado["h_float"], resultado["lim_der"], marker='o', markersize=8, markerfacecolor='#F4F0E6', markeredgecolor='black', linestyle='None')
                    if resultado["punto_exacto"] is not None:
                        ax.plot(resultado["h_float"], resultado["punto_exacto"], marker='o', markersize=8, color='black', linestyle='None')
            
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
            etiqueta_resultado.configure(text="> ERROR: Revisa la expresión.")

    boton_calcular.configure(command=accion_calcular)

    return frame