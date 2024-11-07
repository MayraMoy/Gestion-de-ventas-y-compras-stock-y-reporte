import sqlite3
import tkinter as tk
from tkinter import messagebox

# Configurar la base de datos
def setup_database():
    conn = sqlite3.connect("compras.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        stock_actual INTEGER,
                        stock_minimo INTEGER
                    )''')
    conn.commit()
    conn.close()

# Función para verificar el stock
def verificar_stock():
    conn = sqlite3.connect("compras.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, stock_actual, stock_minimo FROM productos")
    productos = cursor.fetchall()
    conn.close()

    for producto in productos:
        id_producto, nombre, stock_actual, stock_minimo = producto
        if stock_actual < stock_minimo:
            # Alerta de bajo stock
            messagebox.showwarning("Alerta de Stock Bajo", f"El producto '{nombre}' está por debajo del stock mínimo.\nStock actual: {stock_actual}\nStock mínimo: {stock_minimo}")
            generar_orden_compra(nombre, stock_minimo - stock_actual)

# Función para generar una orden de compra
def generar_orden_compra(nombre_producto, cantidad_necesaria):
    # Aquí podrías registrar la orden en una base de datos o archivo, o notificar al responsable de compras
    conn = sqlite3.connect("compras.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ordenes_compra (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        producto TEXT,
                        cantidad INTEGER,
                        estado TEXT
                    )''')
    cursor.execute("INSERT INTO ordenes_compra (producto, cantidad, estado) VALUES (?, ?, ?)",
                   (nombre_producto, cantidad_necesaria, "Pendiente"))
    conn.commit()
    conn.close()
    messagebox.showinfo("Orden de Compra Generada", f"Se generó una orden de compra para el producto '{nombre_producto}' por {cantidad_necesaria} unidades.")

# Función para agregar un nuevo producto (para probar el sistema)
def agregar_producto():
    nombre = entry_nombre.get()
    stock_actual = entry_stock_actual.get()
    stock_minimo = entry_stock_minimo.get()

    if not (nombre and stock_actual and stock_minimo):
        messagebox.showerror("Error", "Por favor, completa todos los campos")
        return

    try:
        stock_actual = int(stock_actual)
        stock_minimo = int(stock_minimo)
    except ValueError:
        messagebox.showerror("Error", "El stock debe ser un número entero")
        return

    conn = sqlite3.connect("compras.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, stock_actual, stock_minimo) VALUES (?, ?, ?)",
                   (nombre, stock_actual, stock_minimo))
    conn.commit()
    conn.close()

    messagebox.showinfo("Éxito", "Producto agregado correctamente")
    limpiar_formulario()

# Limpiar formulario después de agregar un producto
def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_stock_actual.delete(0, tk.END)
    entry_stock_minimo.delete(0, tk.END)

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Automatización de Pedidos")

# Etiquetas y entradas para el formulario de nuevo producto
tk.Label(root, text="Nombre del Producto:").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Stock Actual:").grid(row=1, column=0)
entry_stock_actual = tk.Entry(root)
entry_stock_actual.grid(row=1, column=1)

tk.Label(root, text="Stock Mínimo:").grid(row=2, column=0)
entry_stock_minimo = tk.Entry(root)
entry_stock_minimo.grid(row=2, column=1)

# Botones para agregar producto y verificar stock
btn_agregar = tk.Button(root, text="Agregar Producto", command=agregar_producto)
btn_agregar.grid(row=3, column=0, columnspan=2)

btn_verificar_stock = tk.Button(root, text="Verificar Stock", command=verificar_stock)
btn_verificar_stock.grid(row=4, column=0, columnspan=2)

# Ejecutar la configuración de la base de datos y la interfaz gráfica
setup_database()
root.mainloop()