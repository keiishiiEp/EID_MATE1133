import customtkinter as ctk # Importamos CustomTkinter para crear la interfaz gráfica.

from inicio import crear_pantalla_inicio # Importamos la función que construye la pantalla de inicio.
from graficadora import crear_pantalla_graficadora # Importamos la función que construye la pantalla de la graficadora.

# --- Config ventana principal---
ventana = ctk.CTk() # Creamos la ventana principal.
ventana.geometry("900x700") # Definimos el tamaño inicial de la ventana
ventana.title("Evaluador de Límites") # Asignamos un título a la ventana.
ventana.configure(fg_color="#D1C9D6") # Establecemos el color de fondo.

from inicio import crear_pantalla_inicio
from graficadora import crear_pantalla_graficadora

# --- Config ventana---
ventana = ctk.CTk()
ventana.geometry("900x700")
ventana.title("Evaluador de Límites")
ventana.configure(fg_color="#EDE7F6")

# --- Estilos compartidos ---
fuente_retro = ("Courier New", 13, "bold") # Fuente para textos generales.
fuente_titulo = ("Courier New", 22, "bold") # Fuente para títulos.

# Estilo base para las entradas de texto.
estilo_frame = {"fg_color": "#E8E0F0", "border_width": 3, "border_color": "#7E57C2", "corner_radius": 0}
estilo_boton = {"fg_color": "#D4C5E8", "text_color": "#3B1F6B", "border_width": 2, "border_color": "#7E57C2", "corner_radius": 0, "hover_color": "#B8A9D4", "font": fuente_retro}
estilo_entrada = {"fg_color": "white", "text_color": "black", "border_width": 2, "border_color": "black", "corner_radius": 0, "font": fuente_retro}

# --- Lógica de Navegación ---
def ir_a_graficadora():
    pantalla_inicio.pack_forget() # Ocultamos la pantalla de inicio.
    # Mostramos la pantalla de la graficadora.
    pantalla_graficadora.pack(pady=30, padx=30, fill="both", expand=True)

def regresar_a_inicio():
    pantalla_graficadora.pack_forget() # Ocultamos la pantalla de la graficadora.
    # Volvemos a mostrar la pantalla de inicio.
    pantalla_inicio.pack(pady=30, padx=30, fill="both", expand=True)

# --- Pantallas ---
pantalla_inicio = crear_pantalla_inicio(ventana, ir_a_graficadora, estilo_frame, fuente_titulo, fuente_retro, estilo_boton)
pantalla_graficadora = crear_pantalla_graficadora(ventana, regresar_a_inicio, estilo_frame, estilo_entrada, estilo_boton, fuente_retro)

# Pantalla de inicio por defecto
pantalla_inicio.pack(pady=30, padx=30, fill="both", expand=True)

# Iniciamos la aplicación
ventana.mainloop()
