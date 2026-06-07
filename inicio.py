import customtkinter as ctk
import webbrowser

def crear_pantalla_inicio(ventana_maestra, comando_iniciar, estilo_frame, fuente_titulo, fuente_retro, estilo_boton):
    frame = ctk.CTkFrame(ventana_maestra, **estilo_frame)
    
    # --- TÍTULOS ---
    titulo_proyecto = ctk.CTkLabel(frame, text="Límites", font=fuente_titulo, text_color="black")
    titulo_proyecto.pack(pady=(30, 5))

    codigo_curso = ctk.CTkLabel(frame, text="[ MATE1133 - Cálculo básico ]", font=fuente_retro, text_color="black")
    codigo_curso.pack(pady=(0, 20))

    # --- DESCRIPCIÓN ---
    texto_descripcion = (
        "Programa de análisis matemático\n\n"
        "> Herramienta interactiva de apoyo académico.\n"
        "> Permite evaluar límites y visualizar curvas.\n"
        "> Implementado estrictamente en Python."
    )
    lbl_descripcion = ctk.CTkLabel(frame, text=texto_descripcion, font=fuente_retro, text_color="black", justify="left")
    lbl_descripcion.pack(pady=10)

    # --- INTEGRANTES ---
    frame_integrantes = ctk.CTkFrame(frame, **estilo_frame)
    frame_integrantes.pack(pady=15, padx=50, fill="x")

    lbl_titulo_integrantes = ctk.CTkLabel(frame_integrantes, text="> Devs:", font=fuente_retro, text_color="black")
    lbl_titulo_integrantes.pack(pady=(10, 5), padx=15, anchor="w")

    nombres_integrantes = (
        "  * Keisy D. Epul Landero\n"
        "  * María R. Henríquez Cayuqueo\n"
        "  * Josefa I. Duarte Inostroza"
    )
    lbl_nombres = ctk.CTkLabel(frame_integrantes, text=nombres_integrantes, font=fuente_retro, text_color="black", justify="left")
    lbl_nombres.pack(pady=(0, 10), padx=15, anchor="w")

    # --- ZONA DE BOTONES ---
    frame_botones = ctk.CTkFrame(frame, fg_color="transparent")
    frame_botones.pack(pady=15)

    
    # --- Consola simulada ---
    consola = ctk.CTkLabel(
        frame, 
        text=">Sistema en espera de inicio...", 
        font=("Courier New", 12), 
        text_color="#00FF00", 
        fg_color="black",     
        justify="left", 
        anchor="w", 
        corner_radius=0
    )
    consola.pack(pady=15, padx=50, ipadx=10, ipady=10, fill="x")

    # --- Lógica animación de carga ---
    def iniciar_con_carga():
        # Deshabilitamos los botones para evitar clics múltiples durante la carga
        boton_comenzar.configure(state="disabled")
        boton_docs.configure(state="disabled")
        
        texto_base = ""
        
        def paso1():
            consola.configure(text="> Cargando motor algebraico SymPy... [OK]")
            ventana_maestra.after(600, paso2)
            
        def paso2():
            consola.configure(text="> Cargando motor algebraico SymPy... [OK]\n> Inicializando subsistema gráfico Matplotlib... [OK]")
            ventana_maestra.after(700, paso3)
            
        def paso3():
            consola.configure(text="> Cargando motor algebraico SymPy... [OK]\n> Inicializando subsistema gráfico Matplotlib... [OK]\n> Verificando integridad de módulos... [OK]")
            ventana_maestra.after(500, paso4)
            
        def paso4():
            consola.configure(text="> Cargando motor algebraico SymPy... [OK]\n> Inicializando subsistema gráfico Matplotlib... [OK]\n> Verificando integridad de módulos... [OK]\n> Sistema listo para evaluar.")
            # Tras mostrar el último mensaje, esperamos 800ms y cambiamos a la graficadora
            ventana_maestra.after(800, comando_iniciar)
            
            # Restaurar el estado para cuando el usuario decida volver al inicio
            def restaurar_estado():
                consola.configure(text="> Sistema en espera de inicio...")
                boton_comenzar.configure(state="normal")
                boton_docs.configure(state="normal")
            
            ventana_maestra.after(1000, restaurar_estado)

        # Iniciar la secuencia
        paso1()

    boton_comenzar = ctk.CTkButton(frame_botones, text="Iniciar", **estilo_boton, height=40, command=iniciar_con_carga)
    boton_comenzar.pack(side="left", padx=10)
    def abrir_docs():
        webbrowser.open_new("https://github.com/keiishiiEp/EID_MATE1133/wiki")

    boton_docs = ctk.CTkButton(
        frame_botones, 
        text="[ Wiki ]", 
        fg_color="black", 
        text_color="white", 
        hover_color="#333333", 
        corner_radius=0, 
        border_width=2, 
        border_color="black", 
        font=fuente_retro, 
        height=40, 
        command=abrir_docs
    )
    boton_docs.pack(side="left", padx=10)
    
    
    # --- FOOTER INSTITUCIONAL ---
    footer = ctk.CTkLabel(
        frame, 
        text="Universidad Católica de Temuco | Ingeniería Civil en Informática | build v1.1.0", 
        font=("Courier New", 10), 
        text_color="#555555"
    )
    footer.pack(side="bottom", pady=10)

    return frame