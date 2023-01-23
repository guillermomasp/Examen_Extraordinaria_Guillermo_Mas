#Función para que haga el cifrado

def original(chain,key):
    chain = chain.lower()
    key = key.lower()
    original = ""
    for i in range(len(chain)):
        original += chr((ord(chain[i]) + ord(key[i%len(key)]) - 2*ord('a'))%26 + ord('a'))
    return original

#Creamos la función del descifrado del Cesar
def cesar(chain,key):
    chain = chain.lower()
    key = key.lower()
    cesar = ""
    for i in range(len(chain)):
        cesar += chr((ord(chain[i]) - ord(key[i%len(key)]) + 26)%26 + ord("a"))
    return cesar