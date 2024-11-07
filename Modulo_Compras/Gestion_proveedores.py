import sqlite3
import tkinter as tk
from tkinter import messagebox

# Configurar la base de datos
def setup_database():
    conn = sqlite3.connect("compras.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS proveedores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        contacto TEXT,
                        productos TEXT
                    )''')
    conn.commit()
    conn.close()

# Función para agregar un proveedor
def agregar_proveedor():
    nombre = entry_nombre.get()
    contacto = entry_contacto.get()
    productos = entry_productos.get()

    if not (nombre and contacto and productos):
        messagebox.showerror("Error", "Por favor, completa todos los campos")
        return

    conn = sqlite3.connect("compras.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO proveedores (nombre, contacto, productos) VALUES (?, ?, ?)",
                   (nombre, contacto, productos))
    conn.commit()
    conn.close()

    messagebox.showinfo("Éxito", "Proveedor agregado correctamente")
    limpiar_formulario()
    actualizar_lista_proveedores()

# Función para eliminar un proveedor seleccionado
def eliminar_proveedor():
    try:
        selected_item = listbox_proveedores.curselection()[0]
        proveedor_id = listbox_proveedores.get(selected_item).split(" ")[0]  # Obtener el ID del proveedor

        conn = sqlite3.connect("compras.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM proveedores WHERE id = ?", (proveedor_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Éxito", "Proveedor eliminado correctamente")
        actualizar_lista_proveedores()
    except IndexError:
        messagebox.showerror("Error", "Selecciona un proveedor para eliminar")

# Función para actualizar la lista de proveedores en la interfaz
def actualizar_lista_proveedores():
    listbox_proveedores.delete(0, tk.END)
    conn = sqlite3.connect("compras.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, contacto FROM proveedores")
    proveedores = cursor.fetchall()
    conn.close()
    for proveedor in proveedores:
        listbox_proveedores.insert(tk.END, f"{proveedor[0]} - {proveedor[1]} (Contacto: {proveedor[2]})")

# Limpiar formulario después de agregar o editar un proveedor
def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_contacto.delete(0, tk.END)
    entry_productos.delete(0, tk.END)

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Gestión de Proveedores")

# Etiquetas y entradas para el formulario
tk.Label(root, text="Nombre del Proveedor:").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Contacto:").grid(row=1, column=0)
entry_contacto = tk.Entry(root)
entry_contacto.grid(row=1, column=1)

tk.Label(root, text="Productos Suministrados:").grid(row=2, column=0)
entry_productos = tk.Entry(root)
entry_productos.grid(row=2, column=1)

# Botones para agregar y eliminar proveedores
btn_agregar = tk.Button(root, text="Agregar Proveedor", command=agregar_proveedor)
btn_agregar.grid(row=3, column=0, columnspan=2)

btn_eliminar = tk.Button(root, text="Eliminar Proveedor", command=eliminar_proveedor)
btn_eliminar.grid(row=4, column=0, columnspan=2)

# Lista de proveedores
tk.Label(root, text="Lista de Proveedores:").grid(row=5, column=0, columnspan=2)
listbox_proveedores = tk.Listbox(root, width=50)
listbox_proveedores.grid(row=6, column=0, columnspan=2)

# Ejecutar la configuración de la base de datos y la interfaz gráfica
setup_database()
actualizar_lista_proveedores()
root.mainloop()


