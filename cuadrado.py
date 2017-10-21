import turtle

lapiz = turtle.Turtle()

def pintarCuadrado(long, grados):
    lapiz.forward(long)
    lapiz.left(grados)
    lapiz.forward(long)
    lapiz.left(grados)
    lapiz.forward(long)
    lapiz.left(grados)
    lapiz.forward(long)


def posicionCuadrado(long, grados):
    lapiz.left(grados)
    lapiz.forward(long)

contador = 1

while(contador < 5):
    pintarCuadrado(50, 90)
    posicionCuadrado(50, 90)
    contador = contador + 1    
    pintarCuadrado(50, 90)
    pintarCuadrado(50, 90)
    posicionCuadrado(50, 90)

turtle.mainloop()
