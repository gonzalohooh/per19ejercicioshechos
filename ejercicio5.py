class Complejo():
    def __init__(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def get_suma(self):
        suma = self.numero1 + self.numero2
        return suma

    def get_resta(self):
        resta = self.numero1 - self.numero2
        return resta

    def get_multiplicacion(self):
        multiplicacion = self.numero1*self.numero2
        return multiplicacion

    def get_division(self):
        division = self.numero1/self.numero2
        return division

c = Complejo((1+1j),(1j))
print(c.get_suma(), c.get_resta(), c.get_multiplicacion(), c.get_division())


