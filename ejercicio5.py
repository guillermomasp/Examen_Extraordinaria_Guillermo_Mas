#Función para que haga el cifrado

def cesar(chain,llave):
    chain = chain.lower()
    key = llave.lower()
    cesar = ""
    for i in range(len(chain)):
        cesar += chr((ord(chain[i]) + ord(llave[i%len(llave)]) - 2*ord('a'))%26 + ord('a'))
    return cesar