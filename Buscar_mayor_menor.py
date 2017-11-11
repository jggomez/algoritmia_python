
def solicitarDatos(numVeces):
    numeros = []

    indice = 1

    while indice <= numVeces:
        num = int(input("Digite un número => "))
        numeros.append(num)
        indice = indice + 1    

    return numeros

def obtenerNumeroMayor(numeros):
    numMayor = 0

    indice = 0
    tam = len(numeros)

    while indice < tam:
        num = numeros[indice]
        if num > numMayor:
            numMayor = num
        indice = indice + 1

    #for num in numeros:
        #if num > numMayor
           # numMayor = num
    
    return numMayor

def obtenerNumeroMenor(numeros):
    numMenor = 999999999999

    for num in numeros:
        if num < numMenor:
            numMenor = num

    return numMenor

def principal():
    nombre = "juan"
    print(nombre[2])

    numVeces = int(input("Cuantos numeros quiere? => "))
    numeros = solicitarDatos(numVeces)
    numMayor = obtenerNumeroMayor(numeros)
    print("El número mayor es => ", numMayor)
    numMenor = obtenerNumeroMenor(numeros)
    print("El número menor es => ", numMenor)

principal()




