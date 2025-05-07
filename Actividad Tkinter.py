# Programa 1: Version original

#Ejecutar el problema elegido por separado ya que tkinter solo permite un tk por ejecucion

#Hasta el final hay una pequeña lista de colores para intercambiar(en el 3er programa).Para cambiar los colores es cuestion de sustituir el color, por ejemplo: (ligthblue).Combiarlo por el color de tu preferencia escrito hasta el final. Es obligatorio cambiar todos los comandos de colores 

import tkinter as tk

def saludar_v1():
    nombre = entrada_v1.get()
    resultado_v1.config(text=f"¡Hola {nombre}!")

ventana1 = tk.Tk()
ventana1.title("Saludo")
ventana1.geometry("300x150")

tk.Label(ventana1, text="Ingresa tu nombre:").pack()
entrada_v1 = tk.Entry(ventana1)
entrada_v1.pack()
tk.Button(ventana1, text="Saludar", command=saludar_v1).pack()
resultado_v1 = tk.Label(ventana1, text="")
resultado_v1.pack()

#Agregar el comando para el primer programa y borrar los demas 
#ventana1.mainloop()


# Programa 2: Cambios de la practica guida



def saludar_v2():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    resultado_v2.config(text=f"Hola {nombre}, tienes {edad} años.")

ventana2 = tk.Tk()
ventana2.title("Cordial saludo y edad")
ventana2.geometry("400x200")

tk.Label(ventana2, text="Dime tu nombre:").pack()
entrada_nombre = tk.Entry(ventana2)
entrada_nombre.pack()
tk.Label(ventana2, text="Dime tu edad:").pack()
entrada_edad = tk.Entry(ventana2)
entrada_edad.pack()
tk.Button(ventana2, text="Mostrar saludo", command=saludar_v2).pack()
resultado_v2 = tk.Label(ventana2, text="")
resultado_v2.pack()


#Agregar el comando para el segundo programa y borrar los demas 
#ventana2.mainloop()



# Programa 3: (color + autor)



def saludar_v3():
    nombre = entrada_nombre3.get()
    edad = entrada_edad3.get()
    resultado_v3.config(text=f"¡Hola {nombre}!, tienes {edad} años")

ventana3 = tk.Tk()
ventana3.title("Saludo con edad y color de tu preferencia")
ventana3.geometry("400x200")
ventana3.config(bg="lightblue")

tk.Label(ventana3, text="Dime tu nombre:", bg="lightblue").pack()
entrada_nombre3 = tk.Entry(ventana3)
entrada_nombre3.pack()
tk.Label(ventana3, text=" Dime tu edad:", bg="lightblue").pack()
entrada_edad3 = tk.Entry(ventana3)
entrada_edad3.pack()
tk.Button(ventana3, text="Mostrar saludo", command=saludar_v3).pack()
resultado_v3 = tk.Label(ventana3, text="", bg="lightblue")
resultado_v3.pack()
tk.Label(ventana3, text="Autor: Tu Nombre", bg="lightblue").pack(side="bottom")

#lightblue
#lightgreen
#lightyellow
#white
#black
#gray
#blue
#red
#green
#orange
#purple
#brown
#cyan
#gold


#Agregar el comando para el tercer programa y borrar los demas 
#ventana3.mainloop()