#Juego de tabla e multiplicar de ley de modulativa

# Importamos la librería tkinter y le asignamos el nombre de tk para poder abreviarla.
import tkinter as tk
# Importamos de forma específica de la librería tkinter font, que sería una tipografía para el diseño de la interfaz, y hacemos una abreviatura.
from tkinter import font as tkFont

# Función para mostrar el resultado en la tabla
# Definimos una función de nombre mostrar_resultado, con tres parámetros: operacion (para la multiplicación), resultado (un número) y color (para darle el color al resultado).
# Usamos la palabra clave 'def' para definir una función, seguido del nombre de la función y entre paréntesis los tres parámetros.
def mostrar_resultado(operacion, resultado, color):
    # resultado_label es un widget de etiqueta en tkinter que usamos para mostrar el texto en una interfaz gráfica. Luego usamos config para modificar las propiedades de la etiqueta.
    # Usamos 'text' como una cadena para crear el texto que muestra la etiqueta. 
    # 'bg=color' establece el color de fondo de la etiqueta.
    resultado_label.config(text=f"{operacion} = {resultado}", bg=color, fg="black")  # Cambiar el fondo y el color del texto del resultado

# Función para oscurecer el color
# Creamos una función que toma el parámetro color, el cual tiene que ser hexadecimal.
def oscurecer_color(color):
    # Debemos convertir el color hexadecimal a componentes RGB
    color = color.lstrip("#")
    # Se obtienen los colores del formato hexadecimal y se pasan a valores decimales usando int con una base de 16.
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)

    # Oscurecer el color
    # Hacemos que los colores se oscurezcan y le decimos que reste 40, asegurándonos de que no pase de 0 para que no se vuelva negativo, ya que después no funcionarían.
    r = max(0, r - 40)  # Disminuir el rojo
    g = max(0, g - 40)  # Disminuir el verde
    b = max(0, b - 40)  # Disminuir el azul

    # Volver a convertir a color hexadecimal
    return f"#{r:02x}{g:02x}{b:02x}"

# Crear la ventana principal
# Creamos una instancia que será la ventana que abrirá la aplicación.
ventana = tk.Tk()
# Le ponemos el título al programa.
ventana.title("Juego de Ley Modulativa")
# Le damos el tamaño de la ventana al abrirla.
ventana.geometry("900x900")
# Establecemos el color de fondo de la ventana.
ventana.configure(bg="#E6E6FA")  # Fondo claro.

# Cambiar la tipografía a una más moderna y redonda
# Declaramos una variable que va a almacenar el objeto de fuente del texto.
# Creamos una nueva fuente con tkFont utilizando la clase Font, y entre paréntesis especificamos la familia, el tamaño y el grosor.
fuente_label = tkFont.Font(family="Montserrat", size=28, weight="bold")

# Crear un marco para la tabla con bordes redondeados (efecto visual)
# Creamos una función para el marco.
# 1) Padre será el elemento donde se colocará el marco, 
# 2) color_fondo será el color de fondo del marco, 
# 3) ancho será la anchura del marco, 
# 4) alto será la altura del marco, 
# y el radio se usará para las esquinas redondeadas.
def crear_marco_redondeado(padre, color_fondo, ancho, alto, radio):
    # Crear un canvas para el marco 
    # Creamos un lienzo donde se va a dibujar el marco, el cual tiene un tamaño definido por el ancho y alto, además de su color de fondo.
    canvas = tk.Canvas(padre, width=ancho, height=alto, bg=color_fondo, highlightthickness=0)
    canvas.pack(pady=20)

    # Dibujar un rectángulo con esquinas redondeadas
    # Creamos las esquinas redondeadas.
    canvas.create_oval(0, 0, radio*2, radio*2, fill=color_fondo, outline=color_fondo)
    canvas.create_oval(0, alto - radio*2, radio*2, alto, fill=color_fondo, outline=color_fondo)
    canvas.create_oval(ancho - radio*2, 0, ancho, radio*2, fill=color_fondo, outline=color_fondo)
    canvas.create_oval(ancho - radio*2, alto - radio*2, ancho, alto, fill=color_fondo, outline=color_fondo)
    
    # Creamos el cuerpo del marco.
    canvas.create_rectangle(radio, 0, ancho - radio, alto, fill=color_fondo, outline=color_fondo)
    canvas.create_rectangle(0, radio, ancho, alto - radio, fill=color_fondo, outline=color_fondo)
    
    # Devolvemos el lienzo que tiene todo dibujado.
    return canvas

# Crear el marco redondeado para el resultado
# Creamos una variable para guardar el valor del lienzo. 
# Usamos la función que ya creamos y le damos los argumentos que se pasan a la función. 
# El marco se dibujará sobre la ventana. 
# Luego le damos el color del marco, seguido del ancho y la altura.
tabla_frame = crear_marco_redondeado(ventana, "#E6E6FA", 760, 100, 20)

# Etiqueta para el resultado
# Creamos la etiqueta (label) que mostrará el resultado.
# La etiqueta estará en el marco de la tabla.
# Mostrará el texto "Resultado: ".
# Se le asigna un fondo blanco para la etiqueta y se establece la fuente para el estilo.
# Las dimensiones de la etiqueta serán un ancho de 30 y una altura de 4.
resultado_label = tk.Label(tabla_frame, text="Resultado: ", font=fuente_label, bg="#E6E6FA", fg="black", width=30, height=4)
# Se agrega un espacio vertical de 5 píxeles entre la etiqueta y otros componentes.
resultado_label.pack(pady=5)

# Crear un marco para los botones
# Se crea un marco para los botones, que se añade a la ventana principal y se le asigna un color de fondo.
# Se utiliza el método pack() para mostrar el marco en la ventana y se añade un espacio vertical alrededor del marco con pady.
marco_botones = tk.Frame(ventana, bg="#E6E6FA")
marco_botones.pack(pady=20)

# Lista de operaciones con colores asignados
# Creamos la tupla operaciones colores y le damos a cada tabla un color igual. 
# Al comienzo tiene un valor y luego el valor del color
operaciones_colores = [
    ((2, 2), "#A2DFF7"),  # 2 × 2 (Azul Pastel)
    ((6, 6), "#FFB3BA"),  # 6 × 6 (Rosa Pastel)
    ((2, 3), "#A2DFF7"),  # 2 × 3 (Azul Pastel)
    ((2, 8), "#A2DFF7"),  # 2 × 8 (Azul Pastel)
    ((3, 7), "#FFC3A0"),  # 3 × 7 (Coral Pastel)
    ((4, 7), "#BFD3C1"),  # 4 × 7 (Verde Pastel)
    ((5, 4), "#FFF5BA"),  # 5 × 4 (Amarillo Pastel)
    ((5, 9), "#FFF5BA"),  # 5 × 9 (Amarillo Pastel)
    ((6, 9), "#FFB3BA"),  # 6 × 9 (Rosa Pastel)
    ((3, 3), "#FFC3A0"),  # 3 × 3 (Coral Pastel)
    ((7, 7), "#FFDAC1"),  # 7 × 7 (Durazno Pastel)
    ((2, 4), "#A2DFF7"),  # 2 × 4 (Azul Pastel)
    ((2, 9), "#A2DFF7"),  # 2 × 9 (Azul Pastel)
    ((3, 8), "#FFC3A0"),  # 3 × 8 (Coral Pastel)
    ((4, 8), "#BFD3C1"),  # 4 × 8 (Verde Pastel)
    ((5, 6), "#FFF5BA"),  # 5 × 6 (Amarillo Pastel)
    ((6, 4), "#FFB3BA"),  # 6 × 4 (Rosa Pastel)
    ((7, 8), "#FFDAC1"),  # 7 × 8 (Durazno Pastel)
    ((4, 4), "#BFD3C1"),  # 4 × 4 (Verde Pastel)
    ((8, 8), "#FFB3E0"),  # 8 × 8 (Rosa Claro)
    ((2, 6), "#A2DFF7"),  # 2 × 6 (Azul Pastel)
    ((3, 4), "#FFC3A0"),  # 3 × 4 (Coral Pastel)
    ((3, 9), "#FFC3A0"),  # 3 × 9 (Coral Pastel)
    ((5, 2), "#FFF5BA"),  # 5 × 2 (Amarillo Pastel)
    ((5, 7), "#FFF5BA"),  # 5 × 7 (Amarillo Pastel)
    ((6, 7), "#FFB3BA"),  # 6 × 7 (Rosa Pastel)
    ((7, 9), "#FFDAC1"),  # 7 × 9 (Durazno Pastel)
    ((5, 5), "#FFF5BA"),  # 5 × 5 (Amarillo Pastel)
    ((9, 9), "#FFE6CC"),  # 9 × 9 (Beige Pastel)
    ((2, 7), "#A2DFF7"),  # 2 × 7 (Azul Pastel)
    ((3, 6), "#FFC3A0"),  # 3 × 6 (Coral Pastel)
    ((4, 6), "#BFD3C1"),  # 4 × 6 (Verde Pastel)
    ((5, 3), "#FFF5BA"),  # 5 × 3 (Amarillo Pastel)
    ((5, 8), "#FFF5BA"),  # 5 × 8 (Amarillo Pastel)
    ((6, 8), "#FFB3BA"),  # 6 × 8 (Rosa Pastel)
    ((8, 9), "#FFB3E0"),  # 8 × 9 (Rosa Claro)
]


# Función para animar los botones al presionar
# Esta funcion es para cuando activan el boton. Pone el color original del boton mas oscuro. 
def on_press(event):
    original_color = event.widget.cget("bg")
    event.widget.config(bg=oscurecer_color(original_color))

# La animacion del boton cuando lo aprietas.
def on_release(event, color):
    event.widget.config(bg=color)

# Crear botones para las operaciones en filas de 9 columnas y 4 filas
# Se usa para crear un boton. Los colores y el orden.
for i, ((op1, op2), color) in enumerate(operaciones_colores):
    boton = tk.Button(marco_botones, text=f"{op1} × {op2}", font=("Montserrat", 16, "bold"), width=10, height=3,
                      command=lambda op1=op1, op2=op2, color=color: mostrar_resultado(f"{op1} × {op2}", op1 * op2, color),
                      bg=color, fg="black", activebackground=color, relief="flat")  # Color activo igual al de fondo

    # Asignar eventos para la animación
    boton.bind("<ButtonPress>", on_press)
    boton.bind("<ButtonRelease>", lambda event, color=color: on_release(event, color))
    
    # Colocar en una cuadrícula de 9 columnas
    boton.grid(row=i // 9, column=i % 9, padx=5, pady=5)


# Iniciar el bucle de la aplicación
ventana.mainloop()
