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


    #1 perdiz en un peral, 2 tortolas y , 3 gallinas francesas, 4 pájaros cantando, 5   anillos de oro, 6 gansos una puesta, 7 cisnes nadando, 8 críadas un ordeño,
# 9 damas bailando , 10 señores de un salto, 11 gaiteros, 12 bateristas tocando el tambor