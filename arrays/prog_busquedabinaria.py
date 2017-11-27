

def busquedaBinaria(numeros, numeroBuscar, low, high):

    if low > high:
        return False

    mitad = int((low + high) / 2)

    if(numeros[mitad] == numeroBuscar):
        return True
    elif numeros[mitad] > numeroBuscar:
        return busquedaBinaria(numeros, numeroBuscar, low, mitad - 1)
    else:
        return busquedaBinaria(numeros, numeroBuscar, mitad + 1, high)


def ppal():
    numeros = [1, 3, 4, 6, 10, 11, 25, 28, 105, 200, 325, 508]
    numBuscar = int(input("Digita un número a buscar => "))
    result = busquedaBinaria(numeros, numBuscar, 0, len(numeros) - 1)

    if result is True:
        print("El número se encuentra en la lista")
    else:
        print("El número no se encuentra en la lista")

ppal()