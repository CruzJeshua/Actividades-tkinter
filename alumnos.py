import tkinter as tk

estudiantes = {}

def mostrar_datos():
    texto = "Datos de los estudiantes:\n"
    for numero, datos in estudiantes.items():
        texto += f"Estudiante {numero} - Calificacion: {datos['calificacion']}, Sexo: {datos['sexo']}\n"
    etiqueta.config(text=texto)

ventana = tk.Tk()
ventana.title("Estudiantes")
ventana.geometry("400x300")

tk.Label(ventana, text="Numero de estudiante:").pack()
entrada_numero = tk.Entry(ventana)
entrada_numero.pack()

tk.Label(ventana, text="Calificacion:").pack()
entrada_calificacion = tk.Entry(ventana)
entrada_calificacion.pack()

tk.Label(ventana, text="Sexo (M/F):").pack()
entrada_sexo = tk.Entry(ventana)
entrada_sexo.pack()

def agregar_estudiante():
    if len(estudiantes) >= 3:
        etiqueta.config(text="Ya se ingresaron 3 estudiantes.")
        return

    numero = entrada_numero.get()
    try:
        calificacion = float(entrada_calificacion.get())
    except ValueError:
        etiqueta.config(text="La calificacion debe ser un numero.")
        return
    sexo = entrada_sexo.get().upper()

    if numero and sexo in ["M", "F"]:
        estudiantes[numero] = {
            "calificacion": calificacion,
            "sexo": sexo
        }
        etiqueta.config(text=f"Estudiante {numero} agregado.")
        entrada_numero.delete(0, tk.END)
        entrada_calificacion.delete(0, tk.END)
        entrada_sexo.delete(0, tk.END)
    else:
        etiqueta.config(text="Datos invalidos. Revisa los campos.")

tk.Button(ventana, text="Agregar estudiante", command=agregar_estudiante).pack(pady=5)
tk.Button(ventana, text="Mostrar datos", command=mostrar_datos).pack(pady=5)

etiqueta = tk.Label(ventana, text="", justify="left")
etiqueta.pack(pady=10)

ventana.mainloop()