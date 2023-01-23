import itertools

#Creamos la función que nos cuente el valor de las letras.
def numeros(word):
    permutaciones = list(itertools.permutations(word))
    permutaciones.sort()
    position = permutaciones.index(tuple(word))
    return position + 1

#Pedimos al usuario que inserte unas letras para comprobar:
print("¿Qué letras quieres conocer su valor numérico?")
word = int(input())


