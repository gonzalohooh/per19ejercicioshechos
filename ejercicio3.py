from datetime import datetime

class Libro():
    def __init__(self,prestamo,devolucion,dame_info):
        self.prestamo = prestamo
        self.devolucion = devolucion
        self.dame_info = dame_info

    def get_prestamo(self):
        return self.prestamo

    def get_devolucion(self):
        return self.devolucion

    def get_dias_prestado(self):
        def days_between(d1, d2):
            d1 = datetime.strptime(d1, "%Y-%m-%d")
            d2 = datetime.strptime(d2, "%Y-%m-%d")
            return abs((d2 - d1).days)
        dif = days_between(self.prestamo,self.devolucion)
        return dif


    def get_titulo(self):
        autor = self.dame_info[0]
        return autor

    def get_autor(self):
        titulo = self.dame_info[1]
        return titulo

l = Libro('2019-1-30','2019-2-3',['El sanador de caballos', 'Gonzalo Giner'])
print('El libro ha sido prestado ',l.get_dias_prestado(), 'días')
print('El título del libro es ',l.get_titulo())
print('El autor del libro es ',l.get_autor())
