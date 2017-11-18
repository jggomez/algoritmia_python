
def calcularPotencia(base, exponente):
  resultado = 1
  for i in range(exponente):
    resultado = resultado * base
  print(resultado)
  
calcularPotencia(2, 3)