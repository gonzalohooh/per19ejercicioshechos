class Laboratorio():
    def __init__(self, nombre_laboratorio, inventario):
        self.nombre_laboratorio = nombre_laboratorio
        self.inventario = inventario
    def devuelve_nombre(self):
        return self.nombre_laboratorio
    def devuelve_inventario(self):
        return self.inventario

class Producto():
    def __init__(self, nombre_producto, precio):
        self.precio = precio
        self.nombre_producto = nombre_producto
    def devuelve_nombre(self):
        return self.nombre_producto
    def devuelve_precio(self):
        return self.precio
        
class Medicamento(Producto):
    def __init__(self, nombre_medicamento, precio, cantidad):
        self.nombre_medicamento = nombre_medicamento
        self.precio = precio
        self.cantidad = cantidad
    def calcula_porcentaje(self):
        return self.cantidad

p = Producto('Crema', 10)
print(p.devuelve_precio())
m = Medicamento('Ibuprofeno',2,0.3)
print(m.devuelve_precio())

 
