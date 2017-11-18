
def capturarCadenas(cantidad):
    cadenas = []

    for i in range(cantidad):
        cadena = input("Digita un cadena => ")
        cadenas.append(cadena)

    return cadenas

def obtenerCadenasIguales(cadenas):    
    cadenasIguales = []

    index = 0
    indexTmp = 0

    while index < len(cadenas):
        cadTemp = cadenas[index]        
        indexTmp = 0
        for cad in cadenas:    
            if str(cad) == str(cadTemp) and index != indexTmp and cad not in cadenasIguales:                
                cadenasIguales.append(cadTemp)
            indexTmp = indexTmp + 1   
        index = index + 1 
    
    return cadenasIguales

def principal():
    cadenas = capturarCadenas(4)
    cadenasIguales = obtenerCadenasIguales(cadenas)
    print("Cadenas Iguales => ", cadenasIguales)

principal()









