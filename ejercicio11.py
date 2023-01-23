#Creamos la función:
def es_potencia_de_4(x):
    if not isinstance(x, int):
        return False
    while x % 4 == 0 and x > 0:
        x = x / 4
    return x == 1

