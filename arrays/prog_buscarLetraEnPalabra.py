
def solicitarPalabra():
    return input("Por favor digite una palabra => ")

def pintarLineaAbajoPalabra(palabra):
    numLetras = len(palabra)
    for i in range(numLetras):
        print("_", end=" ")
    print()

def solicitarLetra():
    return input("Por favor digite una letra => ")

def buscarPosicionLetra(palabra, letra):
    cont = 1
    for i in palabra:
        if i == letra:
            return cont
        cont += 1

    return -1

def ppal():
    palabra = solicitarPalabra()
    pintarLineaAbajoPalabra(palabra)
    letra = solicitarLetra()
    posicion = buscarPosicionLetra(palabra, letra)

    if posicion != -1:
        print("la letra esta en la posición => ", posicion)
    else:
        print("la palabra no contiene la letra")

ppal()