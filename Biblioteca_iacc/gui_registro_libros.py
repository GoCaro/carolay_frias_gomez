import tkinter as tk
from tkinter import ttk, messagebox

def registrar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()
    genero = genero_var.get()
    categorias = [cat for cat, var in categoria_vars.items() if var.get()]
    estado = estado_var.get()
    copias = entry_copias.get()
    resumen = text_resumen.get("1.0", tk.END).strip()
    idioma = idioma_var.get()

    print("\n--- LIBRO REGISTRADO ---")
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Año de publicación: {anio}")
    print(f"Género: {genero}")
    print(f"Categorías: {', '.join(categorias)}")
    print(f"Estado: {estado}")
    print(f"Número de copias: {copias}")
    print(f"Resumen: {resumen}")
    print(f"Idioma: {idioma}")
    print("------------------------\n")

    messagebox.showinfo("Registro Exitoso", "Los datos del libro se han registrado en la consola.")

def limpiar_formulario():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)
    genero_var.set(None)
    for var in categoria_vars.values():
        var.set(False)
    estado_var.set("Disponible")
    entry_copias.delete(0, tk.END)
    text_resumen.delete("1.0", tk.END)
    idioma_var.set("Español")

# Crear ventana
ventana = tk.Tk()
ventana.title("Biblioteca SaberX - Registro de Libros")

# ----- Frame: Detalles del libro -----
frame_detalles = tk.LabelFrame(ventana, text="Detalles del Libro")
frame_detalles.pack(padx=10, pady=5, fill="x")

tk.Label(frame_detalles, text="Título:").grid(row=0, column=0, sticky="w")
entry_titulo = tk.Entry(frame_detalles, width=50)
entry_titulo.grid(row=0, column=1)

tk.Label(frame_detalles, text="Autor:").grid(row=1, column=0, sticky="w")
entry_autor = tk.Entry(frame_detalles, width=50)
entry_autor.grid(row=1, column=1)

tk.Label(frame_detalles, text="Año de Publicación:").grid(row=2, column=0, sticky="w")
entry_anio = tk.Entry(frame_detalles, width=20)
entry_anio.grid(row=2, column=1, sticky="w")

# ----- Frame: Género y Categoría -----
frame_genero = tk.LabelFrame(ventana, text="Género y Categoría")
frame_genero.pack(padx=10, pady=5, fill="x")

genero_var = tk.StringVar()
tk.Radiobutton(frame_genero, text="Ficción", variable=genero_var, value="Ficción").grid(row=0, column=0, sticky="w")
tk.Radiobutton(frame_genero, text="No Ficción", variable=genero_var, value="No Ficción").grid(row=0, column=1, sticky="w")

categoria_vars = {
    "Novela": tk.BooleanVar(),
    "Ciencia": tk.BooleanVar(),
    "Historia": tk.BooleanVar(),
    "Biografía": tk.BooleanVar(),
    "Fantasía": tk.BooleanVar(),
}
col = 0
for i, (categoria, var) in enumerate(categoria_vars.items()):
    tk.Checkbutton(frame_genero, text=categoria, variable=var).grid(row=1, column=col, sticky="w")
    col += 1

# ----- Frame: Estado -----
frame_estado = tk.LabelFrame(ventana, text="Estado del Libro")
frame_estado.pack(padx=10, pady=5, fill="x")

estado_var = tk.StringVar(value="Disponible")
tk.Radiobutton(frame_estado, text="Disponible", variable=estado_var, value="Disponible").pack(side="left", padx=10)
tk.Radiobutton(frame_estado, text="Prestado", variable=estado_var, value="Prestado").pack(side="left", padx=10)

# ----- Frame: Número de Copias -----
frame_copias = tk.LabelFrame(ventana, text="Copias Disponibles")
frame_copias.pack(padx=10, pady=5, fill="x")

tk.Label(frame_copias, text="Nº de copias:").grid(row=0, column=0, sticky="w")
entry_copias = tk.Entry(frame_copias, width=10)
entry_copias.grid(row=0, column=1, sticky="w")

# ----- Frame: Resumen -----
frame_resumen = tk.LabelFrame(ventana, text="Resumen del Libro")
frame_resumen.pack(padx=10, pady=5, fill="x")

text_resumen = tk.Text(frame_resumen, height=5)
text_resumen.pack(fill="x", padx=5, pady=5)

# ----- Menú Desplegable: Idioma -----
frame_idioma = tk.LabelFrame(ventana, text="Idioma")
frame_idioma.pack(padx=10, pady=5, fill="x")

idioma_var = tk.StringVar(value="Español")
tk.Label(frame_idioma, text="Seleccionar idioma:").pack(side="left", padx=5)
combo_idioma = ttk.Combobox(frame_idioma, textvariable=idioma_var, values=["Español", "Inglés", "Francés", "Alemán", "Portugués"])
combo_idioma.pack(side="left")

# ----- Botones -----
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Registrar Libro", command=registrar_libro).grid(row=0, column=0, padx=10)
tk.Button(frame_botones, text="Limpiar", command=limpiar_formulario).grid(row=0, column=1, padx=10)

ventana.mainloop()