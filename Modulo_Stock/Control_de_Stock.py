class Producto:
    """
    Representa un producto en el inventario.
    """

    def __init__(self, nombre, codigo, stock_inicial):
        """
        Inicializa un nuevo producto.

        Args:
            nombre (str): El nombre del producto.
            codigo (str): El código del producto.
            stock_inicial (int): El stock inicial del producto.
        """
        self.nombre = nombre
        self.codigo = codigo
        self.stock = stock_inicial

    def actualizar_stock(self, cantidad):
        """
        Actualiza el stock del producto.

        Args:
            cantidad (int): La cantidad a agregar o restar del stock.
        """
        self.stock += cantidad

    def __str__(self):
        """
        Devuelve una representación en cadena del producto.
        """
        return f"Nombre: {self.nombre}, Código: {self.codigo}, Stock: {self.stock}"


class Inventario:
    """
    Representa el inventario de productos.
    """

    def __init__(self):
        """
        Inicializa un nuevo inventario.
        """
        self.productos = {}

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario.

        Args:
            producto (Producto): El producto a agregar.
        """
        self.productos[producto.codigo] = producto

    def obtener_producto(self, codigo):
        """
        Obtiene un producto del inventario por su código.

        Args:
            codigo (str): El código del producto.

        Returns:
            Producto: El producto con el código dado, o None si no se encuentra.
        """
        return self.productos.get(codigo)

    def actualizar_stock(self, codigo, cantidad):
        """
        Actualiza el stock de un producto.

        Args:
            codigo (str): El código del producto.
            cantidad (int): La cantidad a agregar o restar del stock.
        """
        producto = self.obtener_producto(codigo)
        if producto:
            producto.actualizar_stock(cantidad)
        else:
            print(f"Error: Producto con código '{codigo}' no encontrado.")

    def mostrar_inventario(self):
        """
        Muestra el inventario completo.
        """
        print("Inventario:")
        for producto in self.productos.values():
            print(producto)


# Ejemplo de uso
inventario = Inventario()

# Agregar productos al inventario
inventario.agregar_producto(Producto("Camiseta", "C001", 100))
inventario.agregar_producto(Producto("Pantalón", "P002", 50))

# Mostrar el inventario inicial
inventario.mostrar_inventario()

# Actualizar el stock de un producto
inventario.actualizar_stock("C001", -20)  # Se venden 20 camisetas

# Mostrar el inventario actualizado
inventario.mostrar_inventario()
