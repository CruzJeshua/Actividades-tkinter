import tkinter as tk
def saludar ():
    nombre=entrada.get()
    resultado.config(text=f"hola{nombre}, tienes {edad} años")
    
    ventana=tk.Tk()
    ventana.title("saludos")
    ventana.geometry("300x150")
    
    tk.Label(ventana, text="ingresa tu nombre", bg lightblue)
    entrada=tk.Entry(ventana)
    entrada,pack()
    tk.Label(ventana, text="ingresa tu edad", bg lightblue)
    entrada=tk.Entry(ventana)
    entrada,pack()
    tk.Button(ventana, text="mostrar saludo"command=saludar).pack()
    resultado=tk.Label(ventana, text="")
    resultado.pack()
    
    ventana.mainloop()
