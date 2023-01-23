#Creamos la función:
def es_potencia_de_4(x):
    if not isinstance(x, int):
        return False
    while x % 4 == 0 and x > 0:
        x = x / 4
    return x == 1

#Le pedimos al usuario que nos mdiga su numero para hacer la comprobación
print("¿Que número quiere comprobar?")
x = int(input())
