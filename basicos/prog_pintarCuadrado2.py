import turtle

lapiz = turtle.Turtle()


def pintarCuadrado(long, angulo):
    lados = 4
    i = 0
    while i < lados:
        lapiz.forward(long)
        lapiz.right(angulo)
        i += 1


def posicionCuadradoHorizontalDer(long):
    lapiz.right(90)
    lapiz.forward(long)
    lapiz.left(90)


def posicionCuadradoHorizontalIzq(long):
    lapiz.forward(long)


def posicionCuadradoVertical(long):
    lapiz.forward(long)


def pintarCuadrados(long, numveces, tipoPosicion):
    contador = 1
    while contador <= numveces:
        pintarCuadrado(long, 90)
        if tipoPosicion == 1:
            posicionCuadradoHorizontalDer(long)
        elif tipoPosicion == 2:
            posicionCuadradoVertical(long)
        elif tipoPosicion == 3:
            posicionCuadradoHorizontalIzq(long)
        contador = contador + 1


def pintarCuadradoDeCuadrados():
    #Se pinta cuadrados arriba-horizontal
    lapiz.left(90)
    pintarCuadrados(50, 4, 1)
    #Se pinta cuadrados derecha-vertical
    lapiz.right(180)
    pintarCuadrados(50, 3, 2)
     #Se pinta cuadrados abajo-horizontal
    lapiz.right(90)
    lapiz.forward(50)
    pintarCuadrados(50, 3, 3)
    #Se pinta cuadrados izquierda-vertical
    lapiz.right(90)
    lapiz.forward(50)
    pintarCuadrados(50, 2, 2)

pintarCuadradoDeCuadrados()

turtle.mainloop()
