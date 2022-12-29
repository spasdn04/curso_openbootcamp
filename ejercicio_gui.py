#Importamos las librerias necesarias
import tkinter
from tkinter import ttk

#Creamos la ventana y definimo suna estructura grid con 2 columnas y 4 filas
window = tkinter.Tk()
window.columnconfigure(0, weight=4)
window.columnconfigure(1, weight=1)

#Creamos una variable que soporte tkinter
opcion = tkinter.StringVar(None)

#Creamos la lista de radiobutton y los ordenamos
elemento_1 = ttk.Radiobutton(window, text='Opcion 1', variable=opcion, value=1)
elemento_1.grid(column=0, row=1, padx=5, pady=5)
elemento_2 = ttk.Radiobutton(window, text='Opcion 2', variable=opcion, value=2)
elemento_2.grid(column=0, row=2, padx=5, pady=5)
elemento_3 = ttk.Radiobutton(window, text='Opcion 3', variable=opcion, value=3)
elemento_3.grid(column=0, row=3, padx=5, pady=5)
elemento_4 = ttk.Radiobutton(window, text='Opcion 4', variable=opcion, value=4)
elemento_4.grid(column=0, row=4, padx=5, pady=5)

#Definimos la funcion de reseteo de la variable de la lista anterior
def reset():
    opcion.set(None)

#Definimos y mostramos el boton de reinicio
boton_de_reinicio = tkinter.Button(window, text='Reiniciar', command=reset, fg='green')
boton_de_reinicio.grid(column=1, row=1, padx=5, pady=5)

#Hacemos un bucle para que funcione la ventana
window.mainloop()