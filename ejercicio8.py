#Creamos la función.
def ordenar(lista):
    for i in range(len(lista)):
         for j in range(len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

#Enseñamos la lista.
if _name_ == "_main_":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    print(ordenar(lista))