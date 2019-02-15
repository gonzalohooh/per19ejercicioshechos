from fractions import Fraction
class Fraccion():
    def __init__(self,numerador1,divisor1,numerador2,divisor2):
        self.numerador1 = numerador1
        self.divisor1 = divisor1
        self.numerador2 = numerador2
        self.divisor2 = divisor2

    def get_suma(self):
        suma = Fraction(self.numerador1,self.divisor1) + Fraction(self.numerador2,self.divisor2)
        return suma
    def get_resta(self):
        resta = Fraction(self.numerador1,self.divisor1) - Fraction(self.numerador2,self.divisor2)
        return resta

    def get_multiplicacion(self):
        multiplicacion = Fraction(self.numerador1,self.divisor1) * Fraction(self.numerador2,self.divisor2)
        return multiplicacion

    def get_division(self):
        division = Fraction(self.numerador1,self.divisor1) / Fraction(self.numerador2,self.divisor2)
        return division

f = Fraccion(2,3, 1,3)
print(f.get_suma(), f.get_resta(), f.get_multiplicacion(), f.get_division())

