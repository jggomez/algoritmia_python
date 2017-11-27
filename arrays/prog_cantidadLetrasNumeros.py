
def solicitarPalabra():
    return input("Por favor digite una palabra => ")


def isAlfanumerica(palabra):
    tieneCaracteres = False
    tieneNumeros = False
    for car in palabra:
        if car.isdigit():
            tieneNumeros = True
        else:
            tieneCaracteres = True

    return (tieneCaracteres and tieneNumeros)


def numCaracteres(palabra):
    numCaracteres = 0
    for car in palabra:
        if car.isdigit() is False:
            numCaracteres += 1

    return numCaracteres


def numDigitos(palabra):
    cont = 0
    for car in palabra:
        if car.isdigit():
            cont += 1

    return cont


def ppal():
    palabra = solicitarPalabra()
    esAlfaNum = isAlfanumerica(palabra)

    if(not esAlfaNum):
         print("No contiene numeros o letras")
         return

    numCarac = numCaracteres(palabra)
    print("Numero de caracteres => ", numCarac)

    contNumeros = numDigitos(palabra)
    print("Numero de digitos => ", contNumeros)


ppal()
