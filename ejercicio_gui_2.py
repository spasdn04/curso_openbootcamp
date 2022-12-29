#Importamos las librerias necesarias
import tkinter
from tkinter import ttk

#Iniciamos una ventana
window = tkinter.Tk()

#Ponemos un label y lo colocamos con pack()
titulo = ttk.Label(window, 
                   text='Marcas populares de equipos informaticos', 
                   foreground='red'
)
titulo.pack()

#Creamos una lista y le damos un formato que soporte ttk
lista = ['Asus', 'Mac', 'Acer', 'Hp', 'Msi', 'Lenovo']
lista_items = tkinter.StringVar(value=lista)

#Creamos una lista seleccionable y la colocamos con pack()
listbox = tkinter.Listbox(window, 
                          height=10, 
                          width=50, 
                          listvariable=lista_items
)
listbox.pack()

#Hacemos un bucle para que funcione
window.mainloop()