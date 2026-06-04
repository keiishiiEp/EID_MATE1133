# Evaluación Integrada de Desempeño (EID) - MATE1133
**Analizador y visualizador de límites matemáticos**

Proyecto desarrollado para la asignatura de Cálculo I (MATE1133) de la Universidad Católica de Temuco . 
Consiste en una plataforma tecnológica de apoyo académico construida íntegramente en Python, diseñada para evaluar límites de forma analítica 
y graficar el comportamiento de las funciones sin el uso de librerías de procesamiento numérico de arreglos.

---
## Características principales
* **Evaluación simbólica:** Resolución analítica de límites matemáticos (incluyendo indeterminaciones y límites al infinito) utilizando el motor algebraico `SymPy`.
* **Visualización gráfica:** Renderizado de curvas matemáticas interactuando directamente con `Matplotlib`, implementando algoritmos nativos para el manejo de asíntotas, recorte dinámico del eje Y (clipping) y discontinuidades de salto.
* **Interfaz de usuario (GUI):** Diseño retro/brutalista implementado con `CustomTkinter`, estructurado bajo el principio de separación de responsabilidades (Modularidad).
* **Restricción técnica cumplida:** El motor de graficación opera al 100% mediante lógica nativa de Python.

---
## Arquitectura del proyecto
El código fuente ha sido modularizado para separar la lógica matemática de la interfaz visual:

* `main.py`: Archivo principal de ejecución. Administra la navegación y los estilos globales de la aplicación.
* `logica.py`: Motor matemático aislado. Recibe strings, evalúa límites laterales y generales con SymPy, y devuelve diccionarios con coordenadas validadas.
* `vista_inicio.py`: Módulo que contiene la estructura visual de la pantalla de bienvenida.
* `vista_graficadora.py`: Módulo que integra los controles de entrada y el Canvas de Matplotlib.

---
## Equipo de desarrollo
* **Keisy D. Epul Landero (https://github.com/keiishiiEp)**
* **María R. Henríquez Cayuqueo (https://github.com/mhenriquez2026-maker)**
* **Josefa I(https://github.com/jduarte2026-hue)**

---
## Requisitos de instalación

Para ejecutar este proyecto localmente, asegúrese de tener Python 3.14 instalado y ejecute el siguiente comando para instalar las dependencias requeridas:

```bash
pip install sympy customtkinter matplotlib
