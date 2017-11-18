

def buscarPares(listaNumeros):
    arrNumPares = []

    for numero in listaNumeros:
        if numero == 0 or numero%2 == 0:
            arrNumPares.append(numero)

    return arrNumPares

def buscarImpares(listaNumeros):
    arrNumImpares = []

    for numero in listaNumeros:
        if numero%2 != 0:
            arrNumImpares.append(numero)

    return arrNumImpares

def ppal():
    listaNumeros = [2,5,6,8,25,100]
    arrNumPares = buscarPares(listaNumeros)

    print("Los números pares son: ", end =" ")
    for num in arrNumPares:
        print(num, end = " ")

    print("")

    arrNumImpares = buscarImpares(listaNumeros)
    print("Los números impares son: ", end =" ")
    for numero in arrNumImpares:
        print(numero, end=" ")
    
ppal()    