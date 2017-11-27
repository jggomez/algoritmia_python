
def solicitarPalabra():
    return input("Por favor digite una palabra => ")

def longitudPalabra(palabra):
    cont = 0
    for i in palabra:
        cont += 1

    return cont

def sumatoriaNumeros(hasta):
    sum = 0
    for i in range(hasta):
        sum += (i+1)
    return sum

def ppal():
    palabra = solicitarPalabra()
    longitud = longitudPalabra(palabra)
    sum = sumatoriaNumeros(longitud)
    print("La palabra tiene ", longitud, " caracteres")
    print("La sumatoria es => ", sum)

ppal()    