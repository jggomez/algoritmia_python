import turtle

lapiz = turtle.Turtle()


def pintarTriangulo(long, lados):
    i = 0
    while i < lados:
        lapiz.forward(long)
        lapiz.right(360 / lados)
        i += 1


pintarTriangulo(50, 3)
pintarTriangulo(50, 4)
pintarTriangulo(50, 5)

turtle.mainloop()
