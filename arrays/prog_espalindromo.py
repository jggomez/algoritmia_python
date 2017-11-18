
def es_palindromo(cadena):

    longCadena = len(cadena)
    indice = longCadena - 1;
    cadenaTemporal = ""

    while(indice >= 0):
        caracter = cadena[indice]
        cadenaTemporal = cadenaTemporal + caracter
        indice = indice - 1

    if cadena == cadenaTemporal:
        return True

    return False

def ppal():
    palabras = [
        "oso",
        "rajar",
        "ojo",
        "america campeon"
    ]

    for palabra in palabras:
        esPalindromo = es_palindromo(palabra)
        if(esPalindromo):
            print("la palabra ", palabra, " SI es palindromo")
        else:
            print("la palabra ", palabra, " NO es palindromo")

ppal()


