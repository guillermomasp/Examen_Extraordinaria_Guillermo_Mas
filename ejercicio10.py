import math
#Le preguntamos al usuario que base y exponente quiere usar.
print("¿Que numero quiere que sea su base?")
base = int(input())
print("¿Y su exponente?")
exponente = int(input())

#Creamos la función.
def potencia(base, exponente):
    if exponente < 0:
        print(None)
    else:
        return base ^ exponente

print(base ^ exponente)