
import random

IMAGENES = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

PALABRAS = [
    "universidad",
    "america",
    "colombia",
    "murcielago"
]

def seleccionarPalabra():
    numPalabra = random.randint(0,3)
    return PALABRAS[numPalabra]

def pintarJugada(indiceImagen, palabra, indicesPalabra):

    print(IMAGENES[indiceImagen])
    lonPalabra = len(palabra)    

    for i in range(lonPalabra):

        existe = existeIndice(i, indicesPalabra)

        if(existe):
            print(palabra[i], end=" ")
            if((i+1) == lonPalabra):        
                print("")
                print("___________________________________ ")
        elif((i+1) == lonPalabra):
            print("_ ")
            print("")
            print("___________________________________ ")
        else:
            print("_ ", end=" ")

def existeIndice(indice, indicesPalabras):

    if(indicesPalabras is not None):
        for indPalabra in indicesPalabras:
            if(indPalabra == indice):
                return True

    return False

def pedirLetra():
    letra = input("Por favor digite una letra: ")
    #TODO Validar que es una letra
    return letra

def verificarLetraEnCadena(letra, palabra):
    
    arrIndiceLetras = []
    for i in range(len(palabra)):
        if palabra[i] == letra:
            arrIndiceLetras.append(i)

    return arrIndiceLetras

def principal():
    palabra = seleccionarPalabra()
    pintarJugada(0, palabra, None)

    oportunidades = 6
    oportunidadesDesperdiciadas = 0
    indiceImagen = 0

    indicesPalabraTotal = []

    while(oportunidadesDesperdiciadas <= 5):
        letra = pedirLetra()
        indicesPalabra = verificarLetraEnCadena(letra, palabra)

        if(len(indicesPalabra) == 0):
            oportunidadesDesperdiciadas = oportunidadesDesperdiciadas + 1
            indiceImagen = indiceImagen + 1

        if(len(indicesPalabra) > 0):
            for i in indicesPalabra:
                indicesPalabraTotal.append(i)
        
        pintarJugada(indiceImagen, palabra, indicesPalabraTotal)

        if(len(indicesPalabraTotal) == len(palabra)):
            print("Ganaste!!")
            return;

    if(oportunidadesDesperdiciadas == 6):
        print("Lo siento perdiste!!")

    
principal()

    







