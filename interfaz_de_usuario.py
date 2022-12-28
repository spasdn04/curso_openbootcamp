import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text='Hola Mundo', bg='yellow', fg='blue')
label_saludo.pack(ipadx=50, ipady=50, fill='both')

label_despido = tkinter.Label(window, text='Adios Mundo', bg='blue', fg='yellow')
label_despido.pack(ipadx=50, ipady=30, fill='y')

window.mainloop()