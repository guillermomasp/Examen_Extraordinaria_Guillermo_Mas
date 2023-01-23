#Creamos la función
def ordenar(lista):
    for i in range(len(lista)):
         for j in range(len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista