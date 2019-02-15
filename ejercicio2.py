class Contador():
    def __init__(self,numero):
        self.numero = numero

    def get_count(self):
        count = 0
        count += self.numero
        return count

c = Contador(-3)
print(c.get_count())
