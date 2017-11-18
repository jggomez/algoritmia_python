
def calcularPromedio(listaNumeros):
    suma = 0
    i = 0

    for elemento in listaNumeros:
        suma += elemento
        i += 1
        
    promedio = suma / i

    return promedio

def ppal():
    listaDeNumeros = [2.5, 2, 3, 5]
    promedioResp = calcularPromedio(listaDeNumeros)    
    print(promedioResp)  

ppal()    