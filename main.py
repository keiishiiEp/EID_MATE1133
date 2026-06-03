import customtkinter as ctk

from inicio import crear_pantalla_inicio
from graficadora import crear_pantalla_graficadora

# --- Config ventana---
ventana = ctk.CTk()
ventana.geometry("900x700")
ventana.title("Evaluador de Límites")
ventana.configure(fg_color="#D1C9D6")

# --- Estilos ---
fuente_retro = ("Courier New", 13, "bold")
fuente_titulo = ("Courier New", 22, "bold")

estilo_frame = {"fg_color": "#D1D1D0", "border_width": 3, "border_color": "black", "corner_radius": 0}
estilo_boton = {"fg_color": "#EAE4E9", "text_color": "black", "border_width": 2, "border_color": "black", "corner_radius": 0, "hover_color": "#C4BCC9", "font": fuente_retro}
estilo_entrada = {"fg_color": "white", "text_color": "black", "border_width": 2, "border_color": "black", "corner_radius": 0, "font": fuente_retro}

# --- Logica de Nav ---
def ir_a_graficadora():
    pantalla_inicio.pack_forget()
    pantalla_graficadora.pack(pady=30, padx=30, fill="both", expand=True)

def regresar_a_inicio():
    pantalla_graficadora.pack_forget()
    pantalla_inicio.pack(pady=30, padx=30, fill="both", expand=True)

# --- Pantallas ---
pantalla_inicio = crear_pantalla_inicio(ventana, ir_a_graficadora, estilo_frame, fuente_titulo, fuente_retro, estilo_boton)
pantalla_graficadora = crear_pantalla_graficadora(ventana, regresar_a_inicio, estilo_frame, estilo_entrada, estilo_boton, fuente_retro)

# Pantalla de inicio por defecto
pantalla_inicio.pack(pady=30, padx=30, fill="both", expand=True)

# Iniciamos la aplicación
ventana.mainloop()