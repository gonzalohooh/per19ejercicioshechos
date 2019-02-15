class Figura(object):   #Clase abstracta, no sabe hacer nada
    def __init__(self):
        return

    def calcular_area(self):
        print('No tiene área')
        return
    def calcular_perimetro(self):
        print('No tiene perímetro')
        return

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcular_area(self):
        area = self.lado**2
        return area
    def calcular_perimetro(self):
        perimetro=4*self.lado
        return perimetro

c = Cuadrado(6)
print(c.calcular_area())
print(c.calcular_perimetro())
d = Figura()
print(d.calcular_area())
