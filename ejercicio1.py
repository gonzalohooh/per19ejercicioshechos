class Cuenta():
    def __init__(self, ingreso, reintegro, transferencia):
        self.ingreso = ingreso
        self.reintegro = reintegro
        self.transferencia = transferencia

    def get_ingreso(self):
        return self.ingreso

    def get_reintegro(self):
        return self.reintegro

    def get_transferencia(self):
        return self.transferencia


c = Cuenta(300,200,100)
print(c.get_transferencia())
