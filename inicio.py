# Importamos la librería CustomTkinter con el alias ctk para crear la interfaz gráfica con un estilo moderno.
import customtkinter as ctk

# Importamos webbrowser para poder abrir la Wiki del proyecto en el navegador cuando el usuario presione el botón correspondiente.
import webbrowser

# Esta función crea la pantalla de inicio de la aplicación.
def crear_pantalla_inicio(ventana_maestra, comando_iniciar, estilo_frame, fuente_titulo, fuente_retro, estilo_boton):
    # Creamos el frame principal que contendrá todos los elementos de la pantalla de inicio.
    frame = ctk.CTkFrame(ventana_maestra, **estilo_frame)
    

    # --- TÍTULOS ---
    # Creamos la etiqueta del título principal del proyecto.
    titulo_proyecto = ctk.CTkLabel(frame, text="Límites", font=fuente_titulo, text_color="black")
    # Ubicamos el título dentro del frame con separación vertical.
    titulo_proyecto.pack(pady=(30, 5))

    # Creamos una etiqueta con el nombre/código del curso.
    codigo_curso = ctk.CTkLabel(frame, text="[ MATE1133 - Cálculo básico ]", font=fuente_retro, text_color="black")
    # Mostramos la etiqueta debajo del título.
    codigo_curso.pack(pady=(0, 20))


    # --- DESCRIPCIÓN ---
    # Guardamos en una variable un texto descriptivo de la aplicación.
    # Se usan saltos de línea para que se vea ordenado.
    texto_descripcion = (
        "Programa de análisis matemático\n\n"
        "> Herramienta interactiva de apoyo académico.\n"
        "> Permite evaluar límites y visualizar curvas.\n"
        "> Implementado estrictamente en Python."
    )

    # Creamos una etiqueta para mostrar la descripción.
    lbl_descripcion = ctk.CTkLabel(frame, text=texto_descripcion, font=fuente_retro, text_color="black", justify="left")
    # Mostramos la descripción en pantalla.
    lbl_descripcion.pack(pady=10)


    # --- INTEGRANTES ---
    # Creamos un frame interno para agrupar la información de las integrantes/desarrolladoras del proyecto.
    frame_integrantes = ctk.CTkFrame(frame, **estilo_frame)
    # Lo ubicamos con margen vertical y horizontal, y hacemos que ocupe el ancho disponible.
    frame_integrantes.pack(pady=15, padx=50, fill="x")

    # Creamos una etiqueta como subtítulo de la sección de integrantes.
    lbl_titulo_integrantes = ctk.CTkLabel(frame_integrantes, text="> Devs:", font=fuente_retro, text_color="black")
    # La ubicamos alineada a la izquierda.
    lbl_titulo_integrantes.pack(pady=(10, 5), padx=15, anchor="w")

    # Guardamos los nombres de las integrantes en un texto multilínea.
    nombres_integrantes = (
        "  * Keisy D. Epul Landero\n"
        "  * María R. Henríquez Cayuqueo\n"
        "  * Josefa I. Duarte Inostroza"
    )

    # Creamos una etiqueta para mostrar los nombres.
    lbl_nombres = ctk.CTkLabel(frame_integrantes, text=nombres_integrantes, font=fuente_retro, text_color="black", justify="left")
    # Mostramos los nombres alineados a la izquierda.
    lbl_nombres.pack(pady=(0, 10), padx=15, anchor="w")


    # --- ZONA DE BOTONES ---
    # Creamos un frame transparente para colocar los botones.
    frame_botones = ctk.CTkFrame(frame, fg_color="transparent")
    # Lo mostramos debajo de la sección de integrantes.
    frame_botones.pack(pady=15)

    
    # --- Consola simulada ---
    # Creamos una etiqueta que simula una consola.
    # Aquí se mostrarán mensajes de carga para dar una sensación de inicialización del sistema.
    consola = ctk.CTkLabel(
        frame, 
        text=">Sistema en espera de inicio...", 
        font=("Courier New", 12), 
        text_color="#7E57C2", 
        fg_color="black",     
        justify="left", 
        anchor="w", 
        corner_radius=0
    )
    # Mostramos la consola ocupando todo el ancho disponible.
    consola.pack(pady=15, padx=50, ipadx=10, ipady=10, fill="x")


    # --- Lógica animación de carga ---
    # Esta función se ejecuta cuando el usuario presiona "Iniciar".
    def iniciar_con_carga():
        # Deshabilitamos los botones para evitar clics múltiples durante la carga.
        boton_comenzar.configure(state="disabled")
        boton_docs.configure(state="disabled")
        
        # Variable preparada para posible uso futuro.
        texto_base = ""
        
        # Primer paso de la carga.
        def paso1():
            # Mostramos el primer mensaje en la consola.
            consola.configure(text="> Cargando motor algebraico SymPy... [OK]")
            # Esperamos 600 milisegundos y llamamos al siguiente paso.
            ventana_maestra.after(600, paso2)

        # Segundo paso de la carga.   
        def paso2():
            # Agregamos una nueva línea con otro mensaje.
            consola.configure(text="> Cargando motor algebraico SymPy... [OK]\n> Inicializando subsistema gráfico Matplotlib... [OK]")
            # Esperamos 700 milisegundos y llamamos al siguiente paso.
            ventana_maestra.after(700, paso3)

        # Tercer paso de la carga.  
        def paso3():
            # Mostramos un tercer mensaje en la consola.
            consola.configure(text="> Cargando motor algebraico SymPy... [OK]\n> Inicializando subsistema gráfico Matplotlib... [OK]\n> Verificando integridad de módulos... [OK]")
            # Esperamos 500 milisegundos y continuamos.
            ventana_maestra.after(500, paso4)

        # Cuarto y último paso de la carga. 
        def paso4():
            # Mostramos el mensaje final de sistema listo.
            consola.configure(text="> Cargando motor algebraico SymPy... [OK]\n> Inicializando subsistema gráfico Matplotlib... [OK]\n> Verificando integridad de módulos... [OK]\n> Sistema listo para evaluar.")
            # Tras mostrar el último mensaje, esperamos 800ms y cambiamos a la graficadora
            ventana_maestra.after(800, comando_iniciar)
            
            # Restaurar el estado para cuando el usuario decida volver al inicio
            def restaurar_estado():
                # Restauramos el mensaje inicial de la consola.
                consola.configure(text="> Sistema en espera de inicio...")

                # Volvemos a habilitar los botones.
                boton_comenzar.configure(state="normal")
                boton_docs.configure(state="normal")
            
            # Llamamos a la restauración después de 1000 milisegundos.
            ventana_maestra.after(1000, restaurar_estado)

        # Iniciar la secuencia
        paso1()

    # Creamos el botón "Iniciar", cuando se presiona, ejecuta la función iniciar_con_carga.
    boton_comenzar = ctk.CTkButton(frame_botones, text="Iniciar", **estilo_boton, height=40, command=iniciar_con_carga)
    # Mostramos el botón a la izquierda dentro del frame de botones.
    boton_comenzar.pack(side="left", padx=10)
    
    # Esta función abre la Wiki del proyecto en el navegador.
    def abrir_docs():
        webbrowser.open_new("https://github.com/keiishiiEp/EID_MATE1133/wiki")

    # Creamos el botón que abre la Wiki/documentación.
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

    # Mostramos el botón de documentación junto al de iniciar.
    boton_docs.pack(side="left", padx=10)
    
    
    # --- FOOTER INSTITUCIONAL ---
    
     # Creamos un texto al pie de la pantalla con información institucional y la versión del programa.
    footer = ctk.CTkLabel(
        frame, 
        text="Universidad Católica de Temuco | Ingeniería Civil en Informática | build v1.1.1", 
        font=("Courier New", 10), 
        text_color="#555555"
    )

    # Ubicamos el footer en la parte inferior.
    footer.pack(side="bottom", pady=10)

    # Retornamos el frame para que pueda ser usado desde otro archivo.
    return frame