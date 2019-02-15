
def duck_duck_goose(numero):
    jugadores = ['Jesus', 'Luis', 'Roberto', 'Paco']
    posicion = ['1', '2', '3', '4']
    resultado = dict(zip(posicion,jugadores))
    return resultado[numero]
numero = input('Número: ')
print(duck_duck_goose(numero))

