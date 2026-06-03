import customtkinter as ctk

def crear_pantalla_inicio(ventana_maestra, comando_iniciar, estilo_frame, fuente_titulo, fuente_retro, estilo_boton):
    frame = ctk.CTkFrame(ventana_maestra, **estilo_frame)
    
    titulo_proyecto = ctk.CTkLabel(frame, text="Límites", font=fuente_titulo, text_color="black")
    titulo_proyecto.pack(pady=(40, 10))

    codigo_curso = ctk.CTkLabel(frame, text="[ MATE1133 - Cálculo básico ]", font=fuente_retro, text_color="black")
    codigo_curso.pack(pady=(0, 30))

    texto_descripcion = (
        "Programa de análisis matemático\n\n"
        "> Herramienta interactiva de apoyo académico.\n"
        "> Permite evaluar límites y visualizar curvas.\n"
        "> Implementado estrictamente en Python."
    )
    lbl_descripcion = ctk.CTkLabel(frame, text=texto_descripcion, font=fuente_retro, text_color="black", justify="left")
    lbl_descripcion.pack(pady=20)

    frame_integrantes = ctk.CTkFrame(frame, **estilo_frame)
    frame_integrantes.pack(pady=30, padx=50, fill="x")

    lbl_titulo_integrantes = ctk.CTkLabel(frame_integrantes, text="> Devs:", font=fuente_retro, text_color="black")
    lbl_titulo_integrantes.pack(pady=(15, 5), padx=15, anchor="w")

    nombres_integrantes = (
        "  * Keisy D. Epul Landero\n"
        "  * María R. Henríquez Cayuqueo\n"
        "  * Josefa I. Duarte Inostroza"
    )
    lbl_nombres = ctk.CTkLabel(frame_integrantes, text=nombres_integrantes, font=fuente_retro, text_color="black", justify="left")
    lbl_nombres.pack(pady=(0, 15), padx=15, anchor="w")

    boton_comenzar = ctk.CTkButton(frame, text="Iniciar", **estilo_boton, height=40, command=comando_iniciar)
    boton_comenzar.pack(pady=(20, 40))

    return frame