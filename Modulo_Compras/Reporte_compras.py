import sqlite3
import tkinter as tk
from tkinter import messagebox

# Configurar la base de datos
def setup_database():
    conn = sqlite3.connect("compras.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS compras (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fecha TEXT,
                        proveedor TEXT,
                        producto TEXT,
                        cantidad INTEGER,
                        precio REAL
                    )''')
    conn.commit()
    conn.close()

# Función para registrar una compra
def registrar_compra():
    fecha = entry_fecha.get()
    proveedor = entry_proveedor.get()
    producto = entry_producto.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()

    if not (fecha and proveedor and producto and cantidad and precio):
        messagebox.showerror("Error", "Por favor, completa todos los campos")
        return

    try:
        cantidad = int(cantidad)
        precio = float(precio)
    except ValueError:
        messagebox.showerror("Error", "Cantidad debe ser un número entero y Precio un número decimal")
        return

    conn = sqlite3.connect("compras.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO compras (fecha, proveedor, producto, cantidad, precio) VALUES (?, ?, ?, ?, ?)",
                   (fecha, proveedor, producto, cantidad, precio))
    conn.commit()
    conn.close()

    messagebox.showinfo("Éxito", "Compra registrada correctamente")
    limpiar_formulario()

# Limpiar formulario después de registrar la compra
def limpiar_formulario():
    entry_fecha.delete(0, tk.END)
    entry_proveedor.delete(0, tk.END)
    entry_producto.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Registro de Compras")

# Etiquetas y entradas para el formulario
tk.Label(root, text="Fecha (AAAA-MM-DD):").grid(row=0, column=0)
entry_fecha = tk.Entry(root)
entry_fecha.grid(row=0, column=1)

tk.Label(root, text="Proveedor:").grid(row=1, column=0)
entry_proveedor = tk.Entry(root)
entry_proveedor.grid(row=1, column=1)

tk.Label(root, text="Producto:").grid(row=2, column=0)
entry_producto = tk.Entry(root)
entry_producto.grid(row=2, column=1)

tk.Label(root, text="Cantidad:").grid(row=3, column=0)
entry_cantidad = tk.Entry(root)
entry_cantidad.grid(row=3, column=1)

tk.Label(root, text="Precio:").grid(row=4, column=0)
entry_precio = tk.Entry(root)
entry_precio.grid(row=4, column=1)

# Botón para registrar la compra
btn_registrar = tk.Button(root, text="Registrar Compra", command=registrar_compra)
btn_registrar.grid(row=5, columnspan=2)

# Ejecutar la configuración de la base de datos y la interfaz gráfica
setup_database()
root.mainloop()