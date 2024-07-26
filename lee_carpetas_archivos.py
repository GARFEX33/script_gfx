import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Variables a necesitar
directorio = ""
archivo_salida = ""

def listar_directorio_y_guardar_markdown(directorio, archivo_salida):
    with open(archivo_salida, 'w', encoding='utf-8') as salida:
        for root, dirs, files in os.walk(directorio):
            salida.write(f"\n## Directorio: `{root}`\n\n")
            salida.write("### Carpetas:\n")
            for dir in dirs:
                salida.write(f"- {dir}\n")
            salida.write("\n### Archivos:\n")
            for file in files:
                if file.endswith('.py') or file.endswith('.dart'):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, directorio)
                    salida.write(f"\n#### Contenido de: `{relative_path}`\n\n")
                    salida.write("```\n")
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            salida.write(f.read() + "\n")
                    except (UnicodeDecodeError, IOError) as e:
                        salida.write(f"Error leyendo el archivo {file_path}: {e}\n")
                    salida.write("```\n")
            salida.write("\n")

def seleccionar_directorio():
    global directorio
    directorio = filedialog.askdirectory()
    directorio_entrada.delete(0, tk.END)
    directorio_entrada.insert(0, directorio)

def ejecutar_script():
    global directorio, archivo_salida
    directorio = directorio_entrada.get()
    archivo_salida = archivo_salida_entrada.get() + ".md"

    if os.path.exists(directorio) and os.path.isdir(directorio):
        listar_directorio_y_guardar_markdown(directorio, archivo_salida)
        messagebox.showinfo("Éxito", f"La información del directorio ha sido exportada a {archivo_salida} en formato Markdown.")
    else:
        messagebox.showerror("Error", f"No se encontró el directorio '{directorio}'.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Exportar Directorio a Markdown")

# Etiqueta y entrada para el directorio
tk.Label(ventana, text="Directorio:").grid(row=0, column=0, padx=10, pady=5)
directorio_entrada = tk.Entry(ventana, width=50)
directorio_entrada.grid(row=0, column=1, padx=10, pady=5)
tk.Button(ventana, text="Seleccionar", command=seleccionar_directorio).grid(row=0, column=2, padx=10, pady=5)

# Etiqueta y entrada para el archivo de salida
tk.Label(ventana, text="Nombre del archivo de salida:").grid(row=1, column=0, padx=10, pady=5)
archivo_salida_entrada = tk.Entry(ventana, width=50)
archivo_salida_entrada.grid(row=1, column=1, padx=10, pady=5)

# Botón para ejecutar el script
tk.Button(ventana, text="Ejecutar", command=ejecutar_script).grid(row=2, column=1, padx=10, pady=20)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
