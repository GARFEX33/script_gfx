import os
import tkinter as tk
from tkinter import filedialog, messagebox

def create_project_structure(base_directory, project_name):
    # Define the base directory based on the provided project name
    project_directory = os.path.join(base_directory, project_name)

    # Define the structure of the directories within the project
    directories = [
        f"{project_directory}/domain/entities",
        f"{project_directory}/domain/ports",
        f"{project_directory}/domain/services",
        f"{project_directory}/application/use_cases",
        f"{project_directory}/application/interfaces/adapters",
        f"{project_directory}/application/interfaces/ports",
        f"{project_directory}/infrastructure/persistence",
        f"{project_directory}/infrastructure/api/Controllers",
        f"{project_directory}/infrastructure/external_services"
    ]

    # Create the directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Return a confirmation message
    return f"All directories for project '{project_name}' have been created successfully."

def seleccionar_directorio():
    directorio = filedialog.askdirectory()
    directorio_entrada.delete(0, tk.END)
    directorio_entrada.insert(0, directorio)

def ejecutar_script():
    base_directory = directorio_entrada.get()
    project_name = nombre_proyecto_entrada.get()

    if os.path.exists(base_directory) and os.path.isdir(base_directory):
        mensaje = create_project_structure(base_directory, project_name)
        messagebox.showinfo("Éxito", mensaje)
    else:
        messagebox.showerror("Error", f"No se encontró el directorio '{base_directory}'.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Crear Estructura de Proyecto")

# Etiqueta y entrada para el directorio base
tk.Label(ventana, text="Directorio base:").grid(row=0, column=0, padx=10, pady=5)
directorio_entrada = tk.Entry(ventana, width=50)
directorio_entrada.grid(row=0, column=1, padx=10, pady=5)
tk.Button(ventana, text="Seleccionar", command=seleccionar_directorio).grid(row=0, column=2, padx=10, pady=5)

# Etiqueta y entrada para el nombre del proyecto
tk.Label(ventana, text="Nombre del proyecto:").grid(row=1, column=0, padx=10, pady=5)
nombre_proyecto_entrada = tk.Entry(ventana, width=50)
nombre_proyecto_entrada.grid(row=1, column=1, padx=10, pady=5)

# Botón para ejecutar el script
tk.Button(ventana, text="Crear Proyecto", command=ejecutar_script).grid(row=2, column=1, padx=10, pady=20)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
